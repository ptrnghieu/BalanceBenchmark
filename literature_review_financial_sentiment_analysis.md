# Tổng quan tài liệu về Phân tích cảm xúc trong tài chính (Financial Sentiment Analysis): bài toán, phương pháp, dữ liệu và bối cảnh tiếng Việt

## Tóm tắt

Phân tích cảm xúc tài chính (Financial Sentiment Analysis – FSA) thường được hiểu là phân loại văn bản tài chính thành tích cực, tiêu cực hoặc trung lập. Bài tổng quan này lập luận rằng cách hiểu đó quá hẹp. FSA có thể mô tả bằng năm trục độc lập (đơn vị phân tích, đối tượng, loại đầu ra, loại thông tin, mục tiêu sử dụng) và nằm trong một chuỗi bốn tầng: trích xuất cảm xúc (T1), tổng hợp (T2), phân tích phản ứng thị trường (T3), dự báo và giao dịch (T4). Chỉ T1 là phân loại cảm xúc theo nghĩa hẹp; các tầng sau là ứng dụng của nó. Bằng chứng gần đây cho thấy bằng chứng không bắc cầu giữa các tầng: độ chính xác ngôn ngữ cao chưa kéo theo khả năng dự báo lợi suất. Bài khảo sát giai đoạn 2000 đến 10/2026 theo cấu trúc: nền tảng khái niệm, taxonomy, tiến hóa phương pháp (đến LLM), dữ liệu–gán nhãn–đánh giá, ứng dụng, thách thức, rồi đi riêng vào FSA tiếng Việt, nơi chỉ có bốn công trình xử lý văn bản tiếng Việt được kiểm tra, mẫu nhỏ, chưa có benchmark công khai được chuẩn hóa, và chưa so sánh với LLM prompt tài chính.

**Từ khóa:** phân tích cảm xúc, tài chính, taxonomy, FinBERT, mô hình ngôn ngữ lớn, tiếng Việt, PhoBERT

---

## 1. Giới thiệu

### 1.1. Động lực và luận điểm trung tâm

Thị trường tài chính phản ứng với thông tin, và phần lớn thông tin đó ở dạng văn bản. Từ những năm 2000, một nhánh nghiên cứu chuyển văn bản thành chỉ báo định lượng về cảm xúc để kiểm tra mối liên hệ với lợi suất, biến động và khối lượng giao dịch. Luận điểm trung tâm của bài:

> FSA không chỉ là phân loại positive/negative/neutral. Nó gồm nhiều bài toán, nhiều loại nhãn, nhiều nguồn dữ liệu và nhiều mục tiêu downstream, và cần được tách thành bốn tầng: trích xuất cảm xúc (T1), tổng hợp (T2), phân tích phản ứng thị trường (T3), dự báo và giao dịch (T4). Một mô hình tốt ở T1 chưa chắc hữu ích ở T4, và khoảng cách này càng rõ ở ngôn ngữ ít tài nguyên như tiếng Việt.

Ký hiệu T1–T4 (Mục 3.4) được dùng xuyên suốt bài. Các công trình dự báo giá từ văn bản (Ding và cs., 2015; Bollen và cs., 2011; Lopez-Lira & Tang, 2023; Kirtac & Germano, 2024) được giữ lại như ứng dụng của FSA ở T4, không được đánh đồng với bài toán phân loại cảm xúc.

### 1.2. Câu hỏi nghiên cứu

| RQ | Câu hỏi | Mục |
|---|---|---|
| RQ1 | FSA có thể được phân loại thế nào theo bài toán và tầng ứng dụng, và phương pháp, mô hình đã phát triển ra sao? | 3, 4 |
| RQ2 | Những tập dữ liệu, cách gán nhãn và giao thức đánh giá nào được dùng ở từng tầng? | 5 |
| RQ3 | Cảm xúc tài chính được tổng hợp, phân tích phản ứng thị trường và dùng để dự báo ra sao (T2–T4)? | 6 |
| RQ4 | Thách thức và khoảng trống nghiên cứu chính là gì? | 7, 9 |
| RQ5 | FSA tiếng Việt đang ở mức nào so với nghiên cứu toàn cầu? | 8 |

### 1.3. Các khảo sát liên quan

Kearney và Liu (2014) khảo sát cảm xúc văn bản trong tài chính; Loughran và McDonald (2016) khảo sát phân tích văn bản trong kế toán–tài chính; Xing và cs. (2018) khảo sát dự báo tài chính dựa trên ngôn ngữ tự nhiên; Nie và cs. (2024) khảo sát LLM cho ứng dụng tài chính; Kirtac và Germano (2025) bàn riêng câu hỏi "cảm xúc tài chính là gì" và vai trò của LLM trong ước lượng nó. Hai khảo sát ngắn về LLM zero/few-shot cho FSA (Gao, 2026) và về BERT, FinBERT và LLM (Mahendran và cs., 2025) cũng có trong kết quả tìm kiếm nhưng tôi chỉ có tiêu đề và siêu dữ liệu. Bài này khác ở chỗ tổ chức theo năm trục phân loại và bốn tầng (trích xuất, tổng hợp, phản ứng thị trường, dự báo), và dành riêng một phần cho tiếng Việt.

### 1.4. Phương pháp chọn tài liệu, mức xác minh và giới hạn

**Ba lộ trình tìm kiếm.** Tôi không có quyền truy cập Scopus, Web of Science, IEEE Xplore hay ACM DL, nên bài **không phải tổng quan hệ thống kiểu PRISMA đầy đủ**. Quy trình gồm:
1. **Truy vấn có mã lệnh, tái lập được** trên hai API mở: arXiv và Crossref (giai đoạn 01/2000–10/2026).
2. **Tìm kiếm web có mục tiêu** theo tên công trình kinh điển và theo chủ đề (nhất là tiếng Việt).
3. **Lần theo trích dẫn** từ các khảo sát (Kearney & Liu, 2014; Loughran & McDonald, 2016; Xing và cs., 2018; Nie và cs., 2024).

**Truy vấn của lộ trình 1.**

| Mã | arXiv (trường tiêu đề/tóm tắt) | Crossref (query.bibliographic, 200 kết quả đầu theo độ liên quan) |
|---|---|---|
| Q1 | "financial sentiment" | financial sentiment analysis |
| Q2 | sentiment AND (financial news OR stock market OR stock price OR stock return) | news sentiment stock market |
| Q3 | (large language model OR LLM OR ChatGPT OR GPT) AND sentiment AND (financial OR stock) | large language models financial sentiment |
| Q4 | Vietnamese AND (sentiment OR opinion) AND (financial OR stock OR banking) | Vietnamese financial news sentiment stock |

**Sơ đồ sàng lọc của lộ trình 1.**

```
Bản ghi từ API:                      1.360   (arXiv: 560; Crossref: 800)
  - trùng theo tiêu đề chuẩn hóa:     −257
Bản ghi duy nhất:                    1.103
  - sàng 1 (từ khóa cảm xúc + tài chính trong tiêu đề/tóm tắt):  939
  - sàng 2 (tiêu đề phải có từ khóa cảm xúc; Crossref phải có từ khóa tài chính):  697  (arXiv 189; Crossref 508)
  - nhóm ưu tiên 2024–2026 (khảo sát, benchmark, LLM, ...) đọc tiêu đề thủ công:  130
  - công trình mới được đưa vào bài sau khi đọc tóm tắt:  xem Mục 4.4–4.5 và Phụ lục B
```

Số "kết quả tổng cộng" mà Crossref trả về (hàng triệu) không có ý nghĩa vì truy vấn khớp lỏng; chỉ 200 bản ghi đầu mỗi truy vấn được dùng. Việc sàng 1 và sàng 2 là lọc từ khóa tự động, chưa phải đánh giá thủ công từng bản ghi; chỉ nhóm ưu tiên 2024–2026 được tôi đọc tiêu đề.

**Kiểm tra độ phủ.** Trong 33 công trình chính của bài, lộ trình 1 chỉ bắt được **14**. Nó bỏ lỡ nhiều bài kinh điển (Loughran & McDonald, 2011; Antweiler & Frank, 2004; Bollen và cs., 2011), và **không bắt được công trình nào** trong sáu công trình tiếng Việt (gồm PhoBERT) tôi tìm bằng lộ trình 2. Nguyên nhân chính: tiêu đề không chứa từ khóa, và các tạp chí hoặc hội thảo khu vực (CEUR, VNUHCM, JCC) không nằm trong top 200 của Crossref. Vì vậy các nhận định "chưa có công trình" trong bài chỉ đúng với tập tài liệu đã xem, và phần tiếng Việt chắc chắn chưa đầy đủ.

**Tiêu chí (áp dụng không chính thức).** Đưa vào: có thể xác minh thư mục; liên quan trực tiếp đến cảm xúc/văn bản tài chính hoặc là chuẩn tham chiếu của lĩnh vực. Loại: trang tóm tắt, blog, bài không xác minh được tác giả; nghiên cứu về cảm xúc nhà đầu tư không dùng văn bản (ví dụ hai bài về tâm lý nhà đầu tư thị trường Việt Nam trong kết quả Crossref). **Trường trích xuất cho mỗi công trình:** dữ liệu, bài toán (theo năm trục), phương pháp, nhãn, thiết lập đánh giá, tầng (T1–T4), kết quả chính.

**Mức xác minh.**
- *Mức 1 – đọc có mục tiêu toàn văn:* tôi tải PDF, trích văn bản và đọc các đoạn liên quan (không đọc từ đầu đến cuối): Bollen và cs. (2011), Lopez-Lira & Tang (2023, bản 10/2025), Glasserman & Lin (2023), Kirtac & Germano (2024), Mishev và cs. (2020), Loughran & McDonald (2011), Tetlock (2007), Antweiler & Frank (2004, bản working paper), Maia và cs. (2018), Malo và cs. (2014), Araci (2019), Yang và cs. (2020), Nguyen S. T. và cs. (2021), Nguyen P. A. và cs. (2026), và một phần Shen & Zhang (2024) và Vamvourellis & Mehta (2025).
- *Mức 2 – trang bài, tóm tắt đầy đủ hoặc bản HTML qua công cụ đọc trang hoặc API:* Nie và cs. (2024), Wu và cs. (2023), Xie và cs. (2023, 2024), Li và cs. (2023), Zhang và cs. (2023), Vu và cs. (2023), Thanh và cs. (2025), Việt và cs. (2026), Nguyen & Nguyen (2020), và các công trình 2024–2026 ở Mục 4.4.
- *Mức 3 – chỉ tóm tắt hoặc siêu dữ liệu:* Das & Chen (2007), Ding và cs. (2015), Kearney & Liu (2014), Loughran & McDonald (2016), Xing và cs. (2018), Yang và cs. (2023), Daudert (2020), và các mục trong Phụ lục B.

Số liệu là số do tác giả công bố. Chưa kiểm tra lại kết quả bằng cách chạy mã.

---

## 2. Nền tảng khái niệm

### 2.1. Ba khái niệm cần tách biệt

| Khái niệm | Câu hỏi | Ví dụ |
|---|---|---|
| **Cảm xúc văn bản** | Văn bản thể hiện sắc thái gì? | "Doanh thu giảm mạnh" mang sắc thái tiêu cực |
| **Tâm lý nhà đầu tư** | Nhà đầu tư lạc quan hay bi quan? | Chỉ số tâm lý tổng hợp từ nhiều nguồn |
| **Tác động kỳ vọng lên giá** | Thông tin tốt hay xấu cho giá? | Tin cắt giảm chi phí có thể tăng giá dù sắc thái trung tính |

