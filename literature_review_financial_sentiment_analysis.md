# Tổng quan tài liệu về Phân tích cảm xúc trong tài chính (Financial Sentiment Analysis): bài toán, phương pháp, dữ liệu và bối cảnh tiếng Việt

## Tóm tắt

Phân tích cảm xúc tài chính (Financial Sentiment Analysis – FSA) thường được hiểu là phân loại văn bản tài chính thành tích cực, tiêu cực hoặc trung lập. Bài tổng quan này lập luận rằng cách hiểu đó quá hẹp. FSA gồm nhiều bài toán (phân loại, chấm điểm, theo khía cạnh, theo thực thể, theo sự kiện), nhiều loại nhãn (cảm xúc văn bản, tâm lý nhà đầu tư, tác động kỳ vọng lên giá), nhiều nguồn dữ liệu và nhiều mục tiêu ứng dụng. Một mô hình tốt trên benchmark cảm xúc chưa chắc hữu ích cho dự báo tài chính, và khoảng cách này càng rõ ở ngôn ngữ ít tài nguyên như tiếng Việt. Bài khảo sát giai đoạn 2000 đến 2026 theo cấu trúc: nền tảng khái niệm, taxonomy bài toán, tiến hóa phương pháp (đến LLM), dữ liệu–gán nhãn–đánh giá, ứng dụng, thách thức, rồi đi riêng vào FSA tiếng Việt, nơi tôi kiểm tra được năm công trình và chưa thấy benchmark công khai được chuẩn hóa.

**Từ khóa:** phân tích cảm xúc, tài chính, taxonomy, FinBERT, mô hình ngôn ngữ lớn, tiếng Việt, PhoBERT

---

## 1. Giới thiệu

### 1.1. Động lực và luận điểm trung tâm

Thị trường tài chính phản ứng với thông tin, và phần lớn thông tin đó ở dạng văn bản. Từ những năm 2000, một nhánh nghiên cứu chuyển văn bản thành chỉ báo định lượng về cảm xúc để kiểm tra mối liên hệ với lợi suất, biến động và khối lượng giao dịch. Luận điểm trung tâm của bài:

> FSA không chỉ là phân loại positive/negative/neutral. Nó gồm nhiều bài toán, nhiều loại nhãn, nhiều nguồn dữ liệu và nhiều mục tiêu downstream. Một mô hình tốt trên benchmark cảm xúc chưa chắc hữu ích cho dự báo tài chính, và khoảng cách này càng rõ ở ngôn ngữ ít tài nguyên như tiếng Việt.

### 1.2. Câu hỏi nghiên cứu

| RQ | Câu hỏi | Mục |
|---|---|---|
| RQ1 | FSA đã phát triển thế nào về bài toán, phương pháp và mô hình? | 3, 4 |
| RQ2 | Những tập dữ liệu, cách gán nhãn và giao thức đánh giá nào được dùng? | 5 |
| RQ3 | Cảm xúc tài chính được dùng trong ứng dụng downstream ra sao? | 6 |
| RQ4 | Thách thức và khoảng trống nghiên cứu chính là gì? | 7, 9 |
| RQ5 | FSA tiếng Việt đang ở mức nào so với nghiên cứu toàn cầu? | 8 |

### 1.3. Các khảo sát liên quan

Kearney và Liu (2014) khảo sát cảm xúc văn bản trong tài chính; Loughran và McDonald (2016) khảo sát phân tích văn bản trong kế toán–tài chính; Xing và cs. (2018) khảo sát dự báo tài chính dựa trên ngôn ngữ tự nhiên; Nie và cs. (2024) khảo sát LLM cho ứng dụng tài chính. Bài này khác ở chỗ tổ chức theo bài toán và loại nhãn, và dành riêng một phần cho tiếng Việt.

### 1.4. Phương pháp chọn tài liệu, mức xác minh và giới hạn

**Quy trình thực tế.** Tôi không có quyền truy cập Scopus, Web of Science, IEEE Xplore hay ACM DL, nên bài **không phải tổng quan hệ thống kiểu PRISMA**. Việc tìm kiếm dùng tìm kiếm web, đối chiếu với arXiv, ACL Anthology, trang tạp chí (MDPI, VNUHCM, JCC) và Crossref. Nhật ký truy vấn:

| Chủ đề | Từ khóa chính (tiếng Anh) |
|---|---|
| Khảo sát | financial sentiment analysis survey; textual analysis finance survey; LLM finance survey |
| Từ điển và nền tảng | Loughran McDonald; Tetlock media pessimism; message boards sentiment |
| Mô hình tiền huấn luyện | FinBERT (Araci; Yang); lexicons to transformers |
| LLM | ChatGPT stock return; BloombergGPT; FinGPT; PIXIU/FinMA; FinBen; GPT-4 vs FinBERT; look-ahead bias |
| Dữ liệu và gán nhãn | Financial PhraseBank; FiQA; entity-level corpus; annotator agreement |
| Tiếng Việt | Vietnamese financial sentiment; PhoBERT stock news; VN-Index sentiment |

**Tiêu chí áp dụng (không chính thức, không đếm số lượng):** đưa vào các công trình có thể xác minh thư mục, liên quan trực tiếp đến cảm xúc/văn bản tài chính hoặc là chuẩn tham chiếu của lĩnh vực; loại các trang tóm tắt, blog và bài không xác minh được tác giả. Tôi không lập sơ đồ sàng lọc vì không ghi số lượng ở từng bước.

**Mức xác minh.**
- *Nhóm A* (trích chi tiết từ trang bài hoặc bản HTML qua công cụ đọc trang; tôi không đọc trực tiếp PDF): Malo và cs. (2014), Araci (2019), Yang và cs. (2020), Nie và cs. (2024), Wu và cs. (2023), Xie và cs. (2023, 2024), Kirtac & Germano (2024), Shen & Zhang (2024), Vamvourellis & Mehta (2025), Li và cs. (2023), cùng các công trình tiếng Việt ở Mục 8.
- *Nhóm B* (chỉ tóm tắt và kết quả tìm kiếm): Tetlock (2007), Loughran & McDonald (2011, 2016), Das & Chen (2007), Antweiler & Frank (2004), Bollen và cs. (2011), Ding và cs. (2015), Lopez-Lira & Tang (2023), Glasserman & Lin (2023), Kearney & Liu (2014), Xing và cs. (2018), Mishev và cs. (2020), Maia và cs. (2018), Yang và cs. (2023, FinGPT), Zhang và cs. (2023, Instruct-FinGPT).

