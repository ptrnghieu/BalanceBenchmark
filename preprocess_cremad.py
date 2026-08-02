"""Preprocess CREMA-D into the layout expected by balancemm/datasets/cremad_dataset.py.

Reads raw AudioWAV/*.wav and VideoFlash/*.flv, produces:
  <out>/audio/<vid>.pt              log-mel spectrogram tensor
  <out>/visual/<vid>/frame_XX.jpg   extracted frames
  <out>/train.txt, <out>/test.txt   csv: vid,emotion (speaker-disjoint split)
  <out>/stat.csv                    all vid,emotion pairs

Usage:
  python preprocess_cremad.py --src ~/data/CREMA-D --dst ~/data/CREMAD_proc --fps 3
"""
import argparse
import csv
import os
import random
import subprocess
from pathlib import Path

import librosa
import numpy as np
import torch
from tqdm import tqdm

VALID = {"NEU", "HAP", "SAD", "FEA", "DIS", "ANG"}


def wav_to_logmel(wav_path: Path) -> torch.Tensor:
    y, sr = librosa.load(str(wav_path), sr=22050)
    if len(y) < sr:  # pad to 1s minimum
        y = np.pad(y, (0, sr - len(y)))
    mel = librosa.feature.melspectrogram(y=y, sr=sr, n_fft=1024, hop_length=512, n_mels=128)
    log_mel = librosa.power_to_db(mel).astype(np.float32)
    return torch.from_numpy(log_mel)


def extract_frames(video_path: Path, out_dir: Path, fps: int) -> int:
    out_dir.mkdir(parents=True, exist_ok=True)
    cmd = [
        "ffmpeg", "-y", "-loglevel", "error",
        "-i", str(video_path),
        "-vf", f"fps={fps}",
        "-q:v", "2",
        str(out_dir / "frame_%03d.jpg"),
    ]
    subprocess.run(cmd, check=True)
    return len(list(out_dir.glob("*.jpg")))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True, help="CREMA-D raw root (has AudioWAV/, VideoFlash/)")
    ap.add_argument("--dst", required=True, help="Output root")
    ap.add_argument("--fps", type=int, default=3, help="Frames per second to extract")
    ap.add_argument("--test-speakers", type=int, default=15, help="Speakers held out for test")
    ap.add_argument("--seed", type=int, default=42)
    args = ap.parse_args()

    src = Path(args.src).expanduser()
    dst = Path(args.dst).expanduser()
    audio_src = src / "AudioWAV"
    video_src = src / "VideoFlash"
    audio_dst = dst / "audio"
    visual_dst = dst / "visual"
    audio_dst.mkdir(parents=True, exist_ok=True)
    visual_dst.mkdir(parents=True, exist_ok=True)

    wavs = sorted(audio_src.glob("*.wav"))
    print(f"Found {len(wavs)} audio clips")
    if not wavs:
        raise SystemExit(f"No wavs in {audio_src}")

    rows: list[tuple[str, str, str]] = []  # (vid, emotion, speaker)
    for wav in tqdm(wavs, desc="metadata"):
        vid = wav.stem  # 1001_DFA_ANG_XX
        parts = vid.split("_")
        if len(parts) < 3:
            continue
        speaker, _, emo = parts[0], parts[1], parts[2]
        if emo not in VALID:
            continue
        video = video_src / f"{vid}.flv"
        if not video.exists():
            continue
        rows.append((vid, emo, speaker))
    print(f"{len(rows)} clips with matching video and valid emotion")

    # split by speaker to avoid identity leak
    speakers = sorted({s for _, _, s in rows})
    rng = random.Random(args.seed)
    rng.shuffle(speakers)
    test_spk = set(speakers[: args.test_speakers])
    print(f"Total speakers: {len(speakers)}, test speakers: {len(test_spk)}")

    with (dst / "stat.csv").open("w", newline="") as f:
        w = csv.writer(f)
        for vid, emo, _ in rows:
            w.writerow([vid, emo])

    train_rows = [(vid, emo) for vid, emo, s in rows if s not in test_spk]
    test_rows = [(vid, emo) for vid, emo, s in rows if s in test_spk]
    print(f"train={len(train_rows)}  test={len(test_rows)}")

    for name, r in [("train.txt", train_rows), ("test.txt", test_rows)]:
        with (dst / name).open("w", newline="") as f:
            w = csv.writer(f)
            w.writerows(r)

    # audio spectrograms
    for vid, _, _ in tqdm(rows, desc="audio->pt"):
        out = audio_dst / f"{vid}.pt"
        if out.exists():
            continue
        try:
            fbank = wav_to_logmel(audio_src / f"{vid}.wav")
            torch.save(fbank, out)
        except Exception as e:
            print(f"[audio fail] {vid}: {e}")

    # frames
    for vid, _, _ in tqdm(rows, desc="video->jpg"):
        out = visual_dst / vid
        if out.exists() and any(out.glob("*.jpg")):
            continue
        try:
            extract_frames(video_src / f"{vid}.flv", out, args.fps)
        except subprocess.CalledProcessError as e:
            print(f"[video fail] {vid}: {e}")

    print("Done. Set dataset_config.yaml paths to:")
    print(f"  visual_path : {visual_dst}/")
    print(f"  audio_path  : {audio_dst}/")
    print(f"  stat_path   : {dst}/stat.csv")
    print(f"  train_txt   : {dst}/train.txt")
    print(f"  test_txt    : {dst}/test.txt")


if __name__ == "__main__":
    main()