Ba khái niệm không thể mặc định thay thế cho nhau. Phân biệt này thể hiện ngay trong các bộ nhãn: người gán nhãn Financial PhraseBank được yêu cầu đánh giá theo cách thông tin có thể ảnh hưởng đến giá cổ phiếu của công ty được nhắc đến (Mishev và cs., 2020, mô tả; Malo và cs., 2014, nói là theo góc nhìn nhà đầu tư), Lopez-Lira & Tang (2023) yêu cầu mô hình đánh giá tiêu đề đối với giá cổ phiếu, và Kirtac & Germano (2024) gán nhãn "cảm xúc" bằng dấu của lợi suất vượt trội ba ngày. Kirtac và Germano (2025) lập luận riêng rằng khái niệm cảm xúc tài chính cần được định nghĩa rõ trước khi đo.

### 2.2. Cơ sở lý thuyết và bằng chứng ban đầu

Tetlock (2007) phân tích cột "Abreast of the Market" trên Wall Street Journal trong 16 năm (1984–1999) bằng phân tích thành phần chính. Mức bi quan cao của truyền thông dự báo áp lực giảm giá rồi giá hồi về mức cơ bản, còn mức bi quan cực đoan dự báo khối lượng giao dịch lớn; tác giả diễn giải kết quả phù hợp với mô hình có nhà giao dịch nhiễu và thanh khoản.

Antweiler và Frank (2004; bản working paper) nghiên cứu bảng tin Yahoo! Finance và Raging Bull cho 45 công ty (thành phần Dow Jones Industrial Average và Dow Jones Internet Commerce Index), với hơn 1,5 triệu thông điệp. Số lượng thông điệp dự báo khối lượng giao dịch và biến động tăng ở tần suất ngày, khối lượng giao dịch tăng cùng mức "bullish" của thông điệp; họ cũng ghi nhận lợi suất gần như không tương quan với số thông điệp hay mức bullish. Điều này cho thấy ngay từ đầu cảm xúc có thể liên hệ với hoạt động giao dịch mà không dự báo lợi suất.

Kearney và Liu (2014) tổng hợp rằng cảm xúc văn bản liên hệ với hành vi ở cấp cá nhân, doanh nghiệp và thị trường, đồng thời chỉ ra các điểm còn tranh luận.

---

## 3. Taxonomy các bài toán FSA

### 3.1. Vì sao cần nhiều trục phân loại

Một bảng liệt kê "các bài toán FSA" thường trộn những khái niệm khác cấp: phân loại câu (đơn vị phân tích), ABSA (cấu trúc mục tiêu), theo thực thể (đối tượng), chỉ số tổng hợp (cấp tổng hợp), theo sự kiện (cách tổ chức thông tin). Các nhóm này **không loại trừ nhau**: một hệ thống có thể vừa phân tích cảm xúc theo thực thể vừa phân loại theo khía cạnh. Vì vậy bài dùng hai công cụ: (i) năm trục độc lập để mô tả *một công trình làm gì* (Mục 3.2–3.3), và (ii) mô hình bốn tầng để phân biệt *cảm xúc được trích xuất* với *cảm xúc được dùng* (Mục 3.4).

### 3.2. Năm trục độc lập

| Trục | Câu hỏi | Các nhóm |
|---|---|---|
| 1. Đơn vị phân tích | Văn bản được xử lý ở cấp nào? | Từ; câu/cụm từ; thông điệp hoặc tiêu đề; tài liệu; chuỗi thời gian (sau khi gộp) |
| 2. Đối tượng phân tích | Cảm xúc về cái gì? | Cấp tài liệu; cấp thực thể/mục tiêu; cấp khía cạnh (có thể kết hợp thực thể × khía cạnh) |
| 3. Loại đầu ra | Mô hình trả về gì? | Phân loại; chấm điểm/hồi quy; xếp hạng |
| 4. Loại thông tin | Đại lượng nào được đo? | Cực tính cảm xúc (sentiment); cảm xúc chi tiết (emotion/mood); lập trường (stance); tác động kỳ vọng lên giá |
| 5. Mục tiêu sử dụng | Kết quả dùng để làm gì? | Đo lường; phân tích thị trường; dự báo/giao dịch |

Trục 4 chính là ba khái niệm ở Mục 2.1 (cảm xúc văn bản, tâm lý nhà đầu tư, tác động kỳ vọng lên giá), bổ sung hai nhóm chi tiết hơn (emotion, stance).

### 3.3. Định vị các công trình lên các trục

| Công trình | 1. Đơn vị | 2. Đối tượng | 3. Đầu ra | 4. Loại thông tin | 5. Mục tiêu |
|---|---|---|---|---|---|
| Loughran & McDonald (2011) | Từ → tài liệu (10-K) | Tài liệu | Điểm (tỷ lệ từ) | Cực tính (giọng điệu) | Đo lường; phân tích thị trường |
| Tetlock (2007) | Từ → chuỗi thời gian (cột báo hằng ngày) | Thị trường | Điểm (thành phần chính) | Cực tính (bi quan) | Phân tích thị trường |
| Das & Chen (2007) | Thông điệp → chuỗi gộp theo thời gian và cổ phiếu | Tài liệu | Phân loại | Cực tính | Đo lường |
| Malo và cs. (2014) | Câu | Tài liệu (câu) | Phân loại 3 lớp | Cực tính, nhãn theo góc nhìn nhà đầu tư | Đo lường |
| FiQA Task 1 (Maia và cs., 2018) | Tiêu đề, vi blog | Thực thể × khía cạnh (khía cạnh từ danh sách định sẵn) | Phân loại khía cạnh + điểm [−1, 1] | Cực tính | Đo lường |
| FiQA Task 2 (Maia và cs., 2018) | Bài đăng StackExchange | Câu hỏi quan điểm | Xếp hạng câu trả lời (nDCG@10, MRR) | Quan điểm | Đo lường (QA) |
| FinLin (Daudert, 2020) | Tài liệu | Thực thể | Điểm cảm xúc và điểm liên quan | Cực tính | Đo lường |
| Bollen và cs. (2011) | Tweet → chuỗi thời gian ngày | Thị trường chung | Điểm đa chiều | Cảm xúc chi tiết (mood) | Dự báo |
| Ding và cs. (2015) | Sự kiện trích từ tin | Cổ phiếu/chỉ số | Phân loại chiều giá | Tác động kỳ vọng lên giá | Dự báo |
| Lopez-Lira & Tang (2023) | Tiêu đề | Thực thể (công ty) | Phân loại 3 lớp → điểm | Tác động kỳ vọng lên giá | Dự báo/giao dịch |
| Kirtac & Germano (2024) | Bài báo | Doanh nghiệp (tin ghép với 6.214 công ty) | Phân loại nhị phân + điểm | Tác động kỳ vọng lên giá (nhãn từ dấu lợi suất vượt trội 3 ngày) | Giao dịch |
| Nguyen S. T. và cs. (2021) | Tiêu đề | Tài liệu (thực thể bị che) | Phân loại 3 lớp | Tác động ("ảnh hưởng") | Đo lường |
| Vu và cs. (2023) | Bài báo | Tài liệu | Phân loại (số lớp chưa xác minh) | Cực tính | Đo lường; phân tích thị trường |
| Nguyen P. A. và cs. (2026) | Bài báo (tiêu đề, trích đoạn, nội dung) → ngày; **tiếng Anh** | Thị trường (VN-Index) | Điểm từ điển (polarity, subjectivity, VADER) → phân loại chiều | Cực tính, mức chủ quan | Dự báo |

Một số nhận xét:
- **Không loại trừ nhau.** FiQA Task 1 vừa ở cấp thực thể vừa ở cấp khía cạnh, và vừa phân loại khía cạnh vừa chấm điểm; Kirtac & Germano (2024) có đầu ra phân loại nhưng mục tiêu là giao dịch.
- **Trục 4 là chỗ dễ lẫn nhất.** Nhãn "tác động kỳ vọng lên giá" xuất hiện ở các công trình dự báo (Ding và cs.; Lopez-Lira & Tang; Kirtac & Germano) và bộ CafeF (Nguyen S. T. và cs.); Financial PhraseBank nằm ở giữa vì yêu cầu người gán nhãn dùng góc nhìn nhà đầu tư.
- **Chưa thấy trong tập đã xem:** công trình về lập trường (stance) trên dữ liệu tài chính. Xếp hạng chỉ thấy ở FiQA Task 2 (QA), không phải cho cảm xúc. Đây là chỗ thiếu bằng chứng của bài, không phải kết luận rằng chưa có nghiên cứu.
- Việc định vị là cách đọc của tôi; chi tiết các hàng có đọc toàn văn nằm ở Mức 1 (Mục 1.4), các hàng còn lại dựa trên tóm tắt.

### 3.4. Mô hình bốn tầng: từ trích xuất đến giao dịch

Để phân biệt nhất quán FSA với dự báo tài chính từ văn bản, bài dùng bốn tầng ký hiệu T1–T4 xuyên suốt:

| Tầng | Câu hỏi | Đầu ra | Cách đánh giá hợp lệ | Công trình ví dụ |
|---|---|---|---|---|
| **T1. Trích xuất cảm xúc** | Văn bản này thể hiện gì? | Nhãn/điểm cho câu, tiêu đề, tài liệu, thực thể | So với nhãn người: Accuracy, F1, MCC, mức đồng thuận | Malo và cs. (2014); Araci (2019); Yang và cs. (2020); Mishev và cs. (2020); Nguyen S. T. và cs. (2021); Thanh và cs. (2025); Vamvourellis & Mehta (2025) |
| **T2. Tổng hợp cảm xúc** | Gộp nhiều văn bản thành chỉ số cấp doanh nghiệp, ngành, thị trường thế nào? | Chỉ số theo thời gian | Độ hợp lệ và ổn định của chỉ số; liên hệ với biến độc lập | Loughran & McDonald (2011); Tetlock (2007); Das & Chen (2007); đặc trưng của Nguyen P. A. và cs. (2026) |
| **T3. Phân tích phản ứng thị trường** | Thị trường phản ứng thế nào với cảm xúc/thông tin? | Quan hệ cảm xúc–lợi suất, biến động, khối lượng | Nghiên cứu sự kiện, kiểm định thống kê; không hàm ý dự báo | Tetlock (2007); Antweiler & Frank (2004); Vu và cs. (2023) |
| **T4. Dự báo và giao dịch có dùng cảm xúc** | Tín hiệu cảm xúc có giúp dự báo/giao dịch ngoài mẫu? | Dự báo giá, chiều, danh mục | Kiểm định ngoài mẫu, chia theo thời gian, chi phí giao dịch | Bollen và cs. (2011); Ding và cs. (2015); Lopez-Lira & Tang (2023); Kirtac & Germano (2024); Nguyen P. A. và cs. (2026) |