Số liệu là số do tác giả công bố. **Giới hạn:** (i) chưa có truy vấn trên các cơ sở dữ liệu trả phí; (ii) giai đoạn 2025–2026 chỉ được khảo sát qua một số tìm kiếm có mục tiêu, nên phần LLM gần đây chắc chắn chưa đầy đủ; (iii) các nhận định "chưa có công trình" chỉ đúng với tập tài liệu đã xem.

---

## 2. Nền tảng khái niệm

### 2.1. Ba khái niệm cần tách biệt

| Khái niệm | Câu hỏi | Ví dụ |
|---|---|---|
| **Cảm xúc văn bản** | Văn bản thể hiện sắc thái gì? | "Doanh thu giảm mạnh" mang sắc thái tiêu cực |
| **Tâm lý nhà đầu tư** | Nhà đầu tư lạc quan hay bi quan? | Chỉ số tâm lý tổng hợp từ nhiều nguồn |
| **Tác động kỳ vọng lên giá** | Thông tin tốt hay xấu cho giá? | Tin cắt giảm chi phí có thể tăng giá dù sắc thái trung tính |

Ba khái niệm không thể mặc định thay thế cho nhau. Phân biệt này thể hiện ngay trong các bộ nhãn: Financial PhraseBank yêu cầu người gán nhãn đánh giá "từ góc nhìn nhà đầu tư" (Malo và cs., 2014), còn Lopez-Lira & Tang (2023) yêu cầu mô hình đánh giá tiêu đề là tốt, xấu hay trung lập **đối với giá cổ phiếu của công ty**.

### 2.2. Cơ sở lý thuyết và bằng chứng ban đầu

Tetlock (2007) đo mức bi quan của truyền thông từ chuyên mục "Abreast of the Market" trên Wall Street Journal bằng phân tích thành phần chính, giai đoạn 1984–1999. Mức bi quan cao đi kèm áp lực giảm giá rồi giá hồi về mức cơ bản, còn mức bi quan cực đoan đi kèm khối lượng giao dịch lớn; tác giả diễn giải kết quả phù hợp với mô hình có nhà giao dịch nhiễu và thanh khoản, không phù hợp với việc xem nội dung truyền thông chỉ là đại diện cho thông tin cơ bản mới. Antweiler và Frank (2004) phân tích hơn 1,5 triệu bài đăng trên Yahoo! Finance; các nguồn thứ cấp mô tả khả năng dự báo lợi suất là yếu (cần đối chiếu bài gốc). Kearney và Liu (2014) tổng hợp rằng cảm xúc văn bản liên hệ với hành vi ở cấp cá nhân, doanh nghiệp và thị trường, đồng thời chỉ ra các điểm còn tranh luận.

---

## 3. Taxonomy các bài toán FSA

### 3.1. Khung phân loại

| Bài toán | Mục tiêu | Công trình ví dụ | Ghi chú |
|---|---|---|---|
| Phân loại cảm xúc câu/văn bản | Nhãn positive/negative/neutral | Malo và cs. (2014); Das & Chen (2007); Yang và cs. (2020) | Malo: câu; Das & Chen: bài đăng |
| Chấm điểm cảm xúc | Điểm liên tục | FiQA Task 1: điểm trong [−1, 1] cho tiêu đề và tweet (theo Araci, 2019) | Hồi quy |
| Chỉ số cảm xúc tổng hợp | Thước đo từ nhiều văn bản | Tetlock (2007); Loughran & McDonald (2011) | Đếm từ / thành phần chính |
| Theo khía cạnh (ABSA) | Cảm xúc theo khía cạnh | FiQA nhắm đến aspect-based sentiment (Maia và cs., 2018) | Chi tiết nhãn khía cạnh chưa xác minh |
| Theo thực thể | Cảm xúc hướng đến thực thể | FinLin (Daudert, 2020): điểm cảm xúc và điểm liên quan theo thực thể, kèm đoạn văn làm bằng chứng, trên báo cáo, tin tức và StockTwits | Corpus ngành ô tô, ba tháng |
| Cảm xúc chi tiết | Nhiều chiều tâm trạng | Bollen và cs. (2011): GPOMS (calm, alert, sure, vital, kind, happy) | Twitter, không riêng tài chính |
| Theo sự kiện / dự báo từ văn bản | Tác động của sự kiện lên giá | Ding và cs. (2015); Lopez-Lira & Tang (2023) | Giao điểm giữa FSA và dự báo |
| Lập trường (stance) | Lập trường với một chủ đề | Chưa có công trình trong tập đã xem | Khoảng trống về bằng chứng |

Hai lưu ý: ranh giới giữa các hàng không cứng (phân loại là cách đọc của tôi); và các công trình dự báo giá từ văn bản (Ding và cs., 2015) nên gọi là dự báo tài chính dựa trên văn bản, không gọi là FSA thuần túy.

### 3.2. Vì sao cần phân biệt

Xét câu minh họa (do tôi đặt): *"Công ty A báo lãi kỷ lục, trong khi công ty B thua lỗ nặng."* Phân loại cả câu có thể trả về trung lập; phân tích theo thực thể cho A tích cực, B tiêu cực. Tương tự, *"Doanh thu giảm nhưng biên lợi nhuận cải thiện đáng kể"* có nhãn phụ thuộc vào khía cạnh được chú ý.

Một bằng chứng trực tiếp từ tiếng Việt: nhóm Tung và cs. (2021) thay tên riêng, địa danh, tên tổ chức và mã chứng khoán bằng token giữ chỗ trước khi phân loại tiêu đề (qua mô tả mã nguồn của họ). Cách này tránh học thuộc tên công ty nhưng cũng làm mất thông tin về thực thể; nó phù hợp với phân loại cấp tiêu đề và không phù hợp với bài toán theo thực thể. Tin tài chính tiếng Việt thường nhắc nhiều doanh nghiệp và ngành trong cùng bài, nên bài toán theo thực thể và khía cạnh là hướng đáng quan tâm; đây là suy luận của tôi.

---

## 4. Tiến hóa phương pháp

### 4.1. Từ điển

Loughran và McDonald (2011) phân tích 50.115 hồ sơ 10-K giai đoạn 1994–2008 và thấy phần lớn từ mà từ điển Harvard xếp là tiêu cực không mang nghĩa tiêu cực trong báo cáo tài chính (ví dụ *liability, tax, board, vice*). Họ xây từ điển tài chính riêng và cho thấy thước đo dựa trên đó liên hệ rõ hơn với lợi suất quanh ngày nộp báo cáo, khối lượng, biến động, gian lận và điểm yếu trọng yếu. Ưu điểm: minh bạch, rẻ, dễ tái lập. Nhược điểm: bỏ qua ngữ cảnh. Malo và cs. (2014) nhấn mạnh cảm xúc của câu có thể khác cảm xúc của từng từ.

### 4.2. Học máy truyền thống và học sâu

Das và Chen (2007) kết hợp nhiều bộ phân loại bằng bỏ phiếu cho bài đăng bảng tin; họ báo cáo độ chính xác tương đương bộ phân loại Bayes nhưng ít dương tính giả hơn. Ding và cs. (2015) trích sự kiện từ tin tức, dùng mạng tensor nơ-ron và CNN sâu, báo cáo cải thiện khoảng 6% so với baseline trên tin Reuters và Bloomberg. Xing và cs. (2018) tổng quan giai đoạn trước Transformer.

### 4.3. Mô hình tiền huấn luyện

Araci (2019) tiền huấn luyện tiếp BERT trên TRC2-financial (tập con của Reuters TRC2: 46.143 tài liệu, hơn 29 triệu từ), rồi tinh chỉnh. Trên Financial PhraseBank (4.845 câu), FinBERT đạt accuracy 0,86 và F1 0,84 (0,97 và 0,95 trên tập đồng thuận 100%), so với ULMFit 0,83/0,79. Trên FiQA (1.174 tiêu đề và tweet), MSE 0,07 và R² 0,55; tác giả lưu ý FinBERT đánh giá bằng kiểm định chéo 10 lần, các baseline dùng tập kiểm thử chính thức, nên so sánh không trực tiếp.

Yang và cs. (2020) tiền huấn luyện một BERT khác (cũng tên FinBERT) từ đầu trên khoảng 4,9 tỷ token: báo cáo doanh nghiệp 10-K/10-Q (2,5 tỷ), bản ghi họp báo kết quả (1,3 tỷ) và báo cáo phân tích (1,1 tỷ). Mô hình được đánh giá trên Financial PhraseBank (4.840 câu), AnalystTone (10.000 câu) và FiQA (1.111 câu, chuyển thành nhị phân). Accuracy tốt nhất của FinBERT là 0,872, 0,887 và 0,844, so với BERT uncased 0,835, 0,850 và 0,730.

Mishev và cs. (2020) chạy hơn một trăm thí nghiệm từ từ điển đến Transformer; kết luận chính là biểu diễn theo ngữ cảnh vượt từ điển và bộ mã hóa cố định, còn Transformer rút gọn cho hiệu năng gần bản đầy đủ.

### 4.4. Mô hình ngôn ngữ lớn

Có ba cách dùng LLM, cần tách bạch vì không phải công trình LLM nào cũng là FSA theo nghĩa truyền thống.

**(a) LLM làm bộ chấm điểm tin tức / tín hiệu giao dịch.** Lopez-Lira & Tang (2023) cho ChatGPT đánh giá tiêu đề với giá cổ phiếu; tương quan dương có ý nghĩa thống kê với lợi suất ngày kế tiếp, mô hình cơ bản (GPT-1, GPT-2, BERT) không dự báo chính xác, rõ hơn ở cổ phiếu nhỏ. Kirtac & Germano (2024) so sánh OPT, BERT, FinBERT và từ điển Loughran–McDonald trên 965.375 bài báo tài chính Mỹ (01/2010–06/2023): độ chính xác dự đoán cảm xúc lần lượt 74,4%, 72,5%, 72,2% và 50,1%; tỷ số Sharpe của chiến lược mua–bán là 3,05, 2,11, 2,07 và 1,23. Các con số này là backtest do tác giả công bố; cơ sở gán nhãn để tính "độ chính xác" tôi chưa xác minh.

**(b) Đánh giá LLM đa dụng so với FinBERT trên benchmark cảm xúc.** Li và cs. (2023) đánh giá ChatGPT và GPT-4 trên tám tập dữ liệu thuộc năm nhóm tác vụ tài chính, báo cáo cả điểm mạnh và hạn chế so với mô hình tinh chỉnh. Shen & Zhang (2024) kết luận GPT-4o với ví dụ few-shot "có thể ngang một FinBERT được tinh chỉnh tốt" trên tin tức, báo cáo và thông báo doanh nghiệp. Vamvourellis & Mehta (2025) so sánh GPT-4o, GPT-4.1 và o3-mini zero-shot với hai FinBERT trên Financial PhraseBank và thấy lập luận (reasoning) không cải thiện kết quả; cấu hình sát nhãn người nhất là GPT-4o không dùng chain-of-thought, và lập luận có thể gây "nghĩ quá mức" ở câu phức tạp hoặc câu có mức đồng thuận người gán nhãn thấp. Các kết luận này nhất quán ở chỗ LLM few-shot/zero-shot gần bằng mô hình tinh chỉnh chứ chưa vượt rõ trên benchmark cảm xúc.

**(c) LLM chuyên ngành và benchmark.** BloombergGPT (Wu và cs., 2023) có 50 tỷ tham số, huấn luyện trên 363 tỷ token dữ liệu Bloomberg và 345 tỷ token dữ liệu tổng quát. PIXIU (Xie và cs., 2023) gồm FinMA (LLaMA tinh chỉnh theo hướng dẫn), bộ dữ liệu hướng dẫn khoảng 136.000 mẫu và bộ đánh giá FLARE; Zhang và cs. (2023) đề xuất Instruct-FinGPT (LLaMA-7B tinh chỉnh theo hướng dẫn trên dữ liệu cảm xúc tài chính nhỏ); Yang và cs. (2023) đề xuất FinGPT mã nguồn mở với LoRA. FinBen (Xie và cs., 2024) gồm 36 tập dữ liệu thuộc 24 tác vụ; trên 15 LLM, các mô hình làm tốt trích xuất thông tin và phân tích văn bản nhưng yếu ở suy luận nâng cao, sinh văn bản và dự báo, còn tinh chỉnh theo hướng dẫn giúp phân tích văn bản nhưng ít lợi ở tác vụ phức tạp. Nie và cs. (2024) khảo sát cả mảng này và nêu các vấn đề mở như thiên lệch nhìn trước, ô nhiễm dữ liệu và khả năng diễn giải.

### 4.5. Phân tích so sánh