Bốn quy tắc nhất quán áp dụng cho cả bài:
1. **Chỉ T1 là FSA theo nghĩa hẹp**, đánh giá bằng nhãn người. T2–T4 là các ứng dụng của FSA; chúng được giữ lại vì cho thấy cảm xúc được dùng để làm gì, nhưng không được đánh đồng với bài toán phân loại cảm xúc.
2. **Bằng chứng không bắc cầu giữa các tầng.** Hai nghiên cứu 2026 kiểm tra trực tiếp điều này: Luo (2026) thấy các mô hình có accuracy 0,884 (Mistral-7B) trên benchmark ba lớp nhưng không mô hình nào có tín hiệu lợi suất còn ý nghĩa sau khi hiệu chỉnh trên 28 cặp mô hình–kỳ hạn; Bisharat & Hean (2026) thấy LLM đa dụng có độ chính xác phân loại ngang các Transformer chuyên ngành tài chính, nhưng không mô hình nào có quan hệ có ý nghĩa với lợi suất ngày kế tiếp, dù một số liên hệ có ý nghĩa với bất ngờ lợi nhuận. Ngược lại, kết quả T4 tốt cũng không chứng minh T1 tốt: nhãn có thể sai nhưng vẫn tương quan với giá.
3. **Công trình trải nhiều tầng thì báo cáo riêng từng tầng.** Ví dụ Kirtac & Germano (2024) đo "độ chính xác" bằng khả năng dự đoán dấu lợi suất (Mục 4.4a), nên đó đã là một thước đo thuộc T4, không phải T1.
4. **Hệ thống dự báo có bước trích xuất nội bộ vẫn xếp ở T4.** Ding và cs. (2015) trích sự kiện từ tin rồi dự báo giá; Lopez-Lira & Tang (2023) nhờ mô hình đánh giá tiêu đề theo tác động lên giá rồi kiểm tra lợi suất. Cả hai nên gọi là dự báo tài chính dựa trên văn bản có thành phần trích xuất, không phải bộ phân loại cảm xúc thuần túy.

Với ký hiệu này, Bollen và cs. (2011) là T2 (chỉ số tâm trạng theo ngày) cộng T4 (dự đoán chiều DJIA), còn Tetlock (2007) là T2 cộng T3.

### 3.5. Vì sao cần phân biệt: ví dụ

Xét câu minh họa (do tôi đặt): *"Công ty A báo lãi kỷ lục, trong khi công ty B thua lỗ nặng."* Phân loại cả câu (trục 2: cấp tài liệu) có thể trả về trung lập; phân tích theo thực thể cho A tích cực, B tiêu cực. Tương tự, *"Doanh thu giảm nhưng biên lợi nhuận cải thiện đáng kể"* có nhãn phụ thuộc vào khía cạnh được chú ý. FiQA Task 1 được thiết kế đúng cho dạng này, nhưng kết quả thi cho thấy đây là bài toán khó: ở tập tiêu đề, độ chính xác phân loại khía cạnh tốt nhất chỉ 0,2688 và R² của dự đoán điểm cảm xúc tốt nhất là 0,4579 (Maia và cs., 2018).

Một bằng chứng trực tiếp từ tiếng Việt: Nguyen S. T. và cs. (2021) thay tên riêng, địa danh, tên tổ chức và mã chứng khoán bằng token giữ chỗ trước khi phân loại tiêu đề. Cách này tránh học thuộc tên công ty nhưng làm mất thông tin về thực thể; nó phù hợp với phân loại cấp tài liệu và không phù hợp với bài toán cấp thực thể. Tin tài chính tiếng Việt thường nhắc nhiều doanh nghiệp và ngành trong cùng bài, nên bài toán cấp thực thể và khía cạnh là hướng đáng quan tâm; đây là suy luận của tôi.

---

## 4. Tiến hóa phương pháp

### 4.1. Từ điển

Loughran và McDonald (2011) phân tích 50.115 hồ sơ 10-K giai đoạn 1994–2008 và thấy gần ba phần tư số từ mà từ điển Harvard xếp là tiêu cực không mang nghĩa tiêu cực trong báo cáo tài chính (ví dụ *tax, cost, capital, board, liability*). Họ xây từ điển tài chính riêng gồm danh sách từ tiêu cực (Fin-Neg) và năm danh mục khác (tích cực, bất định, tranh chấp pháp lý, modal mạnh, modal yếu), và cho thấy thước đo dựa trên đó liên hệ rõ hơn với lợi suất quanh ngày nộp báo cáo, khối lượng, biến động, gian lận và điểm yếu trọng yếu. Ưu điểm: minh bạch, rẻ, dễ tái lập. Nhược điểm: bỏ qua ngữ cảnh. Malo và cs. (2014) nhấn mạnh cảm xúc của câu có thể khác cảm xúc của từng từ.

### 4.2. Học máy truyền thống và học sâu

Das và Chen (2007) kết hợp nhiều bộ phân loại bằng bỏ phiếu cho bài đăng bảng tin; họ báo cáo độ chính xác tương đương bộ phân loại Bayes nhưng ít dương tính giả hơn. Ding và cs. (2015) là một hệ thống dự báo giá (T4) có bước trích xuất sự kiện bên trong, không phải bộ phân loại cảm xúc: họ trích sự kiện từ tin tức, dùng mạng tensor nơ-ron và CNN sâu, báo cáo cải thiện khoảng 6% so với baseline trên tin Reuters và Bloomberg. Xing và cs. (2018) tổng quan giai đoạn trước Transformer.

### 4.3. Mô hình tiền huấn luyện

Araci (2019) tiền huấn luyện tiếp BERT trên TRC2-financial (tập con của Reuters TRC2: 46.143 tài liệu, hơn 29 triệu từ), rồi tinh chỉnh. Trên Financial PhraseBank (4.845 câu), FinBERT đạt accuracy 0,86 và F1 0,84 (0,97 và 0,95 trên tập đồng thuận 100%), so với ULMFit 0,83/0,79. Trên FiQA (1.174 tiêu đề và tweet, điểm liên tục), MSE 0,07 và R² 0,55; tác giả lưu ý FinBERT đánh giá bằng kiểm định chéo 10 lần, các baseline dùng tập kiểm thử chính thức, nên so sánh không trực tiếp.

Yang và cs. (2020) tiền huấn luyện một BERT khác (cũng tên FinBERT) từ đầu trên khoảng 4,9 tỷ token: báo cáo doanh nghiệp 10-K/10-Q (2,5 tỷ), bản ghi họp báo kết quả (1,3 tỷ) và báo cáo phân tích (1,1 tỷ). Mô hình được đánh giá trên Financial PhraseBank (4.840 câu), AnalystTone (10.000 câu) và FiQA (1.111 câu, chuyển thành nhị phân). Accuracy tốt nhất của FinBERT là 0,872, 0,887 và 0,844, so với BERT uncased 0,835, 0,850 và 0,730.

Mishev và cs. (2020) chạy hơn một trăm thí nghiệm từ từ điển đến Transformer trên tập kết hợp Financial PhraseBank (4.845 câu) và SemEval-2017 Task 5 (2.510 tiêu đề), dùng hệ số tương quan Matthews (MCC) làm chỉ số chính. BART đạt MCC tốt nhất là 0,895; trong họ BERT, BERT-Large-uncased đạt 0,859. Kết luận chính là biểu diễn theo ngữ cảnh vượt từ điển và bộ mã hóa cố định, còn Transformer rút gọn cho hiệu năng gần bản đầy đủ.

### 4.4. Mô hình ngôn ngữ lớn

Có bốn cách dùng LLM trong tài liệu, cần tách bạch vì không phải công trình LLM nào cũng là FSA theo nghĩa hẹp (T1).

**(a) LLM làm bộ chấm điểm tin tức và tín hiệu giao dịch (T4 có thành phần T1).**

*Lopez-Lira & Tang (2023, bản 10/2025).* Họ cho các mô hình đánh giá tiêu đề trên 4.123 công ty, từ 10/2021 đến 05/2024, tức sau thời điểm cắt dữ liệu huấn luyện của GPT-4 (09/2021) để tránh thiên lệch nhìn trước. Tỷ lệ "hit rate" theo danh mục–ngày cho phản ứng ban đầu (không giao dịch được) khoảng 90%; chiến lược mua–bán dựa trên tin qua đêm cho lợi nhuận trung bình 34 điểm cơ bản mỗi ngày trước chi phí giao dịch. Khả năng khai thác chỉ khả thi với đối tượng có chi phí giao dịch thấp, như nhà tạo lập thị trường. Với chiến lược dựa trên drift ngày kế tiếp, Sharpe thường niên là 2,97 với GPT-4, 1,66 với GPT-3.5, 1,26 với DistilBART-MNLI, và âm với hầu hết mô hình cơ bản. Đáng chú ý nhất, Sharpe của chiến lược dựa trên ChatGPT giảm từ 6,54 (quý 4/2021) xuống 3,68 (2022), 2,33 (2023) và 1,22 (01–05/2024), phù hợp với việc LLM được áp dụng rộng rãi làm giá hiệu quả hơn.

*Kirtac & Germano (2024).* Dữ liệu là 965.375 bài báo tài chính Mỹ (Refinitiv, 01/2010–06/2023) sau khi lọc từ 2.732.845 tin ghép với 6.214 công ty. **Nhãn "cảm xúc" được gán bằng dấu của lợi suất vượt trội cộng dồn ba ngày kể từ ngày đăng tin** (dương → 1, không dương → 0); BERT và OPT được tinh chỉnh trên nhãn này, 20% dữ liệu được chia ngẫu nhiên làm tập kiểm thử. Vì vậy "độ chính xác" 74,4% (OPT), 72,5% (BERT), 72,2% (FinBERT) và 50,1% (từ điển Loughran–McDonald) là độ chính xác dự đoán dấu lợi suất, không phải khớp với nhãn người. Điều này kéo theo hai hệ quả: (i) độ chính xác là thước đo T4, và con số 50,1% của từ điển (ngang ngẫu nhiên) không cho thấy "Transformer hiểu cảm xúc tốt hơn từ điển", vì từ điển không học từ nhãn lợi suất; (ii) phần độ chính xác dùng chia ngẫu nhiên, không chia theo thời gian. Chiến lược mua–bán với chi phí 10 điểm cơ bản mỗi giao dịch cho Sharpe 3,05 với OPT (theo tóm tắt: 2,11 với BERT, 2,07 với FinBERT, 1,23 với từ điển), và đoạn nổi bật là giai đoạn 08/2021–07/2023.

*Lefort và cs. (2024)* hỏi ChatGPT với quy trình hai bước trên các bản tóm tắt thị trường hằng ngày của Bloomberg (2010–2023) và báo cáo tương quan dương có ý nghĩa giữa điểm cảm xúc và lợi suất cổ phiếu ở kỳ hạn ngắn đến trung bình, chuyển sang tương quan âm ở kỳ hạn dài (chỉ có tóm tắt).