| Công trình | Dữ liệu | Bài toán | Phương pháp | Kết quả chính (theo tác giả) |
|---|---|---|---|---|
| Loughran & McDonald (2011) | 10-K, 1994–2008 | Giọng điệu văn bản | Từ điển tài chính | Harvard gán sai nhiều từ; từ điển mới liên hệ tốt hơn với kết quả |
| Malo và cs. (2014) | ~5.000 câu tin Phần Lan | Cảm xúc câu | LPS + từ điển mở rộng | Vượt đếm từ và mô hình chung |
| Araci (2019) | PhraseBank, FiQA | Phân loại + chấm điểm | BERT + TRC2-financial | Acc 0,86 / F1 0,84 trên PhraseBank |
| Yang và cs. (2020) | PhraseBank, AnalystTone, FiQA | Phân loại | BERT từ đầu, 4,9 tỷ token | Acc 0,844–0,887, hơn BERT chung |
| Kirtac & Germano (2024) | 965.375 tin, 2010–2023 | Cảm xúc → lợi suất | OPT, BERT, FinBERT, LM | OPT cao nhất cả về độ chính xác và Sharpe |
| Vamvourellis & Mehta (2025) | PhraseBank | Phân loại zero-shot | GPT-4o, 4.1, o3-mini vs FinBERT | Lập luận không giúp |

Một số điểm rút ra:

- **Hai FinBERT khác nhau về ngữ liệu và tác vụ.** Araci tiếp tục tiền huấn luyện BERT trên một tập tin tức nhỏ (~29 triệu từ); Yang và cs. tiền huấn luyện từ đầu trên báo cáo doanh nghiệp, họp báo kết quả và báo cáo phân tích (~4,9 tỷ token). Kích thước mẫu đánh giá cũng khác (PhraseBank 4.845 so với 4.840 câu; FiQA 1.174 so với 1.111 câu), nên không so điểm trực tiếp được.
- **Khi nào Transformer vượt từ điển?** Mishev và cs. (2020) và Kirtac & Germano (2024) cho thấy mô hình theo ngữ cảnh vượt từ điển trên đánh giá cảm xúc ở mức câu/bài báo. Nhưng từ điển Loughran–McDonald được xây cho văn bản dài như 10-K và gắn với kết quả tài chính; độ chính xác 50,1% của nó trong Kirtac & Germano phụ thuộc vào cách gán nhãn tham chiếu, và Mục 2.1 cho thấy nhãn không đồng nhất.
- **Tín hiệu dự báo yếu hơn khi kiểm định chặt hơn.** Bollen và cs. (2011) báo cáo độ chính xác 87,6% khi dự đoán chiều DJIA, còn Lopez-Lira & Tang mô tả tương quan rất nhỏ; hai bên khác dữ liệu và thiết lập nên không so trực tiếp.

---

## 5. Dữ liệu, gán nhãn và đánh giá

### 5.1. Nguồn dữ liệu và cảm xúc phụ thuộc nguồn

| Nguồn | Ví dụ | Đặc điểm | Vấn đề |
|---|---|---|---|
| Báo cáo doanh nghiệp | 10-K (Loughran & McDonald, 2011) | Chính thức, dài | Cảm xúc tinh tế, nhiều văn bản lặp |
| Tin tức | Tetlock (2007); Ding và cs. (2015); Kirtac & Germano (2024) | Biên tập | Cảm xúc không trực tiếp; độ trễ |
| Bảng tin / mạng xã hội | Antweiler & Frank (2004); Das & Chen (2007); Bollen và cs. (2011) | Ngắn, chủ quan, tiếng lóng | Nhiễu, thao túng |
| Báo cáo phân tích, họp báo kết quả | Yang và cs. (2020) dùng làm ngữ liệu tiền huấn luyện | Chuyên môn | Ít bộ nhãn công khai (trong tập đã xem) |

Một mô hình huấn luyện trên Financial PhraseBank không mặc nhiên tốt trên StockTwits hay báo cáo thường niên. Trong tập tài liệu đã xem tôi chưa thấy công trình đánh giá trực tiếp tổng quát hóa giữa các nguồn; khẳng định "chưa ai làm" cần kiểm tra bằng tìm kiếm hệ thống.

### 5.2. Bộ dữ liệu chuẩn và vấn đề tái lập

- **Financial PhraseBank** (Malo và cs., 2014): khoảng 5.000 câu được lấy mẫu từ 53.400 câu trong 10.000 bài tin về các công ty niêm yết trên OMX Helsinki, gán nhãn theo góc nhìn nhà đầu tư. Các bài sau dùng số câu hơi khác nhau (4.845 trong Araci, 4.840 trong Yang và cs.), một dấu hiệu rằng phiên bản dữ liệu cần được ghi rõ khi so sánh.
- **FiQA** (Maia và cs., 2018): thử thách mở tại The Web Conference 2018 về cảm xúc theo khía cạnh và hỏi đáp; dữ liệu từ StackExchange, Reddit và StockTwits (2009–2017). Số mẫu cảm xúc được báo cáo là 1.111, 1.173 hoặc 1.174 tùy bài.
- **FinLin** (Daudert, 2020): corpus cảm xúc theo thực thể, đa nguồn, có điểm cảm xúc và liên quan.
- **AnalystTone** (theo Yang và cs., 2020): 10.000 câu từ báo cáo phân tích (3.580 tích cực, 1.830 tiêu cực, 4.590 trung lập).

### 5.3. Gán nhãn và kiểm soát chất lượng

Financial PhraseBank là trường hợp được ghi nhận chi tiết nhất (Malo và cs., 2014):
- 16 người gán nhãn có kiến thức thị trường tài chính (3 nhà nghiên cứu, 13 sinh viên thạc sĩ Aalto), mỗi câu có 5–8 lượt gán, nhãn lấy theo đa số.
- Trên tập con 150 câu do cả 16 người gán: đồng thuận cặp 74,9%; phân biệt tích cực–tiêu cực đạt 98,7%, tiêu cực–trung lập 94,2%, còn **tích cực–trung lập chỉ 75,2%**, tức là khó nhất.
- Tập "đồng thuận 100%" có 2.259 câu (Malo; bản Hugging Face liệt kê 2.264), phân bố 13,4% tiêu cực, 61,4% trung lập, 25,2% tích cực; tập ">50%" có 4.840 câu.

Ba hệ quả:
1. **Nhãn mang giả định.** "Cảm xúc" ở đây là phán đoán về tác động tới nhà đầu tư, không thuần là sắc thái văn bản (Mục 2.1).
2. **Chọn ngưỡng đồng thuận làm thay đổi bài toán.** Araci báo cáo 0,86 accuracy trên toàn bộ nhưng 0,97 trên tập đồng thuận 100%; chọn tập nào quyết định mức "chính xác".
3. **Bất đồng không chỉ là nhiễu.** Vamvourellis & Mehta (2025) thấy suy luận của LLM kém hơn ở câu có mức đồng thuận thấp, gợi ý rằng bất đồng gắn với độ khó ngữ nghĩa thật. Trong tập đã xem, các bộ dữ liệu khác thường không công bố mức đồng thuận nên không so được. Câu hỏi nên ép một nhãn hay biểu diễn bất đồng vẫn còn mở.

### 5.4. Giao thức đánh giá

Khung dưới là đề xuất tổ chức của tôi, không phải thống kê từ các công trình:

| Mục tiêu | Chỉ số |
|---|---|
| Phân loại | Accuracy, Macro-F1, Precision, Recall |
| Chấm điểm | MAE, RMSE, tương quan Pearson/Spearman (FiQA: MSE, R² như trong Araci) |
| Dự báo tài chính | Độ chính xác chiều, MAE, RMSE, Sharpe (Kirtac & Germano) |
| Giao dịch | Lợi nhuận tích lũy, chi phí giao dịch, sụt giảm tối đa |

Về chia dữ liệu: ngẫu nhiên, phân tầng, theo thời gian, walk-forward, ngoài miền. Chia theo thời gian đặc biệt quan trọng; huấn luyện trên dữ liệu muộn hơn kiểm thử hoặc để tin gần trùng lặp ở cả hai tập làm kết quả không phản ánh khả năng triển khai. Ví dụ trong tập đã xem: Araci dùng kiểm định chéo 10 lần trên FiQA trong khi các baseline dùng tập kiểm thử chính thức; Phong và cs. (2026) dùng kiểm định chéo 10 lần cho dự báo chiều VN-Index, một thiết lập dễ gây rò rỉ thời gian với chuỗi giá (nhận định của tôi, chưa kiểm tra chi tiết bài).

---

## 6. Ứng dụng

| Nhóm | Câu hỏi | Công trình ví dụ |
|---|---|---|
| **Đo lường cảm xúc** | Văn bản thể hiện tâm lý gì? | Loughran & McDonald (2011); Das & Chen (2007); Malo và cs. (2014) |
| **Phân tích phản ứng thị trường** | Thị trường phản ứng thế nào? | Tetlock (2007); Antweiler & Frank (2004); Vu và cs. (2023) |
| **Dự báo / giao dịch** | Cảm xúc có làm tín hiệu dự báo? | Bollen và cs. (2011); Ding và cs. (2015); Lopez-Lira & Tang (2023); Kirtac & Germano (2024) |

Hệ quả logic: đo cảm xúc tốt không chứng minh dự báo được giá; tương quan không chứng minh dự báo ngoài mẫu; dự báo được lợi suất không bảo đảm chiến lược có lãi sau chi phí. Một số con số cần đọc kèm thiết lập: 87,6% của Bollen và cs. (dự đoán chiều DJIA hằng ngày; mẫu chưa xác minh); khoảng 6% của Ding và cs. (so với baseline); 9 và 29 điểm cơ bản mỗi ngày (vị thế mua và bán) của Lopez-Lira & Tang (bản 2024); Sharpe 3,05 của Kirtac & Germano (backtest, 2010–2023). Quản trị rủi ro và tư vấn tự động chủ yếu được thảo luận trong các khảo sát LLM (Nie và cs., 2024), tôi chưa có bằng chứng thực nghiệm đủ mạnh.

---

## 7. Thách thức và vấn đề mở

1. **Thiên lệch nhìn trước.** LLM có thể đã thấy diễn biến giá sau tin. Glasserman và Lin (2023) dùng GPT-3.5 trên tiêu đề tin các công ty S&P 500 và so sánh bản gốc với bản ẩn danh: trong mẫu, bản ẩn danh tốt hơn, tức hiệu ứng xao nhãng lấn át thiên lệch nhìn trước; ngoài mẫu thiên lệch nhìn trước không phải mối lo (bản thảo arXiv, chưa xác minh bình duyệt). Điều này gợi ý các kết quả backtest LLM (như Kirtac & Germano, 2024, giai đoạn 2010–2023) cần được đọc cùng ngày cắt dữ liệu huấn luyện của mô hình.
2. **Tái lập và chi phí.** Mô hình đóng hay API đổi phiên bản làm khó tái lập; FinGPT, FinMA và Transformer rút gọn là hướng giảm chi phí.
3. **Ý nghĩa kinh tế so với thống kê.** Tương quan nhỏ nhưng có ý nghĩa thống kê (Lopez-Lira & Tang, 2023) và Sharpe cao trong backtest đều cần kiểm định ngoài mẫu và tính chi phí giao dịch.
4. **Cảm xúc không bằng tác động lên giá.** Ba bài toán cần tách: hiểu cảm xúc văn bản; đánh giá tin tốt hay xấu cho doanh nghiệp; dự đoán phản ứng thị trường.
5. **Tính chủ quan của nhãn.** Mức đồng thuận tích cực–trung lập chỉ 75,2% trong PhraseBank (Mục 5.3).
6. **Diễn giải.** Từ điển minh bạch nhưng thô, mô hình sâu chính xác hơn nhưng khó giải thích.
7. **Độ tin cậy của LLM khi gán nhãn.** Vamvourellis & Mehta (2025) cho thấy cấu hình prompt ảnh hưởng độ khớp nhãn người; tính ổn định giữa các lần chạy và ảo giác chưa được đo trực tiếp trong tập đã xem.

---

## 8. FSA tiếng Việt

### 8.1. Bức tranh nghiên cứu

Tôi kiểm tra được năm công trình (thư mục và tóm tắt/mô tả từ trang gốc) và gặp thêm một chương sách chưa xác minh được. Tất cả thuộc giai đoạn 2021–2026 và đều dùng tin tức hoặc tiêu đề báo, không có diễn đàn hay mạng xã hội.