**(b) Đánh giá LLM đa dụng so với mô hình tinh chỉnh trên benchmark cảm xúc (T1) và kèm giá trị kinh tế.**
- Li và cs. (2023) đánh giá ChatGPT và GPT-4 trên tám tập dữ liệu thuộc năm nhóm tác vụ tài chính, báo cáo cả điểm mạnh và hạn chế so với mô hình tinh chỉnh.
- Shen & Zhang (2024) kết luận GPT-4o với ví dụ few-shot "có thể ngang một FinBERT được tinh chỉnh tốt" trên tin tức, báo cáo và thông báo doanh nghiệp. Một bản tóm tắt thứ cấp nêu hai con số khác nhau cho GPT-4o zero-shot (0,79 hoặc 0,85) và tôi chưa giải quyết được; không nên dẫn con số cụ thể.
- Vamvourellis & Mehta (2025) so sánh GPT-4o, GPT-4.1 và o3-mini zero-shot với hai FinBERT trên Financial PhraseBank và thấy lập luận không cải thiện kết quả; cấu hình sát nhãn người nhất là GPT-4o không dùng chain-of-thought, và lập luận có thể gây "nghĩ quá mức" ở câu phức tạp hoặc có mức đồng thuận thấp. Một trong hai FinBERT (FinBERT-Prosus) được huấn luyện trực tiếp trên dữ liệu kiểm thử, nên so sánh với nó thiên về mô hình tinh chỉnh.
- Hai nghiên cứu 2026 bổ sung chiều giá trị kinh tế: Luo (2026) kết hợp benchmark ba lớp từ năm tập dữ liệu (QLoRA nâng macro-F1 của Qwen2.5 từ 0,7274 lên 0,8615; Mistral-7B tốt nhất với accuracy 0,8840) với một mẫu Benzinga riêng năm 2019 (10.637 tiêu đề, 13.115 quan sát tiêu đề–cổ phiếu, S&P 100), cho kết quả không có kiểm định nào trong 28 cặp mô hình–kỳ hạn còn ý nghĩa sau hiệu chỉnh Newey–West và FDR (IC thứ hạng trung bình lớn nhất 0,0143, với FinBERT). Bisharat & Hean (2026) so sánh mười hai mô hình theo hai tiêu chí, hợp lệ ngôn ngữ và hợp lệ kinh tế (kết quả ở Mục 3.4).
- Các nghiên cứu khác chỉ có tóm tắt: Wei & Liu (2025) hỏi LLM có phải người học trong ngữ cảnh tốt cho FSA; Rodriguez Inserte và cs. (2024) thích ứng hai mô hình dưới 1,5 tỷ tham số.

Các kết luận này nhất quán ở chỗ LLM few-shot/zero-shot gần bằng mô hình tinh chỉnh chứ chưa vượt rõ trên benchmark cảm xúc, và độ chính xác ngôn ngữ không chuyển thành tín hiệu lợi suất vững chắc.

**(c) LLM chuyên ngành, tinh chỉnh theo hướng dẫn và benchmark.** BloombergGPT (Wu và cs., 2023) có 50 tỷ tham số, huấn luyện trên 363 tỷ token dữ liệu Bloomberg và 345 tỷ token dữ liệu tổng quát. PIXIU (Xie và cs., 2023) gồm FinMA (LLaMA tinh chỉnh theo hướng dẫn), bộ dữ liệu hướng dẫn khoảng 136.000 mẫu và bộ đánh giá FLARE; Zhang và cs. (2023) đề xuất Instruct-FinGPT (LLaMA-7B tinh chỉnh theo hướng dẫn trên dữ liệu cảm xúc tài chính nhỏ); Yang và cs. (2023) đề xuất FinGPT mã nguồn mở với LoRA. Zhao & Welsch (2024) kết hợp tinh chỉnh theo hướng dẫn, RAG và phản hồi thị trường (T1 nối T4), báo cáo cải thiện 1–6% về accuracy và F1 so với các mô hình tiên tiến và danh mục có Sharpe cao hơn 3,61% so với S&P 500 trong thị trường tăng (tóm tắt). FinBen (Xie và cs., 2024) gồm 36 tập dữ liệu thuộc 24 tác vụ; trên 15 LLM, các mô hình làm tốt trích xuất thông tin và phân tích văn bản nhưng yếu ở suy luận nâng cao, sinh văn bản và dự báo. Nie và cs. (2024) khảo sát cả mảng này và nêu các vấn đề mở như thiên lệch nhìn trước, ô nhiễm dữ liệu và khả năng diễn giải.

**(d) LLM, thiên lệch và tính chủ quan của nhãn.** Glasserman và Lin (2023) dùng GPT-3.5 trên tiêu đề tin các công ty S&P 500, so sánh bản gốc với bản ẩn danh. Dữ liệu huấn luyện của ChatGPT đến 09/2021. Trong mẫu, bản ẩn danh cho kết quả giao dịch tốt hơn, nên họ kết luận "hiệu ứng xao nhãng" (kiến thức chung về công ty làm nhiễu phán đoán) lấn át thiên lệch nhìn trước; hiệu ứng mạnh hơn ở công ty lớn; ngoài mẫu, thiên lệch nhìn trước không phải mối lo. Nakagawa và cs. (2024) định lượng "thiên lệch theo công ty" bằng chênh lệch điểm cảm xúc khi tên công ty có hoặc không có trong lời nhắc, trên văn bản tài chính tiếng Nhật. Rahman và cs. (2025) lập luận rằng nhãn Financial PhraseBank phản ánh quan điểm cá nhân của người gán nhãn, nên bổ sung hướng dẫn gán nhãn vào lời nhắc (AIAP) và dùng bộ dữ liệu mới từ subreddit WallStreetBets; họ báo cáo cải thiện tới 9,08 (đơn vị theo tóm tắt).

### 4.5. Phân tích so sánh

| Công trình | Tầng | Dữ liệu | Bài toán | Phương pháp | Kết quả chính (theo tác giả) |
|---|---|---|---|---|---|
| Loughran & McDonald (2011) | T1–T3 | 10-K, 1994–2008 | Giọng điệu văn bản | Từ điển tài chính | Harvard gán sai nhiều từ; từ điển mới liên hệ tốt hơn với kết quả |
| Malo và cs. (2014) | T1 | ~5.000 câu tin | Cảm xúc câu | LPS + từ điển mở rộng | Vượt đếm từ và mô hình chung |
| Araci (2019) | T1 | PhraseBank, FiQA | Phân loại + chấm điểm | BERT + TRC2-financial | Acc 0,86 / F1 0,84 trên PhraseBank |
| Yang và cs. (2020) | T1 | PhraseBank, AnalystTone, FiQA | Phân loại | BERT từ đầu, 4,9 tỷ token | Acc 0,844–0,887, hơn BERT chung |
| Mishev và cs. (2020) | T1 | PhraseBank + SemEval-2017 T5 | Phân loại | Từ điển → Transformer | BART MCC 0,895; ngữ cảnh vượt từ điển |
| Kirtac & Germano (2024) | T4 (nhãn từ lợi suất) | 965.375 tin, 2010–2023 | Dự đoán dấu lợi suất 3 ngày | OPT, BERT, FinBERT, LM | OPT cao nhất: độ chính xác dự đoán dấu lợi suất 74,4%, Sharpe 3,05 |
| Lopez-Lira & Tang (2023) | T4 | 4.123 công ty, 10/2021–05/2024 | Tiêu đề → lợi suất | ChatGPT/GPT-4 | Dự báo drift có ý nghĩa; Sharpe giảm theo thời gian |
| Vamvourellis & Mehta (2025) | T1 | PhraseBank | Phân loại zero-shot | GPT-4o, 4.1, o3-mini vs FinBERT | Lập luận không giúp |
| Luo (2026) | T1 và T4 | 5 tập T1; Benzinga 2019 | Phân loại; tín hiệu lợi suất | TF-IDF NB, FinBERT, QLoRA 7–8B | T1 tốt (acc 0,884); T4 không còn ý nghĩa sau hiệu chỉnh |
| Bisharat & Hean (2026) | T1 và T4 | Thông báo lợi nhuận | Phân loại; liên hệ lợi suất | 12 mô hình | LLM ngang Transformer; không liên hệ lợi suất ngày kế tiếp |

Một số điểm rút ra:

- **Hai FinBERT khác nhau về ngữ liệu và tác vụ (T1).** Araci tiếp tục tiền huấn luyện BERT trên một tập tin tức nhỏ (~29 triệu từ); Yang và cs. tiền huấn luyện từ đầu trên báo cáo doanh nghiệp, họp báo kết quả và báo cáo phân tích (~4,9 tỷ token). Kích thước mẫu đánh giá cũng khác (PhraseBank 4.845 so với 4.840 câu; FiQA 1.174 so với 1.111 câu), nên không so điểm trực tiếp được.
- **Khi nào Transformer vượt từ điển?** Mishev và cs. (2020) cho thấy ở T1, trên nhãn người, mô hình theo ngữ cảnh vượt từ điển. Kirtac & Germano (2024) *không* cho thấy điều đó, vì nhãn của họ là dấu lợi suất; kết quả của họ cho thấy mô hình tinh chỉnh trên nhãn lợi suất dự đoán dấu lợi suất tốt hơn từ điển không tinh chỉnh. Và từ điển Loughran–McDonald được xây cho văn bản dài như 10-K, gắn với kết quả tài chính chứ không phải nhãn câu.
- **Tín hiệu dự báo yếu đi khi kiểm định chặt hơn và theo thời gian (T4).** Bollen và cs. (2011) báo cáo 87,6% trên 15 ngày kiểm thử; Lopez-Lira & Tang cho thấy Sharpe suy giảm khi LLM phổ biến; Luo (2026) và Bisharat & Hean (2026) không tìm thấy tín hiệu vững. Các kết quả này là bằng chứng về T4, không phải về chất lượng trích xuất cảm xúc.

---

## 5. Dữ liệu, gán nhãn và đánh giá

### 5.1. Nguồn dữ liệu và cảm xúc phụ thuộc nguồn

| Nguồn | Ví dụ | Đặc điểm | Vấn đề |
|---|---|---|---|
| Báo cáo doanh nghiệp | 10-K (Loughran & McDonald, 2011) | Chính thức, dài | Cảm xúc tinh tế, nhiều văn bản lặp |
| Tin tức | Tetlock (2007); Ding và cs. (2015); Kirtac & Germano (2024) | Biên tập | Cảm xúc không trực tiếp; độ trễ |
| Bảng tin / mạng xã hội | Antweiler & Frank (2004); Das & Chen (2007); Bollen và cs. (2011); WallStreetBets (Rahman và cs., 2025) | Ngắn, chủ quan, tiếng lóng | Nhiễu, thao túng |
| Báo cáo phân tích, họp báo kết quả | Yang và cs. (2020) dùng làm ngữ liệu tiền huấn luyện | Chuyên môn | Ít bộ nhãn công khai (trong tập đã xem) |

Một mô hình huấn luyện trên Financial PhraseBank không mặc nhiên tốt trên StockTwits hay báo cáo thường niên. Trong tập tài liệu đã xem tôi chưa thấy công trình đánh giá trực tiếp tổng quát hóa giữa các nguồn; khẳng định "chưa ai làm" cần kiểm tra bằng tìm kiếm hệ thống.

### 5.2. Bộ dữ liệu chuẩn và vấn đề tái lập