| Công trình | Nguồn dữ liệu | Quy mô | Nhãn | Bài toán, mô hình | Kết quả (theo tác giả) |
|---|---|---|---|---|---|
| Tung và cs. (2021), CEUR Vol-3026 | Tiêu đề CafeF | 1.000 tiêu đề | 3 lớp: 187 tiêu cực, 248 không tác động, 565 tích cực; "có sự giúp đỡ của chuyên gia" | Phân loại, PhoBERT; thay thực thể bằng token giữ chỗ | Accuracy tới 93% (không có chỉ số từng lớp) |
| Vu và cs. (2023), IJFS 11(3), 101 | Web tài chính–kinh tế | Gần 40.000 bài huấn luyện | Chưa xác minh | Phân loại, PhoBERT; kiểm định phản ứng thị trường | Accuracy trên 81%; không khác biệt đáng kể về giá sau tin, nhưng tin tiêu cực làm đổi phương sai lợi suất |
| Thanh và cs. (2025), VNUHCM JELB 9(1) | VnExpress, VnEconomy, 2024 | 5.126 câu gán nhãn (từ 4.065 bài, 7.130 câu trích) | Nhị phân, chuyên gia trên 20 năm kinh nghiệm, không báo số người gán nhãn hay mức đồng thuận | Ngân hàng câu cảm xúc về khối ngoại; embedding + LR/SVM/RF | SVM accuracy 89% |
| Phong và cs. (2026), VNUHCM JELB 10(1) | Vietnamnet, 2019–2025 | 6.480 bài | Đặc trưng cực tính, chủ quan, điểm tổng hợp (công cụ không nêu rõ) | Dự báo chiều VN-Index; nhiều mô hình học máy | Mô hình tổ hợp tốt nhất; đặc trưng cảm xúc bổ sung giá trị dự báo |
| Việt và cs. (2026), JCSC 42(2) | Tin tức ngân hàng | 12.000 mẫu gán nhãn | Chưa xác minh | Phân loại chủ đề và cảm xúc; PhoBERT, ViT5, BARTPho so với LLaMA-3.1-8B, Vistral-7B | Mô hình tinh chỉnh hơn LLM đa dụng về độ chính xác và hiệu quả tính toán |
| Chương sách Springer về dự báo khó khăn tài chính | Tin tức | – | – | Điểm cảm xúc từ vinai/phobert-base (theo kết quả tìm kiếm) | Chưa xác minh (nội dung truy cập hạn chế) |

Về chi tiết: có một mâu thuẫn nhỏ về Vu và cs. (2023): tóm tắt trên Crossref nói huấn luyện PhoBERT trên gần 40.000 bài, trong khi một tóm tắt thứ cấp nêu 2.738 bài gán nhãn dương/âm; có thể 2.738 là tập có nhãn còn 40.000 là ngữ liệu, nhưng tôi chưa xác minh. Thanh và cs. (2025) cũng không giải thích vì sao 7.130 câu còn 5.126, và tóm tắt nói tám nhóm hành vi nhưng phần phương pháp liệt kê bảy.

Thị trường và lĩnh vực: chứng khoán (VN-Index, VN30, HNX30) và ngân hàng. Bài toán: phần lớn là phân loại hai hoặc ba lớp; hai công trình liên hệ cảm xúc với giá (Vu và cs., Phong và cs.).

### 8.2. Bộ dữ liệu tiếng Việt

| Bộ dữ liệu | Quy mô | Nhãn | Công khai? | Thông tin còn thiếu |
|---|---|---|---|---|
| Tiêu đề CafeF (Tung và cs., 2021) | 1.000 | 3 lớp, mất cân bằng (56,5% tích cực) | Có (GitHub, không nêu giấy phép; không nêu giai đoạn thu thập) | Quy trình gán nhãn, đồng thuận |
| Ngân hàng câu khối ngoại (Thanh và cs., 2025) | 5.126 | Nhị phân | Chưa xác nhận (bài ghi có phụ lục mã) | Số người gán nhãn, đồng thuận, nhãn trung lập |
| Ngữ liệu Vu và cs. (2023) | ~40.000 bài | Chưa xác minh | Chưa xác nhận | Nhãn, công khai |
| Ngữ liệu ngân hàng (Việt và cs., 2026) | 12.000 | Có | Chưa xác nhận | Nguồn, nhãn |

So với Financial PhraseBank (nhãn ba lớp, 16 người gán nhãn, 5–8 lượt gán mỗi câu, báo cáo đồng thuận), chưa bộ tiếng Việt nào tôi tìm thấy công bố quy trình tương đương. Thanh và cs. (2025) dùng nhãn nhị phân nên không có lớp trung lập; ở PhraseBank trung lập chiếm khoảng 60% và là lớp gây bất đồng nhiều nhất, nên kết quả hai bộ không so trực tiếp được. Tôi cũng thấy một mô hình PhoBERT trên Hugging Face được tinh chỉnh bằng nhãn "bạc" do LLM sinh (không phải gán nhãn người) và không có chỉ số đánh giá; đó là thông tin từ model card, không phải nghiên cứu được đánh giá.

### 8.3. Thách thức đặc thù ngôn ngữ

Bằng chứng trực tiếp trong tập đã xem chỉ có hai điểm: PhoBERT đòi hỏi văn bản phải được tách từ trước khi tách token (Nguyen & Nguyen, 2020), và Tung và cs. (2021) dùng VnCoreNLP để tách từ và nhận diện thực thể. Các điểm sau chỉ là câu hỏi cần khảo sát, chưa có bài nào được kiểm tra để khẳng định đó là khó khăn đặc thù tiếng Việt: từ ghép và tách từ ảnh hưởng thế nào đến chất lượng; từ đa nghĩa trong ngữ cảnh tài chính; trộn mã Việt–Anh; viết tắt, mã chứng khoán và tên doanh nghiệp; tiếng lóng diễn đàn; phủ định và mỉa mai.

### 8.4. Các mô hình đã được nghiên cứu

| Mô hình | Bằng chứng |
|---|---|
| PhoBERT | Có (Tung và cs., 2021; Vu và cs., 2023; Việt và cs., 2026) |
| ViT5, BARTPho | Có (Việt và cs., 2026) |
| ML truyền thống | Có: embedding + LR/SVM/RF (Thanh và cs., 2025); mô hình tổ hợp trên đặc trưng cảm xúc (Phong và cs., 2026) |
| LLM đa dụng | Có, làm baseline: LLaMA-3.1-8B, Vistral-7B (Việt và cs., 2026) |
| XLM-R, mBERT | Chưa thấy (PhoBERT được báo cáo vượt XLM-R trên các tác vụ NLP chung, nhưng không phải tài chính) |
| LLM với prompt tài chính (kiểu GPT-4o few-shot) | Chưa thấy trong tiếng Việt |

"Chưa thấy" nghĩa là tôi chưa tìm thấy, không phải chưa ai nghiên cứu. Hướng tiếng Việt thiên về mô hình tinh chỉnh dựa trên PhoBERT, trong khi nghiên cứu quốc tế (Mục 4.4) đã chuyển sang so sánh LLM few-shot với FinBERT.

### 8.5. Ứng dụng và so sánh với FSA toàn cầu

Ứng dụng đã thấy: phản ứng thị trường quanh tin (Vu và cs., 2023), dự báo chiều VN-Index (Phong và cs., 2026), tổng hợp tin ngân hàng (Việt và cs., 2026). Chưa thấy: cảm xúc theo doanh nghiệp hoặc ngành, theo sự kiện, chỉ số tâm lý thị trường, dự báo biến động.

So với toàn cầu, FSA tiếng Việt (i) mới từ khoảng 2021 trở đi; (ii) chỉ dùng văn bản tin tức; (iii) thiếu benchmark chung và đồng thuận gán nhãn công bố; (iv) chưa có bài kiểm tra tổng quát hóa giữa nguồn hay giữa giai đoạn; (v) chưa thấy LLM dùng làm bộ phân loại với prompt tài chính. Nhận định này giới hạn trong các tìm kiếm của bài.

---

## 9. Khoảng trống nghiên cứu và hướng tương lai

| Khoảng trống | Vấn đề chưa giải quyết | Bằng chứng trong bài | Tiềm năng với tiếng Việt |
|---|---|---|---|
| Tổng quát hóa giữa nguồn | Mô hình có chuyển từ tin tức sang diễn đàn, báo cáo không? | Chưa thấy đánh giá trực tiếp (5.1); tiếng Việt chỉ có tin tức (8.1) | Cao |
| Độ bền theo thời gian | Ổn định qua các giai đoạn? | Gián tiếp (7.1, 7.3); kiểm định chéo ngẫu nhiên cho chuỗi giá (5.4) | Cao |
| Cảm xúc theo thực thể và khía cạnh | Cảm xúc hướng đến thực thể nào? | FinLin; FiQA nhắm ABSA; tiếng Việt thay thực thể bằng token giữ chỗ (3.2) | Cao |
| Bất đồng khi gán nhãn | Cảm xúc tài chính có nhất quán? | Có số liệu cho PhraseBank (5.3); tiếng Việt chưa công bố | Cao |
| Cảm xúc văn bản so với tác động thị trường | Có phản ánh tác động kinh tế? | 2.1, 7.4 | Cao |
| LLM few-shot so với mô hình tinh chỉnh | LLM có thay được mô hình tinh chỉnh trên tiếng Việt? | Quốc tế: gần bằng (4.4); tiếng Việt: chỉ có baseline (8.4) | Cao |
| Đánh giá không rò rỉ thời gian | Backtest LLM không nhìn trước | Glasserman & Lin (2023) | Cao |
| Độ tin cậy của LLM | Nhất quán, ít ảo giác? | Rất ít (7.7) | Trung bình |

Hai ưu tiên: (1) xây benchmark tiếng Việt công khai với ba lớp (có trung lập), hướng dẫn gán nhãn, nhiều người gán nhãn và đồng thuận được báo cáo, đủ nhiều nguồn để đo tổng quát hóa; (2) tách rõ nhãn cảm xúc văn bản với nhãn tác động lên giá. Hướng về mô hình nhẹ và đa phương thức đáng làm nhưng cần xuất phát từ các khoảng trống bằng chứng trên.

---

## 10. Kết luận

FSA đã đi từ đếm từ trong từ điển, qua học máy và học sâu, đến Transformer chuyên ngành và LLM. Điểm cốt lõi không nằm ở thứ tự thời gian mà ở việc FSA gồm nhiều bài toán và nhiều loại nhãn, và các mục tiêu đo cảm xúc, phân tích phản ứng thị trường và dự báo cần được tách bạch. Trên benchmark cảm xúc, LLM few-shot hiện gần bằng FinBERT tinh chỉnh chứ chưa vượt rõ; bằng chứng về dự báo thị trường nhìn chung dương nhưng cần kiểm định chặt hơn, đặc biệt về thiên lệch nhìn trước. Với tiếng Việt, đã có các bước đi đầu với PhoBERT và một ngân hàng câu cảm xúc nhị phân, nhưng nhu cầu cấp thiết nhất vẫn là dữ liệu chuẩn mở, quy trình gán nhãn minh bạch và đánh giá có kiểm soát thời gian.

---

## Tài liệu tham khảo (APA 7)

Antweiler, W., & Frank, M. Z. (2004). Is all that talk just noise? The information content of Internet stock message boards. *The Journal of Finance, 59*(3), 1259–1294.

Araci, D. (2019). *FinBERT: Financial sentiment analysis with pre-trained language models*. arXiv:1908.10063. https://arxiv.org/abs/1908.10063

Bollen, J., Mao, H., & Zeng, X. (2011). Twitter mood predicts the stock market. *Journal of Computational Science, 2*(1), 1–8. (Bản tiền ấn: arXiv:1010.3003)

Daudert, T. (2020). *A multi-source entity-level sentiment corpus for the financial domain: The FinLin corpus*. arXiv:2003.04073. https://arxiv.org/abs/2003.04073

Das, S. R., & Chen, M. Y. (2007). Yahoo! for Amazon: Sentiment extraction from small talk on the web. *Management Science, 53*(9), 1375–1388. https://doi.org/10.1287/mnsc.1070.0704

Ding, X., Zhang, Y., Liu, T., & Duan, J. (2015). Deep learning for event-driven stock prediction. *Proceedings of IJCAI 2015*, 2327–2333.

Glasserman, P., & Lin, C. (2023). *Assessing look-ahead bias in stock return predictions generated by GPT sentiment analysis*. arXiv:2309.17322. https://arxiv.org/abs/2309.17322

Kearney, C., & Liu, S. (2014). Textual sentiment in finance: A survey of methods and models. *International Review of Financial Analysis, 33*, 171–185. https://doi.org/10.1016/j.irfa.2014.02.006

Kirtac, K., & Germano, G. (2024). Sentiment trading with large language models. *Finance Research Letters, 62*, 105227. (Bản tiền ấn: arXiv:2412.19245)

Li, X., Chan, S., Zhu, X., Pei, Y., Ma, Z., Liu, X., & Shah, S. (2023). Are ChatGPT and GPT-4 general-purpose solvers for financial text analytics? A study on several typical tasks. *EMNLP 2023 Industry Track*. arXiv:2305.05862. https://arxiv.org/abs/2305.05862

Lopez-Lira, A., & Tang, Y. (2023). *Can ChatGPT forecast stock price movements? Return predictability and large language models*. arXiv:2304.07619. https://arxiv.org/abs/2304.07619

Loughran, T., & McDonald, B. (2011). When is a liability not a liability? Textual analysis, dictionaries, and 10-Ks. *The Journal of Finance, 66*(1), 35–65.

Loughran, T., & McDonald, B. (2016). Textual analysis in accounting and finance: A survey. *Journal of Accounting Research, 54*(4), 1187–1230. https://doi.org/10.1111/1475-679X.12123

Maia, M., Handschuh, S., Freitas, A., Davis, B., McDermott, R., Zarrouk, M., & Balahur, A. (2018). WWW'18 open challenge: Financial opinion mining and question answering. *Companion Proceedings of The Web Conference 2018*, 1941–1942. https://doi.org/10.1145/3184558.3192301