- **Financial PhraseBank** (Malo và cs., 2014): khoảng 5.000 câu lấy mẫu từ 53.400 câu trong 10.000 bài tin về các công ty niêm yết trên OMX Helsinki, gán nhãn theo góc nhìn nhà đầu tư. Các bài sau dùng số câu hơi khác nhau (4.845 trong Araci và Mishev, 4.840 trong Yang và cs.), một dấu hiệu rằng phiên bản dữ liệu cần được ghi rõ khi so sánh.
- **FiQA** (Maia và cs., 2018): Task 1 là phân tích cảm xúc theo khía cạnh, gồm 529 tiêu đề (436 huấn luyện, 93 kiểm thử) và 774 bài vi blog (675 huấn luyện, 99 kiểm thử), có thực thể, khía cạnh và điểm cảm xúc gán thủ công. Task 2 là hỏi đáp dựa trên quan điểm (kho 57.640 bài trả lời, 17.110 cặp hỏi–đáp huấn luyện, 531 cặp kiểm thử), thu thập từ StackExchange giai đoạn 2009–2017. Các bài sau báo cáo số mẫu cảm xúc khác nhau (1.111, 1.173 hoặc 1.174), do cách tiền xử lý khác nhau; tập gốc có 1.303 mẫu Task 1.
- **FinLin** (Daudert, 2020): corpus cảm xúc theo thực thể, đa nguồn (báo cáo đầu tư, báo cáo công ty, tin tức, StockTwits), ngành ô tô, ba tháng, có điểm cảm xúc, điểm liên quan và đoạn văn làm bằng chứng.
- **AnalystTone** (theo Yang và cs., 2020): 10.000 câu từ báo cáo phân tích (3.580 tích cực, 1.830 tiêu cực, 4.590 trung lập).
- **SenseAI** (Kabalisa, 2026): 1.439 điểm dữ liệu cho 40 cổ phiếu Mỹ, có chuỗi lập luận, điểm tin cậy, hiệu chỉnh của người và kết quả thị trường; bản mới, chỉ có tóm tắt.

### 5.3. Gán nhãn và kiểm soát chất lượng

Financial PhraseBank là trường hợp được ghi nhận chi tiết nhất (Malo và cs., 2014):
- 16 người gán nhãn có kiến thức thị trường tài chính (3 nhà nghiên cứu, 13 sinh viên thạc sĩ Aalto), mỗi câu có 5–8 lượt gán, nhãn lấy theo đa số, hướng dẫn gán nhãn theo góc nhìn nhà đầu tư.
- Trên tập con 150 câu do cả 16 người gán: đồng thuận cặp 74,9%; phân biệt tích cực–tiêu cực đạt 98,7%, tiêu cực–trung lập 94,2%, còn **tích cực–trung lập chỉ 75,2%**, tức là khó nhất.
- Tập "đồng thuận 100%" có 2.259 câu (Malo; bản Hugging Face liệt kê 2.264), phân bố 13,4% tiêu cực, 61,4% trung lập, 25,2% tích cực; tập ">50%" có 4.840 câu.

Ba hệ quả:
1. **Nhãn mang giả định.** "Cảm xúc" ở đây là phán đoán về tác động tới nhà đầu tư, không thuần là sắc thái văn bản (Mục 2.1).
2. **Chọn ngưỡng đồng thuận làm thay đổi bài toán.** Araci báo cáo 0,86 accuracy trên toàn bộ nhưng 0,97 trên tập đồng thuận 100%; chọn tập nào quyết định mức "chính xác".
3. **Bất đồng không chỉ là nhiễu.** Vamvourellis & Mehta (2025) thấy suy luận của LLM kém hơn ở câu có mức đồng thuận thấp; Rahman và cs. (2025) cho rằng các lớp cảm xúc trong Financial PhraseBank thiếu định nghĩa rõ, nên LLM phải đoán quan điểm chủ quan của người gán nhãn. Bộ dữ liệu khác thường không công bố mức đồng thuận. Một bài 2026 trên SSRN về ảnh hưởng của mức đồng thuận gán nhãn đến hiệu năng phân loại FSA có trong kết quả tìm kiếm nhưng tôi chưa đọc (Phụ lục B). Câu hỏi nên ép một nhãn hay biểu diễn bất đồng vẫn còn mở.

### 5.4. Giao thức đánh giá

Khung dưới là đề xuất tổ chức của tôi theo bốn tầng (Mục 3.4). Mỗi tầng cần chỉ số riêng, và không nên dùng chỉ số của tầng này để suy ra chất lượng tầng khác:

| Tầng | Chỉ số |
|---|---|
| T1. Trích xuất (phân loại) | Accuracy, Macro-F1, MCC, Precision, Recall, mức đồng thuận người gán nhãn |
| T1. Trích xuất (chấm điểm) | MAE, RMSE, MSE, R², Pearson/Spearman (FiQA: MSE, R², cosine) |
| T2. Tổng hợp | Độ ổn định, độ hợp lệ hội tụ của chỉ số; tương quan với thước đo độc lập |
| T3. Phản ứng thị trường | Lợi suất bất thường, thay đổi phương sai/khối lượng, kiểm định ý nghĩa |
| T4. Dự báo | Độ chính xác chiều, MAE, RMSE, AUC, IC thứ hạng |
| T4. Giao dịch | Sharpe, lợi nhuận tích lũy, chi phí giao dịch, sụt giảm tối đa |

Về chia dữ liệu: ngẫu nhiên, phân tầng, theo thời gian, walk-forward, ngoài miền. Chia theo thời gian đặc biệt quan trọng ở T4: huấn luyện trên dữ liệu muộn hơn kiểm thử hoặc để tin gần trùng lặp ở cả hai tập làm kết quả không phản ánh khả năng triển khai. Ví dụ trong tập đã xem:
- *Chưa tách thời gian:* Kirtac & Germano (2024) chia ngẫu nhiên 20% làm kiểm thử cho phần độ chính xác; Nguyen P. A. và cs. (2026) dùng kiểm định chéo 10 lần cho dự báo chiều VN-Index, một thiết lập dễ gây rò rỉ thời gian với chuỗi giá (nhận định của tôi). Araci dùng kiểm định chéo 10 lần trên FiQA trong khi các baseline dùng tập kiểm thử chính thức.
- *Tốt hơn:* Lopez-Lira & Tang dùng mẫu hoàn toàn sau thời điểm cắt dữ liệu của mô hình; Luo (2026) dùng mẫu 2019 riêng biệt về thời gian, suy luận Newey–West và hiệu chỉnh FDR; Bisharat & Hean (2026) đánh giá theo hai tiêu chí tách bạch (hợp lệ ngôn ngữ và hợp lệ kinh tế).

---

## 6. Ứng dụng của FSA: từ tổng hợp đến giao dịch

Mục này đi theo T2–T4 của Mục 3.4. Các công trình dự báo được giữ lại vì chúng cho thấy FSA được dùng để làm gì, nhưng được đánh giá theo tiêu chí của tầng mình, không theo tiêu chí phân loại cảm xúc.

| Tầng | Câu hỏi | Công trình ví dụ | Điều bằng chứng cho phép kết luận |
|---|---|---|---|
| **T2. Tổng hợp cảm xúc** | Tạo chỉ số cấp doanh nghiệp, ngành, thị trường thế nào? | Loughran & McDonald (2011); Tetlock (2007); Das & Chen (2007) | Chỉ số đo được một khía cạnh ổn định của văn bản |
| **T3. Phản ứng thị trường** | Thị trường phản ứng thế nào với cảm xúc/thông tin? | Tetlock (2007); Antweiler & Frank (2004); Vu và cs. (2023); Bisharat & Hean (2026, liên hệ với bất ngờ lợi nhuận) | Có quan hệ thống kê hay không; chưa hàm ý dự báo |
| **T4. Dự báo và giao dịch** | Cảm xúc có làm tín hiệu dự báo ngoài mẫu? | Bollen và cs. (2011); Ding và cs. (2015); Lopez-Lira & Tang (2023); Kirtac & Germano (2024); Luo (2026); Nguyen P. A. và cs. (2026) | Giá trị dự báo trong thiết lập cụ thể; cần kiểm định thêm |

Hệ quả logic: đo cảm xúc tốt (T1–T2) không chứng minh dự báo được giá; tương quan (T3) không chứng minh dự báo ngoài mẫu; dự báo được lợi suất (T4) không bảo đảm chiến lược có lãi sau chi phí. Các con số sau đều là bằng chứng về T4 và cần đọc kèm thiết lập:
- **Bollen và cs. (2011):** tweet 28/02–19/12/2008 (9.853.498 tweet, khoảng 2,7 triệu người dùng); huấn luyện đến 28/11/2008, kiểm thử 01–19/12/2008 (15 ngày). Độ chính xác 87,6% khi dự đoán chiều DJIA hằng ngày; kiểm định Granger cho thấy chỉ Calm (và phần nào Happy) có quan hệ Granger với DJIA, còn thước đo cực tính của OpinionFinder không cải thiện dự báo. Mẫu kiểm thử nhỏ; chính các tác giả tính xác suất đạt kết quả này do ngẫu nhiên là 0,32% (3,4% khi xét cả việc chọn kỳ kiểm thử 20 ngày).
- **Ding và cs. (2015):** khoảng 6% cải thiện so với baseline trên Reuters và Bloomberg.
- **Lopez-Lira & Tang (bản 10/2025):** 34 điểm cơ bản mỗi ngày trước chi phí giao dịch, Sharpe 2,97 (drift, GPT-4), Sharpe giảm từ 6,54 xuống 1,22 trong 2021–2024.
- **Kirtac & Germano (2024):** Sharpe 3,05 sau chi phí 10 điểm cơ bản mỗi giao dịch, backtest, nhãn lấy từ lợi suất.
- **Luo (2026), Bisharat & Hean (2026):** không có tín hiệu lợi suất vững sau hiệu chỉnh / không có quan hệ có ý nghĩa với lợi suất ngày kế tiếp.

Về T3, Vu và cs. (2023) không thấy khác biệt đáng kể về giá sau tin nhưng thấy tin tiêu cực làm đổi phương sai lợi suất; đây là kết quả về phản ứng thị trường, không phải về độ chính xác của bộ phân loại (trên 81% là kết quả T1 của cùng bài). Quản trị rủi ro và tư vấn tự động chủ yếu được thảo luận trong các khảo sát LLM (Nie và cs., 2024); tôi chưa có bằng chứng thực nghiệm đủ mạnh trong tập đã xem.

---

## 7. Thách thức và vấn đề mở

1. **Thiên lệch nhìn trước và hiệu ứng xao nhãng.** Glasserman và Lin (2023) cho thấy ở trong mẫu, ẩn danh hóa thực thể cải thiện kết quả, tức hiệu ứng xao nhãng lấn át thiên lệch nhìn trước; Nakagawa và cs. (2024) định lượng thiên lệch theo công ty. Lopez-Lira & Tang giải quyết bằng cách chỉ dùng mẫu sau thời điểm cắt dữ liệu của mô hình. Kết quả backtest LLM trên giai đoạn trước hoặc chồng với dữ liệu huấn luyện (như Kirtac & Germano, 2010–2023, với OPT và BERT) cần được đọc cùng ngày cắt dữ liệu huấn luyện.
2. **Tái lập và chi phí.** Mô hình đóng hay API đổi phiên bản làm khó tái lập; FinGPT, FinMA và Transformer rút gọn là hướng giảm chi phí.
3. **Ý nghĩa kinh tế so với thống kê, và suy giảm theo thời gian.** Tương quan nhỏ nhưng có ý nghĩa thống kê, Sharpe cao trong backtest và Sharpe giảm khi công nghệ phổ biến (Lopez-Lira & Tang) đều cần kiểm định ngoài mẫu và tính chi phí giao dịch.
4. **Cảm xúc không bằng tác động lên giá.** Ba bài toán cần tách: hiểu cảm xúc văn bản (T1); đánh giá tin tốt hay xấu cho doanh nghiệp (T1 với nhãn tác động); dự đoán phản ứng thị trường (T3–T4). Bằng chứng không bắc cầu giữa các tầng (Luo, 2026; Bisharat & Hean, 2026).
5. **Tính chủ quan và định nghĩa nhãn.** Mức đồng thuận tích cực–trung lập chỉ 75,2% trong PhraseBank; Rahman và cs. (2025) lập luận các lớp thiếu định nghĩa.
6. **Chia dữ liệu và rò rỉ thời gian.** Chia ngẫu nhiên (Kirtac & Germano) hoặc kiểm định chéo cho chuỗi giá (Nguyen P. A. và cs.) có thể thổi phồng kết quả.
7. **Diễn giải.** Từ điển minh bạch nhưng thô, mô hình sâu chính xác hơn nhưng khó giải thích.
8. **Độ tin cậy của LLM khi gán nhãn.** Vamvourellis & Mehta (2025) cho thấy cấu hình prompt ảnh hưởng độ khớp nhãn người; Kabalisa (2026) mô tả hiện tượng mô hình đưa thông tin không có trong đầu vào vào lập luận ("Latent Reasoning Drift", theo tóm tắt). Tính ổn định giữa các lần chạy chưa được đo trực tiếp trong tập đã xem.

---

## 8. FSA tiếng Việt

Phần này ghi nhận những gì tôi tìm được; **bằng chứng còn mỏng và quy trình tìm kiếm tự động bỏ lỡ toàn bộ** (Mục 1.4), nên không đủ để khẳng định toàn bộ bức tranh FSA tiếng Việt.

### 8.1. Bức tranh nghiên cứu

| Công trình | Ngôn ngữ văn bản | Nguồn dữ liệu | Quy mô | Nhãn | Bài toán, mô hình | Kết quả (theo tác giả) |
|---|---|---|---|---|---|---|
| Nguyen S. T. và cs. (2021), CEUR Vol-3026 | Tiếng Việt | Tiêu đề CafeF | 1.000 tiêu đề; chia 80/10/10 nên tập kiểm thử khoảng 100 | 3 lớp: 187 tiêu cực, 248 không tác động, 565 tích cực; "có sự giúp đỡ của chuyên gia" | Phân loại. PhoBERT, SVM, LR, LSTM, Random Forest, Naive Bayes | PhoBERT: acc 93,12%, F1 90,63%; mô hình tốt thứ hai là Logistic Regression: acc 82,58% |
| Vu và cs. (2023), IJFS 11(3), 101 | Tiếng Việt | Web tài chính–kinh tế | Gần 40.000 bài huấn luyện (theo tóm tắt) | Chưa xác minh | Phân loại bằng PhoBERT; kiểm định phản ứng thị trường | Accuracy trên 81%; không khác biệt đáng kể về giá sau tin, nhưng tin tiêu cực làm đổi phương sai lợi suất |
| Thanh và cs. (2025), VNUHCM JELB 9(1) | Tiếng Việt | VnExpress, VnEconomy, 2024 | 5.126 câu gán nhãn (từ 4.065 bài, 7.130 câu trích) | Nhị phân, chuyên gia trên 20 năm kinh nghiệm; không báo số người gán nhãn hay mức đồng thuận | Ngân hàng câu cảm xúc về khối ngoại; embedding + LR/SVM/RF | SVM accuracy 89% |
| Việt và cs. (2026), JCSC 42(2) | Tiếng Việt | Tin tức ngân hàng | 12.000 mẫu gán nhãn | Chưa xác minh | Phân loại chủ đề và cảm xúc; PhoBERT, ViT5, BARTPho so với LLaMA-3.1-8B, Vistral-7B | Mô hình tinh chỉnh hơn LLM đa dụng về độ chính xác và hiệu quả |
| Nguyen P. A. và cs. (2026), VNUHCM JELB 10(1) | **Tiếng Anh** (Vietnamnet English) | 6.480 bài, 2019–2025 | Khoảng 1.196 quan sát (theo bảng thống kê mô tả) | Không có nhãn: điểm từ điển (polarity, subjectivity) và VADER | Dự báo chiều VN-Index; 7 mô hình học máy, kiểm định chéo 10 lần | Mô hình tổ hợp tốt nhất; đặc trưng cảm xúc bổ sung giá trị dự báo |
| Pham, Phan & Truong (2025), LNCS (IDEAL 2025) | Tin tức | – | – | – | Dự báo khó khăn tài chính; dùng điểm cảm xúc từ vinai/phobert-base (theo kết quả tìm kiếm) | Chưa xác minh (chỉ có siêu dữ liệu) |

Hai điều chỉnh quan trọng so với các bản trước: (i) Nguyen P. A. và cs. (2026) **không xử lý văn bản tiếng Việt**: dữ liệu là tin tiếng Anh của Vietnamnet và cảm xúc được tính bằng từ điển tiếng Anh, nên đây là FSA tiếng Anh về thị trường Việt Nam, không phải FSA tiếng Việt; (ii) số công trình xử lý văn bản tiếng Việt được kiểm tra là bốn, cộng một chương sách chưa xác minh.

Theo mô hình bốn tầng, Nguyen S. T. và cs. (2021), Thanh và cs. (2025) và Việt và cs. (2026) chủ yếu ở T1; Vu và cs. (2023) kết hợp T1 với T3; Nguyen P. A. và cs. (2026) dùng đặc trưng cảm xúc tổng hợp (T2) cho dự báo chiều VN-Index (T4). Như vậy tiếng Việt đã có bằng chứng ở T1 và T3 nhưng T4 mới được thử với tin tiếng Anh, và nhìn chung chưa tách riêng đánh giá T1 khỏi kết quả T4.

Về chi tiết: có một mâu thuẫn nhỏ về Vu và cs. (2023): tóm tắt trên Crossref nói huấn luyện PhoBERT trên gần 40.000 bài với độ chính xác trên 81%, trong khi một tóm tắt thứ cấp nêu 2.738 bài gán nhãn dương/âm; có thể 2.738 là tập có nhãn còn 40.000 là ngữ liệu, nhưng tôi chưa xác minh được vì máy chủ MDPI từ chối truy cập (HTTP 403) và tôi không tìm cách vượt qua. Thanh và cs. (2025) cũng không giải thích vì sao 7.130 câu còn 5.126, và tóm tắt nói tám nhóm hành vi nhưng phần phương pháp liệt kê bảy.

### 8.2. Bộ dữ liệu tiếng Việt

| Bộ dữ liệu | Quy mô | Nhãn | Công khai? | Thông tin còn thiếu |
|---|---|---|---|---|
| Tiêu đề CafeF (Nguyen S. T. và cs., 2021) | 1.000 | 3 lớp, mất cân bằng (56,5% tích cực) | Có: bài ghi mã nguồn và dữ liệu ở GitHub (bài theo giấy phép CC BY 4.0; kho mã không nêu giấy phép; không nêu giai đoạn thu thập) | Quy trình gán nhãn, đồng thuận |
| Ngân hàng câu khối ngoại (Thanh và cs., 2025) | 5.126 | Nhị phân | Chưa xác nhận (bài ghi có phụ lục mã) | Số người gán nhãn, đồng thuận, nhãn trung lập |
| Ngữ liệu Vu và cs. (2023) | ~40.000 bài | Chưa xác minh | Chưa xác nhận | Nhãn, công khai |
| Ngữ liệu ngân hàng (Việt và cs., 2026) | 12.000 | Có | Chưa xác nhận | Nguồn, nhãn |

So với Financial PhraseBank (nhãn ba lớp, 16 người gán nhãn, 5–8 lượt gán mỗi câu, báo cáo đồng thuận), chưa bộ tiếng Việt nào tôi tìm thấy công bố quy trình tương đương. Thanh và cs. (2025) dùng nhãn nhị phân nên không có lớp trung lập; ở PhraseBank trung lập chiếm khoảng 60% và là lớp gây bất đồng nhiều nhất, nên kết quả hai bộ không so trực tiếp được. Bộ CafeF có tập kiểm thử khoảng 100 tiêu đề, nên con số 93,12% có sai số lấy mẫu lớn (mỗi tiêu đề sai tương đương khoảng một điểm phần trăm). Tôi cũng thấy một mô hình PhoBERT trên Hugging Face được tinh chỉnh bằng nhãn "bạc" do LLM sinh (không phải gán nhãn người) và không có chỉ số đánh giá; đó là thông tin từ model card, không phải nghiên cứu được đánh giá.

### 8.3. Thách thức đặc thù ngôn ngữ

Bằng chứng trực tiếp trong tập đã xem chỉ có hai điểm: PhoBERT đòi hỏi văn bản phải được tách từ trước khi tách token (Nguyen & Nguyen, 2020), và Nguyen S. T. và cs. (2021) dùng VnCoreNLP để tách từ và nhận diện thực thể. Các điểm sau chỉ là câu hỏi cần khảo sát, chưa có bài nào được kiểm tra để khẳng định đó là khó khăn đặc thù tiếng Việt: từ ghép và tách từ ảnh hưởng thế nào đến chất lượng; từ đa nghĩa trong ngữ cảnh tài chính; trộn mã Việt–Anh; viết tắt, mã chứng khoán và tên doanh nghiệp; tiếng lóng diễn đàn; phủ định và mỉa mai.

### 8.4. Các mô hình đã được nghiên cứu

| Mô hình | Bằng chứng |
|---|---|
| PhoBERT | Có (Nguyen S. T. và cs., 2021; Vu và cs., 2023; Việt và cs., 2026) |
| ViT5, BARTPho | Có (Việt và cs., 2026) |
| ML truyền thống | Có: SVM, LR, Random Forest, Naive Bayes, LSTM trên dữ liệu CafeF (Nguyen S. T. và cs., 2021); embedding + LR/SVM/RF (Thanh và cs., 2025) |
| LLM đa dụng | Có, làm baseline: LLaMA-3.1-8B, Vistral-7B (Việt và cs., 2026) |
| XLM-R, mBERT | Chưa thấy trong FSA (PhoBERT được báo cáo vượt XLM-R trên các tác vụ NLP chung, nhưng không phải tài chính) |
| LLM với prompt tài chính (few-shot, kiểu GPT-4o) | Chưa thấy trong tiếng Việt |

"Chưa thấy" nghĩa là tôi chưa tìm thấy, không phải chưa ai nghiên cứu. Hướng tiếng Việt thiên về mô hình tinh chỉnh dựa trên PhoBERT, trong khi nghiên cứu quốc tế (Mục 4.4) đã chuyển sang so sánh LLM few-shot với FinBERT và kiểm tra giá trị kinh tế.

### 8.5. Ứng dụng và so sánh với FSA toàn cầu

Ứng dụng đã thấy: phản ứng thị trường quanh tin (Vu và cs., 2023), dự báo chiều VN-Index từ tin tiếng Anh (Nguyen P. A. và cs., 2026), tổng hợp tin ngân hàng (Việt và cs., 2026). Chưa thấy: cảm xúc theo doanh nghiệp hoặc ngành, theo sự kiện, chỉ số tâm lý thị trường từ văn bản tiếng Việt, dự báo biến động.

So với toàn cầu, FSA tiếng Việt (i) mới từ khoảng 2021 trở đi; (ii) chỉ dùng văn bản tin tức; (iii) thiếu benchmark chung và đồng thuận gán nhãn công bố; (iv) chưa có bài kiểm tra tổng quát hóa giữa nguồn hay giữa giai đoạn; (v) chưa thấy LLM dùng làm bộ phân loại với prompt tài chính, và chưa thấy đánh giá hợp lệ kinh tế (T4 với văn bản tiếng Việt) theo chuẩn của Luo (2026) hay Bisharat & Hean (2026). Nhận định này giới hạn trong các tìm kiếm của bài.