Malo, P., Sinha, A., Korhonen, P., Wallenius, J., & Takala, P. (2014). Good debt or bad debt: Detecting semantic orientations in economic texts. *Journal of the Association for Information Science and Technology, 65*(4), 782–796. https://doi.org/10.1002/asi.23062

Mishev, K., Gjorgjevikj, A., Vodenska, I., Chitkushev, L. T., & Trajanov, D. (2020). Evaluation of sentiment analysis in finance: From lexicons to transformers. *IEEE Access, 8*, 131662–131682. https://doi.org/10.1109/ACCESS.2020.3009626

Nguyen, D. Q., & Nguyen, A. T. (2020). PhoBERT: Pre-trained language models for Vietnamese. *Findings of EMNLP 2020*. arXiv:2003.00744. https://arxiv.org/abs/2003.00744

Nie, Y., Kong, Y., Dong, X., Mulvey, J. M., Poor, H. V., Wen, Q., & Zohren, S. (2024). *A survey of large language models for financial applications: Progress, prospects and challenges*. arXiv:2406.11903. https://arxiv.org/abs/2406.11903

Phong, N. A., Phan Huy, T., & Ngo Phu, T. (2026). Sentiment-driven forecasting of the stock index in Vietnam: A machine learning perspective. *VNUHCM Journal of Economics, Business and Law, 10*(1), 6410–6424. https://doi.org/10.32508/stdjelm.v10i1.1687

Shen, Y., & Zhang, P. K. (2024). *Financial sentiment analysis on news and reports using large language models and FinBERT*. arXiv:2410.01987. https://arxiv.org/abs/2410.01987

Tetlock, P. C. (2007). Giving content to investor sentiment: The role of media in the stock market. *The Journal of Finance, 62*(3), 1139–1168. https://doi.org/10.1111/j.1540-6261.2007.01232.x

Thanh, X. P. T., Anh, N. D., & Ha, P. T. (2025). Building a financial sentiment bank on the investment behavior of foreign investors [Ngân hàng câu cảm xúc tài chính về hành vi của khối ngoại]. *VNUHCM Journal of Economics, Business and Law, 9*(1), 6103–6112. https://doi.org/10.32508/stdjelm.v9i1.1548 *(thứ tự tên theo trang tạp chí: Xuan Pham Thi Thanh, Nhu Dang Anh, Phuc Tu Ha; cần chuẩn hóa họ–tên khi nộp)*

Tung, N. S., Long, N. N., Tran, T., Thao, N. T., Phuong, D. T. T., & Nguyen, T. (2021). Stock article title sentiment-based classification using PhoBERT. *Proceedings of the 2nd International Conference on Human-centered Artificial Intelligence (Computing4Human 2021)*, CEUR Workshop Proceedings, Vol. 3026, 225–233. https://ceur-ws.org/Vol-3026/paper25.pdf

Vamvourellis, D., & Mehta, D. (2025). *Reasoning or overthinking: Evaluating large language models on financial sentiment analysis*. arXiv:2506.04574. https://arxiv.org/abs/2506.04574

Việt, A. P., Minh, H. P., Quoc, H. N., Duc, A. N., & Hai, L. T. (2026). Fine-tuned language models for intelligent aggregation systems in the banking sector. *Journal of Computer Science and Cybernetics, 42*(2), 167–181. https://vjs.ac.vn/jcc/article/view/22428 *(họ–tên theo trang tạp chí, cần chuẩn hóa)*

Vu, L. T., Pham, D. N., Kieu, H. T., & Pham, T. T. T. (2023). Sentiments extracted from news and stock market reactions in Vietnam. *International Journal of Financial Studies, 11*(3), 101. https://doi.org/10.3390/ijfs11030101

Wu, S., Irsoy, O., Lu, S., Dabravolski, V., Dredze, M., Gehrmann, S., Kambadur, P., Rosenberg, D., & Mann, G. (2023). *BloombergGPT: A large language model for finance*. arXiv:2303.17564. https://arxiv.org/abs/2303.17564

Xie, Q., Han, W., Zhang, X., Lai, Y., Peng, M., Lopez-Lira, A., & Huang, J. (2023). *PIXIU: A large language model, instruction data and evaluation benchmark for finance*. arXiv:2306.05443. https://arxiv.org/abs/2306.05443

Xie, Q., Han, W., Chen, Z., Xiang, R., Zhang, X., He, Y., et al. (2024). *FinBen: A holistic financial benchmark for large language models*. arXiv:2402.12659. https://arxiv.org/abs/2402.12659

Xing, F. Z., Cambria, E., & Welsch, R. E. (2018). Natural language based financial forecasting: A survey. *Artificial Intelligence Review, 50*(1), 49–73. https://doi.org/10.1007/s10462-017-9588-9

Yang, H., Liu, X.-Y., & Wang, C. D. (2023). *FinGPT: Open-source financial large language models*. arXiv:2306.06031. https://arxiv.org/abs/2306.06031

Yang, Y., Uy, M. C. S., & Huang, A. (2020). *FinBERT: A pretrained language model for financial communications*. arXiv:2006.08097. https://arxiv.org/abs/2006.08097

Zhang, B., Yang, H., & Liu, X.-Y. (2023). *Instruct-FinGPT: Financial sentiment analysis by instruction tuning of general-purpose large language models*. arXiv:2306.12659. https://arxiv.org/abs/2306.12659

---

## Ghi chú về độ tin cậy và việc còn lại

- Mức xác minh từng công trình được nêu ở Mục 1.4. Các con số là số do tác giả công bố; thông tin Nhóm A được trích từ trang bài hoặc bản HTML qua công cụ đọc trang chứ không phải tôi đọc trực tiếp PDF.
- Mục 3 (taxonomy) là cách đọc của tôi; hàng "lập trường" và "báo cáo phân tích/họp báo" ghi nhận chỗ chưa có công trình trong tập đã xem, không phải kết luận rằng chưa có nghiên cứu.
- Chương sách Springer về dự báo khó khăn tài chính ở Mục 8.1 chưa có tác giả/tiêu đề đầy đủ nên không đưa vào danh mục tham khảo.
- Vẫn chưa làm: truy vấn có hệ thống trên Scopus/WoS/IEEE/ACM; sơ đồ sàng lọc; khảo sát đầy đủ LLM 2025–2026; đọc trực tiếp toàn văn PDF các bài Nhóm B; xác minh mâu thuẫn 40.000 so với 2.738 bài của Vu và cs. (2023).