### 8.6. So sánh với các ngôn ngữ ít tài nguyên khác

Tìm kiếm có mã lệnh cho thấy các ngôn ngữ khác đang đi trước trong việc so sánh mô hình tiền huấn luyện với LLM (chỉ có siêu dữ liệu và tiêu đề, trừ khi nêu khác): tiếng Ả Rập (Almusned và cs., 2026, nhận xét các mô hình như AraBERT và CAMeLBERT được huấn luyện trên văn bản tổng quát hoặc mạng xã hội và gặp khó với văn bản tài chính), tiếng Thái (Leechewyuwasorn & Wangpratham, 2024: mô hình NLP truyền thống so với GPT và Gemini), tiếng Bangla (Hasan và cs., 2025: ABSA giải thích được cho tin tài chính bằng LLM), tiếng Nhật (Nakagawa và cs., 2024), và văn bản không phải tiếng Anh nói chung (Jang & Wu, 2025, về MD&A trong dự báo của nhà phân tích). Đây là cơ sở để đề xuất cho tiếng Việt một thiết kế tương tự: so sánh PhoBERT, mô hình đa ngữ và LLM few-shot trên cùng benchmark có nhãn người, rồi mới kiểm tra giá trị kinh tế.

---

## 9. Khoảng trống nghiên cứu và hướng tương lai

| Khoảng trống | Vấn đề chưa giải quyết | Bằng chứng trong bài | Tiềm năng với tiếng Việt |
|---|---|---|---|
| Tổng quát hóa giữa nguồn | Mô hình có chuyển từ tin tức sang diễn đàn, báo cáo không? | Chưa thấy đánh giá trực tiếp (5.1); tiếng Việt chỉ có tin tức (8.1) | Cao |
| Độ bền theo thời gian | Ổn định qua các giai đoạn? | Gián tiếp: Sharpe suy giảm (7.3); chia ngẫu nhiên (5.4) | Cao |
| Cảm xúc theo thực thể và khía cạnh | Cảm xúc hướng đến thực thể nào? | FiQA Task 1 khó (accuracy khía cạnh tiêu đề 0,27); FinLin; tiếng Việt che thực thể (3.5) | Cao |
| Bất đồng khi gán nhãn | Cảm xúc tài chính có nhất quán? | Số liệu cho PhraseBank (5.3); tiếng Việt chưa công bố | Cao |
| Cảm xúc văn bản so với tác động thị trường | Có phản ánh tác động kinh tế? | 2.1, 7.4; Luo (2026); Bisharat & Hean (2026) | Cao |
| LLM few-shot so với mô hình tinh chỉnh | LLM có thay được mô hình tinh chỉnh trên tiếng Việt? | Quốc tế: gần bằng (4.4b); tiếng Việt: chỉ có baseline (8.4) | Cao |
| Đánh giá không rò rỉ thời gian | Backtest LLM không nhìn trước | Glasserman & Lin (2023); Lopez-Lira & Tang (mẫu sau thời điểm cắt dữ liệu) | Cao |
| Đánh giá tách tầng | Báo cáo riêng T1 (nhãn người) và T4 (ngoài mẫu) cho cùng hệ thống | Luo (2026) và Bisharat & Hean (2026) làm; Kirtac & Germano gộp; tiếng Việt thường gộp (8.1) | Cao |
| Độ tin cậy của LLM | Nhất quán, ít ảo giác? | Rất ít (7.8) | Trung bình |

Hai ưu tiên: (1) xây benchmark tiếng Việt công khai với ba lớp (có trung lập), hướng dẫn gán nhãn, nhiều người gán nhãn và đồng thuận được báo cáo, đủ nhiều nguồn để đo tổng quát hóa; (2) đánh giá tách tầng: T1 bằng nhãn người, T4 bằng kiểm định ngoài mẫu có tách thời gian và hiệu chỉnh kiểm định đa lần. Hướng về mô hình nhẹ và đa phương thức đáng làm nhưng cần xuất phát từ các khoảng trống bằng chứng trên.

---

## 10. Kết luận

FSA đã đi từ đếm từ trong từ điển, qua học máy và học sâu, đến Transformer chuyên ngành và LLM. Điểm cốt lõi không nằm ở thứ tự thời gian mà ở hai đóng góp tổng hợp: năm trục độc lập để mô tả một công trình làm gì, và bốn tầng (trích xuất, tổng hợp, phản ứng thị trường, dự báo) để tách phân loại cảm xúc khỏi các ứng dụng của nó. Việc tách tầng có hệ quả thực tế: một số con số nổi bật, như độ chính xác của Kirtac & Germano (2024), hóa ra là thước đo dự đoán lợi suất chứ không phải chất lượng nhận diện cảm xúc, còn các đánh giá 2026 cho thấy độ chính xác phân loại cao không bảo đảm tín hiệu lợi suất. Trên benchmark cảm xúc, LLM few-shot hiện gần bằng mô hình tinh chỉnh chứ chưa vượt rõ. Với tiếng Việt, đã có các bước đi đầu với PhoBERT và một ngân hàng câu cảm xúc nhị phân, nhưng nhu cầu cấp thiết nhất vẫn là dữ liệu chuẩn mở, quy trình gán nhãn minh bạch, và đánh giá tách tầng có kiểm soát thời gian.

---

## Tài liệu tham khảo (APA 7)

Antweiler, W., & Frank, M. Z. (2004). Is all that talk just noise? The information content of Internet stock message boards. *The Journal of Finance, 59*(3), 1259–1294.

Araci, D. (2019). *FinBERT: Financial sentiment analysis with pre-trained language models*. arXiv:1908.10063. https://arxiv.org/abs/1908.10063

Bisharat, A., & Hean, O. (2026). *Evaluating financial sentiment in the age of AI*. arXiv:2609.20198. https://arxiv.org/abs/2609.20198

Bollen, J., Mao, H., & Zeng, X. (2011). Twitter mood predicts the stock market. *Journal of Computational Science, 2*(1), 1–8. (Bản tiền ấn: arXiv:1010.3003)

Daudert, T. (2020). *A multi-source entity-level sentiment corpus for the financial domain: The FinLin corpus*. arXiv:2003.04073. https://arxiv.org/abs/2003.04073

Das, S. R., & Chen, M. Y. (2007). Yahoo! for Amazon: Sentiment extraction from small talk on the web. *Management Science, 53*(9), 1375–1388. https://doi.org/10.1287/mnsc.1070.0704

Ding, X., Zhang, Y., Liu, T., & Duan, J. (2015). Deep learning for event-driven stock prediction. *Proceedings of IJCAI 2015*, 2327–2333.

Du, K., Xing, F., Mao, R., & Cambria, E. (2024). An evaluation of reasoning capabilities of large language models in financial sentiment analysis. *2024 IEEE Conference on Artificial Intelligence (CAI)*, 189–194. https://doi.org/10.1109/CAI59869.2024.00042

Gao, L. (2026). A survey of zero-shot and few-shot learning with large language models for financial sentiment analysis. *Applied and Computational Engineering, 254*(1), 89–95. https://doi.org/10.54254/2755-2721/2026.ld35648

Glasserman, P., & Lin, C. (2023). *Assessing look-ahead bias in stock return predictions generated by GPT sentiment analysis*. arXiv:2309.17322. https://arxiv.org/abs/2309.17322

Kabalisa, B. (2026). *SenseAI: A human-in-the-loop dataset for RLHF-aligned financial sentiment reasoning*. arXiv:2604.05135. https://arxiv.org/abs/2604.05135

Kearney, C., & Liu, S. (2014). Textual sentiment in finance: A survey of methods and models. *International Review of Financial Analysis, 33*, 171–185. https://doi.org/10.1016/j.irfa.2014.02.006

Kirtac, K., & Germano, G. (2024). Sentiment trading with large language models. *Finance Research Letters, 62*, 105227. (Bản tiền ấn: arXiv:2412.19245)

Kirtac, K., & Germano, G. (2025). *Large language models in finance: What is financial sentiment?* arXiv:2503.03612. https://arxiv.org/abs/2503.03612

Lefort, B., Benhamou, E., Ohana, J.-J., Saltiel, D., Guez, B., & Challet, D. (2024). *Can ChatGPT compute trustworthy sentiment scores from Bloomberg market wraps?* arXiv:2401.05447. https://arxiv.org/abs/2401.05447

Li, X., Chan, S., Zhu, X., Pei, Y., Ma, Z., Liu, X., & Shah, S. (2023). Are ChatGPT and GPT-4 general-purpose solvers for financial text analytics? A study on several typical tasks. *EMNLP 2023 Industry Track*. arXiv:2305.05862. https://arxiv.org/abs/2305.05862

Lopez-Lira, A., & Tang, Y. (2023). *Can ChatGPT forecast stock price movements? Return predictability and large language models* (bản 6, 10/2025). arXiv:2304.07619. https://arxiv.org/abs/2304.07619

Loughran, T., & McDonald, B. (2011). When is a liability not a liability? Textual analysis, dictionaries, and 10-Ks. *The Journal of Finance, 66*(1), 35–65.

Loughran, T., & McDonald, B. (2016). Textual analysis in accounting and finance: A survey. *Journal of Accounting Research, 54*(4), 1187–1230. https://doi.org/10.1111/1475-679X.12123

Luo, F. (2026). *From financial sentiment classification to return predictability: A QLoRA benchmark of large language models*. arXiv:2608.04200. https://arxiv.org/abs/2608.04200

Maia, M., Handschuh, S., Freitas, A., Davis, B., McDermott, R., Zarrouk, M., & Balahur, A. (2018). WWW'18 open challenge: Financial opinion mining and question answering. *Companion Proceedings of The Web Conference 2018*, 1941–1942. https://doi.org/10.1145/3184558.3192301

Malo, P., Sinha, A., Korhonen, P., Wallenius, J., & Takala, P. (2014). Good debt or bad debt: Detecting semantic orientations in economic texts. *Journal of the Association for Information Science and Technology, 65*(4), 782–796. https://doi.org/10.1002/asi.23062

Mishev, K., Gjorgjevikj, A., Vodenska, I., Chitkushev, L. T., & Trajanov, D. (2020). Evaluation of sentiment analysis in finance: From lexicons to transformers. *IEEE Access, 8*, 131662–131682. https://doi.org/10.1109/ACCESS.2020.3009626

Nakagawa, K., Hirano, M., & Fujimoto, Y. (2024). *Evaluating company-specific biases in financial sentiment analysis using large language models*. arXiv:2411.00420. https://arxiv.org/abs/2411.00420

Nguyen, D. Q., & Nguyen, A. T. (2020). PhoBERT: Pre-trained language models for Vietnamese. *Findings of EMNLP 2020*. arXiv:2003.00744. https://arxiv.org/abs/2003.00744

Nguyen, P. A., Phan Huy, T., & Ngo Phu, T. (2026). Sentiment-driven forecasting of the stock index in Vietnam: A machine learning perspective. *VNUHCM Journal of Economics, Business and Law, 10*(1), 6410–6424. https://doi.org/10.32508/stdjelm.v10i1.1687

Nguyen, S. T., Nguyen, N. L., Tran, T., Nguyen, T. T., Duong, T. T. P., & Nguyen, T. (2021). Stock article title sentiment-based classification using PhoBERT. *Proceedings of the 2nd International Conference on Human-centered Artificial Intelligence (Computing4Human 2021)*, CEUR Workshop Proceedings, Vol. 3026, 225–233. https://ceur-ws.org/Vol-3026/paper25.pdf

Nie, Y., Kong, Y., Dong, X., Mulvey, J. M., Poor, H. V., Wen, Q., & Zohren, S. (2024). *A survey of large language models for financial applications: Progress, prospects and challenges*. arXiv:2406.11903. https://arxiv.org/abs/2406.11903

Pham, V. T., Phan, D. H., & Truong, C. D. (2025). Leveraging sentiment analysis for improved financial distress forecasting in Vietnamese-listed firms. *Lecture Notes in Computer Science (IDEAL 2025)*. https://doi.org/10.1007/978-3-032-10486-1_12 *(chỉ có siêu dữ liệu; trang và nội dung chưa xác minh)*

Rahman, A. M. M., Uddin, A., & Wang, G. (2025). *Evaluating financial sentiment analysis with annotators instruction assisted prompting: Enhancing contextual interpretation and stock prediction accuracy*. arXiv:2505.07871. https://arxiv.org/abs/2505.07871

Rodriguez Inserte, P., Nakhlé, M., Qader, R., Caillaut, G., & Liu, J. (2024). *Large language model adaptation for financial sentiment analysis*. arXiv:2401.14777. https://arxiv.org/abs/2401.14777

Shen, Y., & Zhang, P. K. (2024). *Financial sentiment analysis on news and reports using large language models and FinBERT*. arXiv:2410.01987. https://arxiv.org/abs/2410.01987

Tetlock, P. C. (2007). Giving content to investor sentiment: The role of media in the stock market. *The Journal of Finance, 62*(3), 1139–1168. https://doi.org/10.1111/j.1540-6261.2007.01232.x

Thanh, X. P. T., Anh, N. D., & Ha, P. T. (2025). Building a financial sentiment bank on the investment behavior of foreign investors [Ngân hàng câu cảm xúc tài chính về hành vi của khối ngoại]. *VNUHCM Journal of Economics, Business and Law, 9*(1), 6103–6112. https://doi.org/10.32508/stdjelm.v9i1.1548 *(thứ tự tên theo trang tạp chí; cần chuẩn hóa họ–tên khi nộp)*

Vamvourellis, D., & Mehta, D. (2025). *Reasoning or overthinking: Evaluating large language models on financial sentiment analysis*. arXiv:2506.04574. https://arxiv.org/abs/2506.04574

Việt, A. P., Minh, H. P., Quoc, H. N., Duc, A. N., & Hai, L. T. (2026). Fine-tuned language models for intelligent aggregation systems in the banking sector. *Journal of Computer Science and Cybernetics, 42*(2), 167–181. https://vjs.ac.vn/jcc/article/view/22428 *(họ–tên theo trang tạp chí, cần chuẩn hóa)*

Vu, L. T., Pham, D. N., Kieu, H. T., & Pham, T. T. T. (2023). Sentiments extracted from news and stock market reactions in Vietnam. *International Journal of Financial Studies, 11*(3), 101. https://doi.org/10.3390/ijfs11030101

Wei, X., & Liu, L. (2025). *Are large language models good in-context learners for financial sentiment analysis?* arXiv:2503.04873. https://arxiv.org/abs/2503.04873

Wu, S., Irsoy, O., Lu, S., Dabravolski, V., Dredze, M., Gehrmann, S., Kambadur, P., Rosenberg, D., & Mann, G. (2023). *BloombergGPT: A large language model for finance*. arXiv:2303.17564. https://arxiv.org/abs/2303.17564

Xie, Q., Han, W., Zhang, X., Lai, Y., Peng, M., Lopez-Lira, A., & Huang, J. (2023). *PIXIU: A large language model, instruction data and evaluation benchmark for finance*. arXiv:2306.05443. https://arxiv.org/abs/2306.05443

Xie, Q., Han, W., Chen, Z., Xiang, R., Zhang, X., He, Y., et al. (2024). *FinBen: A holistic financial benchmark for large language models*. arXiv:2402.12659. https://arxiv.org/abs/2402.12659

Xing, F. Z., Cambria, E., & Welsch, R. E. (2018). Natural language based financial forecasting: A survey. *Artificial Intelligence Review, 50*(1), 49–73. https://doi.org/10.1007/s10462-017-9588-9

Yang, H., Liu, X.-Y., & Wang, C. D. (2023). *FinGPT: Open-source financial large language models*. arXiv:2306.06031. https://arxiv.org/abs/2306.06031

Yang, Y., Uy, M. C. S., & Huang, A. (2020). *FinBERT: A pretrained language model for financial communications*. arXiv:2006.08097. https://arxiv.org/abs/2006.08097

Zhang, B., Yang, H., & Liu, X.-Y. (2023). *Instruct-FinGPT: Financial sentiment analysis by instruction tuning of general-purpose large language models*. arXiv:2306.12659. https://arxiv.org/abs/2306.12659

Zhao, Z., & Welsch, R. E. (2024). *Aligning LLMs with human instructions and stock market feedback in financial sentiment analysis*. arXiv:2410.14926. https://arxiv.org/abs/2410.14926

---

## Phụ lục A. Quy trình tái lập lộ trình tìm kiếm 1

1. Chạy bốn truy vấn arXiv (tối đa 300 kết quả mỗi truy vấn, sắp theo độ liên quan, lọc ngày nộp từ 01/01/2000 đến 31/10/2026) và bốn truy vấn Crossref (`query.bibliographic`, 200 kết quả đầu, lọc ngày xuất bản cùng khoảng) như ở Mục 1.4.
2. Chuẩn hóa tiêu đề (chữ thường, bỏ ký tự không chữ-số), loại trùng.
3. Sàng 1: tiêu đề hoặc tóm tắt chứa một trong các từ *sentiment, opinion, emotion, mood, tone, polarity* và một từ tài chính (*financ, stock, market, invest, econom, bank, earning, 10-k, trading, fintech, crypto, bitcoin, equity, fund*).
4. Sàng 2: tiêu đề phải có từ cảm xúc (*sentiment, opinion, emotion, mood, tone*); với Crossref (không có tóm tắt) tiêu đề cũng phải có từ tài chính.
5. Nhóm ưu tiên: năm xuất bản ≥ 2024 và tiêu đề có từ khóa khảo sát, benchmark, dữ liệu, ngân hàng, LLM, đánh giá, thiên lệch, gán nhãn; đọc tiêu đề thủ công.
6. Giới hạn: top 200 của Crossref không đại diện cho toàn bộ; độ phủ đo được chỉ 14/33 công trình chính (Mục 1.4). Mã lệnh và kết quả thô hiện nằm trong thư mục tạm của phiên làm việc và chưa được đưa vào kho mã.

## Phụ lục B. Công trình 2024–2026 tìm thấy nhưng chưa đọc

Danh sách dưới chỉ là kết quả của lộ trình 1 ở nhóm ưu tiên; **không được xem là bằng chứng**. Cần đọc trước khi trích dẫn trong nội dung.

| Năm | Tiêu đề | Nguồn |
|---|---|---|
| 2026 | Benchmarking large language models for target-based financial sentiment and stock return | Crossref (DOI 10.1007/s41060-026-01201-x; chưa lấy được siêu dữ liệu do giới hạn tốc độ) |
| 2026 | Financial sentiment analysis: The effect of annotation agreement on classification performance | SSRN (DOI 10.2139/ssrn.7354662) |
| 2026 | Event-based sentiment analysis of financial news using large language models: A comprehensive framework | Crossref |
| 2026 | Beyond polarity: Multi-dimensional LLM sentiment signals for WTI crude oil futures return prediction | arXiv 2603.11408 |
| 2026 | LLM-based vs. lexicon-based sentiment signals for tail-risk detection in meme stocks | arXiv 2607.24072 |
| 2026 | Retrieval-augmented few-shot LLMs for financial sentiment classification on social media | PeerJ CS |
| 2025 | Identifying representation bias in large language models used in financial sentiment analysis | IEEE CiFEr 2025 (Sabuncuoglu & Maple) |
| 2025 | Comparing LLMs for sentiment analysis in financial market news | arXiv 2510.15929 |
| 2025 | Comparative evaluation of embedding representations for financial news sentiment analysis | arXiv 2512.13749 |
| 2025 | FinDPO: Financial sentiment analysis for algorithmic trading through preference optimization of LLMs | arXiv 2507.18417 |
| 2025 | Fine-tuning of lightweight large language models for sentiment classification on heterogeneous financial text | arXiv 2512.00946 |
| 2024 | FinSentGPT: A universal financial sentiment engine? | International Review of Financial Analysis, 94, 103291 |
| 2024 | Finance-specific large language models: Advancing sentiment analysis and return prediction with Llama 2 | SSRN |
| 2024 | Designing heterogeneous LLM agents for financial sentiment analysis | arXiv 2401.05799 |
| 2025 | Interpretable aspect-based sentiment analysis of Bangla financial news using LLMs | IEEE ICCIT 2025 |
| 2026 | Empirical evaluation of language models for Arabic financial sentiment analysis | IJACSA 17(9) |

---

## Ghi chú về độ tin cậy và việc còn lại

- **Mức xác minh** được nêu ở Mục 1.4. Các con số là số do tác giả công bố; tôi chưa chạy lại bất kỳ thí nghiệm nào. Mức 1 là đọc có mục tiêu (tìm từ khóa và đọc các đoạn liên quan), không phải đọc từ đầu đến cuối.
- **Đã sửa so với bản trước nhờ đọc toàn văn:** (i) "độ chính xác" của Kirtac & Germano (2024) là dự đoán dấu lợi suất (nhãn từ lợi suất, chia ngẫu nhiên), không phải khớp nhãn người; (ii) số liệu Lopez-Lira & Tang được thay bằng bản 10/2025 (mẫu sau thời điểm cắt dữ liệu, Sharpe suy giảm); (iii) Bollen và cs. kiểm thử chỉ 15 ngày; (iv) Nguyen P. A. và cs. (2026) dùng tin tiếng Anh, nên không còn tính là FSA tiếng Việt; (v) Mishev và cs. dùng tập kết hợp PhraseBank + SemEval và chỉ số MCC; (vi) FiQA Task 1 có 529 + 774 mẫu và độ chính xác khía cạnh rất thấp; (vii) họ của các tác giả Việt Nam trong Nguyen S. T. và cs. (2021) và Nguyen P. A. và cs. (2026) theo thứ tự tên trong chính bài báo.
- **Mâu thuẫn chưa giải quyết:** số bài của Vu và cs. (2023) (gần 40.000 so với 2.738); hai con số cho GPT-4o zero-shot trong Shen & Zhang (2024).
- **Chưa làm được:** truy vấn trên Scopus/WoS/IEEE/ACM; đọc toàn văn từ đầu đến cuối; chạy lại thí nghiệm; đọc nội dung các mục trong Phụ lục B; xác minh Das & Chen (2007), Ding và cs. (2015) và Pham và cs. (2025) vượt quá tóm tắt/siêu dữ liệu. Với MDPI (Vu và cs.), máy chủ trả 403 và tôi không giả danh trình duyệt để vượt qua; nếu bạn có bản PDF hợp lệ, tôi sẽ đối chiếu.
- **Cần chuẩn hóa trước khi nộp:** tên tác giả Việt Nam trong ba tài liệu (Thanh và cs., Việt và cs., Vu và cs.) và dạng trích dẫn trong văn bản.
