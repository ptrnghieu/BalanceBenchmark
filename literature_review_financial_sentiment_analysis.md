# Tổng quan tài liệu về Phân tích cảm xúc trong tài chính (Financial Sentiment Analysis): bài toán, phương pháp, dữ liệu và bối cảnh tiếng Việt

## Tóm tắt

Phân tích cảm xúc tài chính (Financial Sentiment Analysis – FSA) thường được hiểu là phân loại văn bản tài chính thành tích cực, tiêu cực hoặc trung lập. Bài tổng quan này lập luận rằng cách hiểu đó quá hẹp. FSA bao gồm nhiều bài toán khác nhau (phân loại, chấm điểm, theo khía cạnh, theo đối tượng, theo sự kiện), nhiều loại nhãn (cảm xúc văn bản, tâm lý nhà đầu tư, tác động kỳ vọng lên giá), nhiều nguồn dữ liệu và nhiều mục tiêu ứng dụng. Một mô hình tốt trên benchmark cảm xúc chưa chắc hữu ích cho dự báo tài chính. Khoảng cách này càng đáng chú ý ở thị trường mới nổi và ngôn ngữ ít tài nguyên như tiếng Việt. Bài khảo sát giai đoạn 2000 đến nay theo cấu trúc: nền tảng khái niệm, taxonomy các bài toán, tiến hóa phương pháp, dữ liệu–gán nhãn–đánh giá, ứng dụng, thách thức, rồi đi riêng vào FSA tiếng Việt.

**Từ khóa:** phân tích cảm xúc, tài chính, taxonomy, FinBERT, mô hình ngôn ngữ lớn, tiếng Việt

---

## 1. Giới thiệu

### 1.1. Động lực và luận điểm trung tâm

Thị trường tài chính phản ứng với thông tin, và phần lớn thông tin đó ở dạng văn bản. Từ những năm 2000, một nhánh nghiên cứu chuyển văn bản thành chỉ báo định lượng về cảm xúc để kiểm tra mối liên hệ với lợi suất, biến động và khối lượng giao dịch.

Luận điểm trung tâm của bài như sau:

> FSA không chỉ là phân loại positive/negative/neutral. Nó gồm nhiều bài toán, nhiều loại nhãn, nhiều nguồn dữ liệu và nhiều mục tiêu downstream. Một mô hình tốt trên benchmark cảm xúc chưa chắc hữu ích cho dự báo tài chính, và khoảng cách này càng rõ ở ngôn ngữ ít tài nguyên như tiếng Việt.

Phân biệt xuyên suốt bài là giữa **cảm xúc của văn bản**, **tâm lý nhà đầu tư** và **tác động kỳ vọng lên giá** (xem Mục 2).

### 1.2. Câu hỏi nghiên cứu

| RQ | Câu hỏi | Mục tương ứng |
|---|---|---|
| RQ1 | FSA đã phát triển thế nào về bài toán, phương pháp và mô hình? | 3, 4 |
| RQ2 | Những tập dữ liệu, cách gán nhãn và giao thức đánh giá nào được dùng? | 5 |
| RQ3 | Cảm xúc tài chính được dùng trong các ứng dụng downstream ra sao? | 6 |
| RQ4 | Những thách thức và khoảng trống nghiên cứu chính là gì? | 7, 9 |
| RQ5 | FSA tiếng Việt đang ở mức nào so với nghiên cứu toàn cầu? | 8 |

### 1.3. Các khảo sát liên quan

Kearney và Liu (2014) tập trung vào cảm xúc văn bản trong tài chính; Loughran và McDonald (2016) khảo sát phân tích văn bản trong kế toán và tài chính; Xing và cs. (2018) khảo sát dự báo tài chính dựa trên ngôn ngữ tự nhiên; Nie và cs. (2024) khảo sát LLM cho các ứng dụng tài chính, trong đó phân tích cảm xúc là một mảng. Bài này khác ở chỗ tổ chức theo bài toán và loại nhãn, và dành riêng một phần cho tiếng Việt.

### 1.4. Phương pháp chọn tài liệu và giới hạn

Tài liệu được tìm qua tìm kiếm web theo tên công trình và chủ đề, rồi đối chiếu thông tin thư mục (tác giả, năm, tạp chí, trang) với trang kho lưu trữ hoặc cơ sở dữ liệu. Nhiều công trình chỉ được kiểm tra qua tóm tắt và trang thông tin, chưa đọc toàn văn. Các con số kết quả là số do tác giả công bố. **Đây chưa phải tổng quan hệ thống**: chưa có truy vấn xác định trước trên Scopus, Web of Science, IEEE Xplore, ACL Anthology hay ACM DL, chưa có tiêu chí đưa vào/loại ra, chưa có sơ đồ sàng lọc. Do đó bài có thể bỏ sót tài liệu, và các nhận định về "khoảng trống" chỉ có giá trị tương đối với tập tài liệu đã xem. Thời điểm chốt tìm kiếm là tháng 10/2026, nhưng phần lớn công trình về LLM trong bài thuộc giai đoạn 2023–2024; giai đoạn sau chưa được khảo sát và đó là hạn chế cần bổ sung. Bài ghi rõ công trình nào là bản thảo arXiv chưa được xác minh bình duyệt.

---

## 2. Nền tảng khái niệm

### 2.1. Ba khái niệm cần tách biệt

| Khái niệm | Câu hỏi | Ví dụ minh họa |
|---|---|---|
| **Cảm xúc văn bản** (textual sentiment) | Văn bản thể hiện sắc thái gì? | "Doanh thu giảm mạnh" mang sắc thái tiêu cực |
| **Tâm lý nhà đầu tư** (investor sentiment) | Nhà đầu tư lạc quan hay bi quan? | Chỉ số tâm lý tổng hợp từ nhiều nguồn |
| **Tác động kỳ vọng lên giá** (expected market impact) | Thông tin tốt hay xấu cho giá? | Tin cắt giảm chi phí có thể tăng giá dù sắc thái trung tính |

Ba khái niệm này không thể mặc định thay thế cho nhau. Chúng có quan hệ, nhưng một mô hình phân loại tốt khái niệm thứ nhất chưa chắc dự đoán được khái niệm thứ ba. Phân biệt này có ý nghĩa thực tế: Lopez-Lira và Tang (2023) yêu cầu mô hình đánh giá một tiêu đề là tốt, xấu hay trung lập **đối với giá cổ phiếu của công ty**, tức là nhắm vào khái niệm thứ ba chứ không chỉ sắc thái văn bản.

### 2.2. Cơ sở lý thuyết và bằng chứng ban đầu

Cơ sở lý thuyết nằm ở tài chính hành vi: giá có thể bị ảnh hưởng bởi tâm lý nhà đầu tư, không chỉ bởi yếu tố cơ bản. Tetlock (2007) đo mức bi quan của truyền thông từ chuyên mục "Abreast of the Market" trên Wall Street Journal bằng phân tích thành phần chính, giai đoạn 1984–1999. Mức bi quan cao đi kèm áp lực giảm giá rồi giá hồi về mức cơ bản, còn mức bi quan cực đoan (cao hoặc thấp) đi kèm khối lượng giao dịch lớn. Tác giả diễn giải kết quả phù hợp với mô hình có nhà giao dịch nhiễu và nhà giao dịch thanh khoản, và không phù hợp với việc xem nội dung truyền thông chỉ là đại diện cho thông tin cơ bản mới.

Antweiler và Frank (2004) phân tích hơn 1,5 triệu bài đăng trên bảng tin Yahoo! Finance, xét lợi suất, biến động, khối lượng và chênh lệch giá mua–bán. Các nguồn thứ cấp mô tả khả năng dự báo lợi suất là yếu; chi tiết này cần đối chiếu với bài gốc vì chưa truy cập toàn văn.

Kearney và Liu (2014) tổng hợp rằng cảm xúc văn bản liên hệ với hành vi ở cấp cá nhân, doanh nghiệp và thị trường, đồng thời chỉ ra các điểm đồng thuận và còn tranh luận.

---

## 3. Taxonomy các bài toán FSA

### 3.1. Khung phân loại

Phần lớn tổng quan sắp xếp theo phương pháp, nhưng câu hỏi trước tiên là FSA giải quyết những bài toán gì. Bảng dưới đây phân loại theo bài toán, kèm các công trình đã kiểm tra thư mục làm ví dụ.

| Bài toán | Mục tiêu | Công trình ví dụ (đã kiểm tra) | Ghi chú |
|---|---|---|---|
| Phân loại cảm xúc ở mức câu/văn bản | Gán nhãn positive/negative/neutral | Malo và cs. (2014); Das & Chen (2007) | Das & Chen làm ở mức bài đăng; Malo ở mức câu/cụm từ |
| Chấm điểm cảm xúc / cường độ | Cho điểm liên tục thay vì nhãn rời rạc | Araci (2019) báo cáo kết quả trên tác vụ chấm điểm của FiQA | Dạng hồi quy |
| Chỉ số cảm xúc cấp văn bản, tổng hợp | Tạo thước đo cảm xúc từ nhiều văn bản | Tetlock (2007); Loughran & McDonald (2011) | Đo bằng đếm từ/thành phần chính |
| Theo khía cạnh (ABSA) | Cảm xúc đối với một khía cạnh | FiQA (Maia và cs., 2018) nhắm đến aspect-based sentiment analysis | Chi tiết gán nhãn khía cạnh chưa xác minh từ toàn văn |
| Theo đối tượng (target-dependent) | Cảm xúc hướng đến một thực thể cụ thể | Lopez-Lira & Tang (2023): đánh giá tiêu đề đối với giá cổ phiếu của một công ty | Gần với bài toán này nhưng nhãn là tác động, không thuần sắc thái |
| Cảm xúc/tâm trạng chi tiết | Nhiều chiều tâm trạng thay vì phân cực | Bollen và cs. (2011): GPOMS với các chiều calm, alert, sure, vital, kind, happy | Dựa trên Twitter, không riêng văn bản tài chính |
| Theo sự kiện | Thái độ/tác động gắn với sự kiện | Ding và cs. (2015): trích sự kiện từ tin tức để dự báo giá | Thiên về dự báo giá hơn là phân loại cảm xúc |
| Lập trường (stance) | Lập trường đối với một chủ đề | Chưa có công trình nào được kiểm tra trong bài | Khoảng trống về bằng chứng, chưa kết luận là khoảng trống nghiên cứu |

Hai lưu ý:
- Ranh giới giữa các hàng không cứng. Một công trình có thể thuộc nhiều hàng, và phần phân loại ở đây là cách đọc của tôi dựa trên tóm tắt.
- Một số công trình (Ding và cs., 2015) nằm ở giao điểm giữa FSA và dự báo tài chính từ văn bản. Nên gọi chúng là *dự báo tài chính dựa trên văn bản* chứ không gọi là FSA thuần túy.

### 3.2. Vì sao cần phân biệt: ví dụ minh họa

Xét câu minh họa (do tôi đặt, không trích từ bộ dữ liệu nào): *"Công ty A báo lãi kỷ lục, trong khi công ty B thua lỗ nặng."*

- Phân loại cả câu: kết quả có thể là trung lập vì có cả thông tin tốt và xấu.
- Phân tích theo đối tượng: A tích cực, B tiêu cực.

Đây là hai bài toán khác nhau dù dùng cùng một câu. Tương tự với câu *"Doanh thu giảm nhưng biên lợi nhuận cải thiện đáng kể"*: nhãn phụ thuộc vào khía cạnh mà người gán nhãn hoặc mô hình chú ý, nên cần cân nhắc ABSA hoặc cho phép bất đồng giữa người gán nhãn (xem Mục 5.3).

Hệ quả cho tiếng Việt: tin tài chính thường nhắc nhiều doanh nghiệp và ngành trong cùng một bài, nên ABSA và target-dependent sentiment là hướng đáng quan tâm. Đây là suy luận của tôi, chưa có công trình tiếng Việt nào được kiểm tra để chứng minh.

---

## 4. Tiến hóa phương pháp

### 4.1. Từ điển (lexicon-based)

Loughran và McDonald (2011) phân tích 50.115 hồ sơ 10-K của các công ty Mỹ giai đoạn 1994–2008, và thấy phần lớn từ mà từ điển Harvard xếp là tiêu cực không mang nghĩa tiêu cực trong ngữ cảnh báo cáo tài chính (ví dụ *liability, tax, board, vice*). Họ xây từ điển tài chính riêng (danh sách từ tiêu cực và năm danh mục sắc thái khác) và cho thấy thước đo dựa trên từ điển này liên hệ rõ hơn với lợi suất quanh ngày nộp báo cáo, khối lượng giao dịch, biến động, gian lận và điểm yếu trọng yếu. Ưu điểm của cách tiếp cận này là minh bạch, rẻ, dễ tái lập; nhược điểm là bỏ qua ngữ cảnh, phủ định và cấu trúc câu. Malo và cs. (2014) nhấn mạnh rằng cảm xúc của câu có thể khác cảm xúc của từng từ, và đề xuất mô hình cấu trúc cụm từ cùng một từ điển tài chính mở rộng.

### 4.2. Học máy truyền thống

Das và Chen (2007) kết hợp nhiều bộ phân loại bằng bỏ phiếu để phân loại bài đăng trên bảng tin chứng khoán. Họ báo cáo độ chính xác tương đương các bộ phân loại Bayes phổ biến nhưng ít dương tính giả hơn, và việc gộp thông điệp theo thời gian và theo cổ phiếu cải thiện chỉ số cảm xúc, nhất là khi có tiếng lóng và nhập nhằng.

### 4.3. Học sâu

Ding và cs. (2015) trích sự kiện từ tin tức, biểu diễn bằng mạng tensor nơ-ron, rồi dùng mạng tích chập sâu để mô hình hóa ảnh hưởng ngắn và dài hạn lên giá. Họ báo cáo cải thiện khoảng 6% độ chính xác so với các baseline cho dự báo S&P 500 và cổ phiếu riêng lẻ, trên tin Reuters và Bloomberg. Như đã nêu ở Mục 3, công trình này là dự báo giá từ văn bản. Xing và cs. (2018) tổng quan nhóm nghiên cứu dự báo tài chính dựa trên ngôn ngữ tự nhiên ở giai đoạn trước khi Transformer phổ biến.

### 4.4. Mô hình tiền huấn luyện (BERT và biến thể tài chính)

Araci (2019) giới thiệu FinBERT, dựa trên BERT, xuất phát từ hai khó khăn là dữ liệu gán nhãn tài chính khan hiếm và từ vựng chuyên ngành. Tác giả báo cáo kết quả tốt nhất vào thời điểm đó trên FiQA (chấm điểm cảm xúc) và Financial PhraseBank, và cho biết mô hình vượt các phương pháp học máy trước đó dù dùng ít dữ liệu và chỉ tinh chỉnh một phần mô hình. Yang và cs. (2020) tiền huấn luyện một BERT khác (cũng tên FinBERT) trên văn bản giao tiếp tài chính và báo cáo vượt BERT miền tổng quát trên ba tác vụ phân loại cảm xúc tài chính; tác giả nói đây là BERT chuyên ngành tài chính đầu tiên được công bố. Mishev và cs. (2020) chạy hơn một trăm thí nghiệm trên các tập dữ liệu công khai do chuyên gia gán nhãn, đi từ từ điển tài chính đến Transformer; kết luận chính là biểu diễn theo ngữ cảnh vượt từ điển và bộ mã hóa cố định, còn Transformer rút gọn cho hiệu năng gần bản đầy đủ.

### 4.5. Mô hình ngôn ngữ lớn

Cần phân biệt ba cách dùng LLM, vì không phải công trình LLM nào cũng là FSA theo nghĩa truyền thống:

1. **LLM làm bộ chấm điểm tin tức, dùng làm tín hiệu**: Lopez-Lira & Tang (2023) yêu cầu ChatGPT đánh giá tiêu đề là tốt/xấu/trung lập đối với giá cổ phiếu, rồi xét tương quan với lợi suất sau đó. Họ báo cáo tương quan dương có ý nghĩa thống kê, các mô hình cơ bản hơn (GPT-1, GPT-2, BERT) không dự báo được chính xác, khả năng dự báo cao nhất ở mô hình mạnh hơn (GPT-4), và rõ hơn ở cổ phiếu nhỏ. Tác giả chính lưu ý trong phỏng vấn rằng tương quan rất nhỏ dù có ý nghĩa thống kê.
2. **LLM chuyên ngành tài chính**: BloombergGPT (Wu và cs., 2023) có 50 tỷ tham số, huấn luyện trên 363 tỷ token dữ liệu của Bloomberg cộng 345 tỷ token dữ liệu tổng quát; tác giả báo cáo vượt các mô hình cùng cỡ trên tác vụ tài chính. FinGPT (Yang và cs., 2023) theo hướng mã nguồn mở, nhấn mạnh quy trình dữ liệu và thích ứng nhẹ bằng LoRA.
3. **Khảo sát LLM tài chính**: Nie và cs. (2024) xếp cảm xúc là một trong các nhóm ứng dụng, cùng với tác vụ ngôn ngữ, chuỗi thời gian, suy luận và tác tử, và nêu các vấn đề mở như thiên lệch nhìn trước, ràng buộc pháp lý, ô nhiễm dữ liệu và khả năng diễn giải.

Công trình của Lopez-Lira & Tang thiên về dự báo lợi suất hơn là trích xuất cảm xúc thuần túy; BloombergGPT và FinGPT là mô hình nền đa tác vụ, trong đó cảm xúc chỉ là một tác vụ.

### 4.6. Phân tích so sánh

| Công trình | Dữ liệu | Bài toán | Phương pháp | Đánh giá | Kết quả chính (theo tác giả) |
|---|---|---|---|---|---|
| Loughran & McDonald (2011) | 10-K, 1994–2008 | Đo giọng điệu văn bản | Từ điển tài chính | Liên hệ với kết quả tài chính | Từ điển chuyên ngành cần thiết, Harvard gán sai nhiều từ |
| Das & Chen (2007) | Bài đăng bảng tin | Phân loại cảm xúc, chỉ số tổng hợp | Nhiều bộ phân loại, bỏ phiếu | Độ chính xác, dương tính giả | Ít dương tính giả hơn Bayes; gộp theo thời gian cải thiện chỉ số |
| Malo và cs. (2014) | Tin kinh tế, Financial PhraseBank | Cảm xúc câu/cụm từ | Mô hình cấu trúc cụm từ + từ điển mở rộng | Phân loại (chỉ số chưa xác minh) | Ngữ cảnh cụm từ quan trọng |
| Araci (2019) | Financial PhraseBank, FiQA | Phân loại và chấm điểm | FinBERT | Chưa xác minh chi tiết | Tiền huấn luyện miền tài chính hữu ích |
| Yang và cs. (2020) | Ba tác vụ cảm xúc tài chính | Phân loại | FinBERT tiền huấn luyện trên văn bản giao tiếp tài chính | Chưa xác minh chi tiết | Vượt BERT tổng quát |
| Mishev và cs. (2020) | Nhiều tập công khai | Phân loại | Từ điển → Transformer | So sánh hơn 100 thí nghiệm | Ngữ cảnh vượt từ điển; rút gọn gần bằng đầy đủ |
| Ding và cs. (2015) | Tin Reuters, Bloomberg | Dự báo giá từ sự kiện | Tensor nơ-ron + CNN | Độ chính xác dự báo | Khoảng +6% so với baseline |
| Lopez-Lira & Tang (2023) | Tiêu đề tin | Chấm điểm tin → lợi suất | ChatGPT/GPT-4 | Tương quan, lợi nhuận danh mục | Dương, nhỏ, rõ hơn ở cổ phiếu nhỏ |

Một số phân tích so sánh có thể rút ra, kèm giới hạn:

- **Hai FinBERT khác nhau.** Araci (2019) tinh chỉnh BERT cho cảm xúc tài chính và đánh giá trên FiQA và Financial PhraseBank; Yang và cs. (2020) tiền huấn luyện BERT trên văn bản giao tiếp tài chính và đánh giá trên ba tác vụ cảm xúc. Hai công trình khác nhau về ngữ liệu và tác vụ đánh giá, nên không thể so điểm trực tiếp. Chi tiết về ngữ liệu tiền huấn luyện và chỉ số cần đối chiếu với bài gốc.
- **Khi nào Transformer vượt từ điển?** Mishev và cs. (2020) cho thấy lợi thế của biểu diễn theo ngữ cảnh trên các tập có nhãn ở mức câu. Nhưng từ điển Loughran–McDonald được xây cho văn bản dài như 10-K và gắn trực tiếp với kết quả tài chính. Hai bối cảnh khác nhau, nên "Transformer thắng từ điển" chưa nên khái quát cho mọi nguồn dữ liệu và mọi mục tiêu.
- **Mâu thuẫn tiềm năng.** Bollen và cs. (2011) báo cáo độ chính xác 87,6% khi dự đoán chiều biến động DJIA, trong khi Lopez-Lira & Tang (2023) mô tả tương quan rất nhỏ. Hai công trình khác dữ liệu, thời kỳ và thiết lập, nên không so trực tiếp được; điều đáng ghi nhận là tín hiệu dự báo thường yếu hơn khi kiểm định chặt hơn.

---

## 5. Dữ liệu, gán nhãn và đánh giá

### 5.1. Nguồn dữ liệu và cảm xúc phụ thuộc nguồn

| Nguồn | Công trình ví dụ | Đặc điểm | Vấn đề |
|---|---|---|---|
| Báo cáo doanh nghiệp (10-K) | Loughran & McDonald (2011) | Ngôn ngữ chính thức, dài, nhiều thuật ngữ | Cảm xúc tinh tế, nhiều văn bản pháp lý lặp lại |
| Tin tức | Tetlock (2007); Ding và cs. (2015); Lopez-Lira & Tang (2023) | Ngôn ngữ biên tập | Cảm xúc có thể không biểu hiện trực tiếp; độ trễ so với giá |
| Bảng tin / mạng xã hội | Antweiler & Frank (2004); Das & Chen (2007); Bollen và cs. (2011) | Ngắn, chủ quan, tiếng lóng | Nhiễu, spam, khả năng thao túng |
| Báo cáo phân tích, họp báo kết quả | Chưa có công trình được kiểm tra trong bài | – | Khoảng trống bằng chứng của bài này |

Hệ quả: một mô hình huấn luyện trên Financial PhraseBank không mặc nhiên hoạt động tốt trên StockTwits hay báo cáo thường niên. Đó là vấn đề tổng quát hóa giữa các nguồn (cross-source generalization) và thích ứng miền. Trong số công trình đã kiểm tra, tôi chưa thấy công trình nào đánh giá trực tiếp vấn đề này; khẳng định "chưa ai làm" cần kiểm tra bằng tìm kiếm hệ thống.

### 5.2. Bộ dữ liệu chuẩn

- **Financial PhraseBank** (Malo và cs., 2014): khoảng 5.000 cụm từ/câu từ tin kinh tế, gán nhãn bởi chuyên gia tài chính (theo mô tả thứ cấp; cần đối chiếu số liệu và quy trình với bài gốc).
- **FiQA** (Maia và cs., 2018): thử thách mở tại The Web Conference 2018 gồm phân tích cảm xúc theo khía cạnh và hỏi đáp dựa trên quan điểm. Dữ liệu thu thập từ StackExchange, Reddit và StockTwits giai đoạn 2009–2017. Một khảo sát (arXiv 2402.02315) mô tả phần FiQA-SA có 1.173 bài đăng từ tiêu đề và vi blog.

Cả hai chủ yếu là tiếng Anh, quy mô nhỏ, nên điểm cao trên benchmark chưa chắc chuyển sang môi trường thực.

### 5.3. Gán nhãn và kiểm soát chất lượng

Trong phạm vi tài liệu đã kiểm tra, thông tin cụ thể về quy trình gán nhãn rất hạn chế (Financial PhraseBank do chuyên gia gán nhãn; bộ CafeF tiếng Việt gán nhãn "với sự giúp đỡ của chuyên gia"). Vì vậy phần này chủ yếu đặt ra khung câu hỏi cần trả lời khi đánh giá một bộ dữ liệu, không khẳng định thực tế của từng bộ.

1. **Độ chi tiết**: gán nhãn ở mức câu, đoạn, bài hay thực thể?
2. **Định nghĩa nhãn**: nhãn theo sắc thái người viết, theo thái độ nhà đầu tư, hay theo tác động kỳ vọng lên giá? (Đây là ba khái niệm ở Mục 2.1.) Ví dụ: "Công ty công bố giảm 20% chi phí vận hành" có thể là tích cực nếu xét hiệu quả kinh doanh, nhưng chưa chắc nếu xét sắc thái người viết hay phản ứng thị trường.
3. **Chuyên môn người gán nhãn**: người thường hay chuyên gia tài chính?
4. **Mức đồng thuận**: các người gán nhãn có đồng ý với nhau không? Chỉ số đồng thuận của từng bộ dữ liệu nêu trên chưa được xác minh trong bài này.

Câu hỏi mở: có nên ép mỗi văn bản vào một nhãn duy nhất, hay biểu diễn bất đồng và độ bất định giữa người gán nhãn? Tôi chưa có bằng chứng thực nghiệm về mức bất đồng trong FSA, nên đây là hướng cần khảo sát, không phải kết luận.

### 5.4. Giao thức đánh giá

Khung dưới đây là đề xuất tổ chức, không phải thống kê các công trình đã khảo sát:

| Mục tiêu | Chỉ số / giao thức thường dùng |
|---|---|
| Phân loại cảm xúc | Accuracy, Macro-F1, Precision, Recall |
| Chấm điểm cảm xúc (hồi quy) | MAE, RMSE, tương quan Pearson/Spearman |
| Dự báo tài chính | Độ chính xác chiều, MAE, RMSE, Sharpe |
| Đánh giá giao dịch | Lợi nhuận tích lũy, chi phí giao dịch, mức sụt giảm tối đa |

Về cách chia dữ liệu: ngẫu nhiên, phân tầng, **theo thời gian**, walk-forward, và đánh giá ngoài miền. Chia theo thời gian đặc biệt quan trọng. Nếu huấn luyện trên dữ liệu muộn hơn kiểm thử, hoặc tin gần trùng lặp xuất hiện ở cả hai tập, kết quả không phản ánh khả năng triển khai. Điều này gắn trực tiếp với thiên lệch nhìn trước ở Mục 7. Các thiết lập đánh giá cụ thể của từng công trình trong bảng Mục 4.6 phần lớn chưa được xác minh từ toàn văn.

---

## 6. Ứng dụng

Bài tách ứng dụng thành ba nhóm, vì mỗi nhóm trả lời một câu hỏi khác nhau và bằng chứng của nhóm này không suy ra nhóm kia.

| Nhóm | Câu hỏi | Công trình ví dụ |
|---|---|---|
| **Đo lường cảm xúc** | Văn bản thể hiện tâm lý gì? | Loughran & McDonald (2011); Das & Chen (2007); Malo và cs. (2014) |
| **Phân tích phản ứng thị trường** | Thị trường phản ứng thế nào với thông tin/cảm xúc? | Tetlock (2007); Antweiler & Frank (2004); Loughran & McDonald (2011) |
| **Ứng dụng dự báo** | Cảm xúc có làm tín hiệu dự báo giá, biến động, giao dịch? | Bollen và cs. (2011); Ding và cs. (2015); Lopez-Lira & Tang (2023) |

Các hệ quả logic:

- Đo cảm xúc tốt không chứng minh cảm xúc dự báo được giá.
- Tương quan giữa cảm xúc và lợi suất không chứng minh khả năng dự báo ngoài mẫu.
- Dự báo được lợi suất không có nghĩa chiến lược giao dịch có lợi nhuận sau chi phí.

**Về các con số hiệu năng đã nêu**, mỗi con số cần đọc kèm thiết lập:
- Bollen và cs. (2011): độ chính xác 87,6% khi dự đoán chiều DJIA hằng ngày (số do tác giả công bố; mẫu và thiết lập đánh giá chưa được tôi xác minh từ toàn văn).
- Ding và cs. (2015): cải thiện khoảng 6% so với baseline trên dữ liệu Reuters/Bloomberg; thiết lập cụ thể chưa xác minh.
- Lopez-Lira & Tang (bản 2024): lợi nhuận bình quân ngày khoảng 9 điểm cơ bản ở vị thế mua và 29 điểm cơ bản ở vị thế bán, trong mẫu nghiên cứu của họ; chưa xác minh việc có tính đầy đủ chi phí giao dịch.

Phần quản trị rủi ro và hỗ trợ ra quyết định hiện được thảo luận chủ yếu trong các khảo sát LLM (Nie và cs., 2024; Yang và cs., 2023). Tôi chưa có bằng chứng thực nghiệm đủ mạnh trong tập tài liệu đã kiểm tra.

---

## 7. Thách thức và vấn đề mở

**(1) Thiên lệch nhìn trước và rò rỉ thời gian.** LLM được huấn luyện trên dữ liệu có thể đã chứa thông tin về diễn biến giá sau tin đang kiểm thử. Glasserman và Lin (2023) dùng GPT-3.5 trên tiêu đề tin của các công ty S&P 500, so sánh tiêu đề gốc với tiêu đề đã ẩn danh. Trong mẫu, phiên bản ẩn danh cho kết quả tốt hơn, và họ diễn giải rằng "hiệu ứng xao nhãng" (kiến thức chung về công ty làm nhiễu phán đoán) lấn át thiên lệch nhìn trước; ngoài mẫu thì thiên lệch nhìn trước không phải mối lo, dù sự xao nhãng vẫn có thể xảy ra. Đây là bản thảo arXiv, tôi chưa tìm thấy bản bình duyệt.

**(2) Tái lập và chi phí.** BloombergGPT không công khai (theo bình luận trên trang Hugging Face, chưa xác minh nguồn chính thức), còn kết quả của API thương mại thay đổi theo phiên bản. Các hướng mở như FinGPT và Transformer rút gọn (Mishev và cs., 2020) là phương án giảm chi phí.

**(3) Ý nghĩa kinh tế so với ý nghĩa thống kê.** Tương quan nhỏ nhưng có ý nghĩa thống kê (Lopez-Lira & Tang, 2023) và kết quả ấn tượng trên mẫu hẹp (Bollen và cs., 2011) cho thấy cần kiểm định ngoài mẫu, tính chi phí giao dịch và kiểm tra tính bền vững qua các giai đoạn thị trường.

**(4) Cảm xúc không bằng tác động lên giá.** Ba bài toán cần tách: mô hình hiểu cảm xúc văn bản; mô hình đánh giá thông tin tốt hay xấu cho một doanh nghiệp; mô hình dự đoán phản ứng thực tế của thị trường. Chúng có quan hệ nhưng không đồng nhất, và thị trường còn phụ thuộc vào kỳ vọng trước đó và thông tin đã phản ánh vào giá.

**(5) Tính chủ quan của nhãn.** Hai chuyên gia có thể diễn giải cùng một thông tin theo hai hướng (xem ví dụ doanh thu giảm nhưng biên lợi nhuận tăng ở Mục 3.2).

**(6) Tính diễn giải.** Từ điển minh bạch nhưng thô; mô hình sâu chính xác hơn nhưng khó giải thích, điều quan trọng với tổ chức chịu yêu cầu tuân thủ.

**(7) Độ tin cậy của LLM khi gán nhãn.** Tính ổn định, nhất quán và ảo giác khi LLM gán nhãn là câu hỏi hợp lý, nhưng trong tập tài liệu đã kiểm tra tôi chưa có công trình nào đo trực tiếp việc này (Glasserman & Lin, 2023, mô tả sự "quá tự tin" của GPT-3.5, là chi tiết liên quan duy nhất).

---

## 8. FSA tiếng Việt

Phần này ghi nhận những gì đã tìm được; **bằng chứng hiện còn mỏng**, nên không đủ để khẳng định toàn bộ bức tranh FSA tiếng Việt. Mở rộng cần một đợt tìm kiếm có hệ thống riêng.

### 8.1. Bức tranh nghiên cứu

Từ một lượt tìm kiếm, tôi ghi nhận ba nhóm công trình:

- Một nghiên cứu đăng trên *International Journal of Financial Studies* (2023, 11(3), 101) về cảm xúc trích xuất từ tin tức và phản ứng thị trường chứng khoán Việt Nam, dùng PhoBERT để phân loại. Theo mô tả tìm được, bộ huấn luyện gồm gần 40.000 bài từ các trang tài chính–kinh tế; kết quả là phản ứng giá tức thời nhỏ nhưng nhà đầu tư có xu hướng phản ứng thái quá với tin tốt và xấu. Danh sách tác giả và chi tiết phương pháp chưa xác minh.
- Một nghiên cứu trong lĩnh vực ngân hàng xây dựng ngữ liệu 12.000 mẫu gán nhãn và tinh chỉnh PhoBERT, ViT5, BARTPho, báo cáo cải thiện độ chính xác 7,15% (theo mô tả tìm được).
- Một bản thảo (nhắc đến trong kết quả tìm kiếm, chưa xác minh) dùng PhoBERT gán nhãn tin tài chính rồi kiểm định Granger và mô hình VAR ngưỡng với giá cổ phiếu một tập đoàn giai đoạn 2018–2023.

Thị trường/lĩnh vực: chứng khoán và ngân hàng. Bài toán: chủ yếu phân loại cảm xúc ba lớp và liên hệ với giá.

### 8.2. Bộ dữ liệu tiếng Việt

| Bộ dữ liệu | Nguồn | Quy mô | Nhãn | Công khai? | Thông tin còn thiếu |
|---|---|---|---|---|---|
| Tiêu đề CafeF (GitHub, 209sontung) | CafeF.vn | 1.000 tiêu đề | 3 lớp: 187 tiêu cực, 248 không tác động, 565 tích cực | Có (kho GitHub) | Thời gian thu thập, quy trình gán nhãn, đồng thuận |
| Ngữ liệu IJFS (2023) | Trang tài chính–kinh tế | Gần 40.000 bài (bộ huấn luyện) | Chưa xác minh | Chưa xác nhận | Có gán nhãn không; cách gán nhãn |
| Ngữ liệu ngân hàng (VJS) | Lĩnh vực ngân hàng | 12.000 mẫu | Có gán nhãn | Dường như chưa công khai | Nguồn, nhãn, đơn vị gán nhãn |

Bộ CafeF mất cân bằng lớp (khoảng 56,5% tích cực), và độ chính xác 93% là số tự báo cáo trên bộ nhỏ, nên không thể xem là benchmark.

### 8.3. Thách thức đặc thù ngôn ngữ (giả thuyết cần kiểm chứng)

Các điểm sau là câu hỏi cần khảo sát. Tôi chưa có bài nào để khẳng định chúng thực sự là khó khăn đặc thù của tiếng Việt, nên không nêu như sự thật:

- Từ ghép và phân đoạn từ ảnh hưởng thế nào đến bộ tách từ.
- Từ đa nghĩa trong ngữ cảnh tài chính.
- Thuật ngữ tài chính Việt–Anh và trộn mã (code-switching).
- Viết tắt, mã chứng khoán và tên doanh nghiệp.
- Tiếng lóng trên diễn đàn chứng khoán.
- Phủ định, mỉa mai và diễn đạt gián tiếp.

### 8.4. Các mô hình đã được nghiên cứu

| Mô hình | Có bằng chứng trong bài này? |
|---|---|
| PhoBERT | Có (nghiên cứu IJFS 2023; nghiên cứu ngân hàng; bản thảo) |
| ViT5, BARTPho | Có (nghiên cứu ngân hàng) |
| ML truyền thống với TF-IDF | Chưa có |
| XLM-R, mBERT | Chưa có |
| LLM với prompt tài chính | Chưa có |

"Chưa có" nghĩa là tôi chưa tìm thấy trong lượt tìm kiếm này, chứ không có nghĩa là chưa ai nghiên cứu.

### 8.5. Ứng dụng

Các ứng dụng đã thấy: liên hệ cảm xúc tin tức với phản ứng giá. Các hướng như cảm xúc theo doanh nghiệp hoặc ngành, phân tích theo sự kiện, chỉ số tâm lý thị trường, cảm xúc khách hàng ngân hàng, dự báo lợi suất và biến động chưa có bằng chứng cụ thể trong bài, và là phần cần tìm hiểu để đánh giá liệu nghiên cứu tiếng Việt có tập trung quá nhiều vào phân loại mà chưa khai thác ứng dụng downstream.

### 8.6. So với FSA toàn cầu

So với tiếng Anh, tập tài liệu tiếng Việt đã tìm được nhỏ hơn nhiều và thiếu một benchmark công khai có quy trình gán nhãn rõ ràng như Financial PhraseBank. Nhận định này giới hạn trong lượt tìm kiếm của bài.

---

## 9. Khoảng trống nghiên cứu và hướng tương lai

| Khoảng trống | Vấn đề chưa giải quyết | Bằng chứng trong bài | Tiềm năng với tiếng Việt |
|---|---|---|---|
| Tổng quát hóa giữa các nguồn | Mô hình có chuyển được giữa tin tức, báo cáo và mạng xã hội không? | Chưa thấy công trình đánh giá trực tiếp (Mục 5.1) | Cao |
| Độ bền theo thời gian | Mô hình có ổn định qua các giai đoạn thị trường không? | Gián tiếp qua Mục 7(1), 7(3) | Cao |
| Cảm xúc chi tiết | Phân cực ba lớp có đủ không? | Bollen và cs. (2011) dùng đa chiều, nhưng ngoài tài chính thuần | Trung bình |
| Cảm xúc theo đối tượng/khía cạnh | Cảm xúc hướng đến thực thể nào? | FiQA nhắm ABSA; chưa thấy kết quả tiếng Việt | Cao |
| Bất đồng khi gán nhãn | Cảm xúc tài chính có nhất quán giữa người gán nhãn không? | Chưa có dữ liệu thực nghiệm (Mục 5.3) | Cao |
| Cảm xúc văn bản so với tác động thị trường | Cảm xúc ngôn ngữ có phản ánh tác động kinh tế không? | Mục 2.1, 7(4) | Cao |
| Độ tin cậy của LLM | LLM có nhất quán, ít ảo giác khi gán nhãn không? | Rất ít (Mục 7(7)) | Trung bình |
| Đánh giá không rò rỉ thời gian | Backtest LLM không bị nhìn trước | Glasserman & Lin (2023) | Cao |

Hai hướng cần ưu tiên trước khi đo bằng mô hình: (1) xây benchmark tiếng Việt công khai, có hướng dẫn gán nhãn và mức đồng thuận, và (2) tách rõ nhãn cảm xúc văn bản với nhãn tác động lên giá. Các hướng về mô hình nhẹ và đa phương thức đáng làm nhưng cần xuất phát từ khoảng trống bằng chứng chứ không từ giải pháp kỹ thuật.

---

## 10. Kết luận

Hai thập kỷ qua, FSA đi từ đếm từ trong từ điển, qua học máy và học sâu, đến Transformer chuyên ngành và LLM. Điểm cốt lõi của bài không nằm ở thứ tự thời gian đó, mà ở việc FSA gồm nhiều bài toán và nhiều loại nhãn, và các mục tiêu đo cảm xúc, phân tích phản ứng thị trường và dự báo cần được tách bạch. Bằng chứng về khả năng dự báo thị trường nhìn chung dương nhưng khiêm tốn, chủ yếu từ mẫu hạn chế và tiếng Anh. Với tiếng Việt, nhu cầu cấp thiết nhất là dữ liệu chuẩn mở, quy trình gán nhãn minh bạch và đánh giá chặt chẽ.

---

## Tài liệu tham khảo (APA 7)

Antweiler, W., & Frank, M. Z. (2004). Is all that talk just noise? The information content of Internet stock message boards. *The Journal of Finance, 59*(3), 1259–1294.

Araci, D. (2019). *FinBERT: Financial sentiment analysis with pre-trained language models*. arXiv:1908.10063. https://arxiv.org/abs/1908.10063

Bollen, J., Mao, H., & Zeng, X. (2011). Twitter mood predicts the stock market. *Journal of Computational Science, 2*(1), 1–8. (Bản tiền ấn: arXiv:1010.3003)

Das, S. R., & Chen, M. Y. (2007). Yahoo! for Amazon: Sentiment extraction from small talk on the web. *Management Science, 53*(9), 1375–1388. https://doi.org/10.1287/mnsc.1070.0704

Ding, X., Zhang, Y., Liu, T., & Duan, J. (2015). Deep learning for event-driven stock prediction. *Proceedings of the 24th International Joint Conference on Artificial Intelligence (IJCAI)*, 2327–2333.

Glasserman, P., & Lin, C. (2023). *Assessing look-ahead bias in stock return predictions generated by GPT sentiment analysis*. arXiv:2309.17322. https://arxiv.org/abs/2309.17322

Kearney, C., & Liu, S. (2014). Textual sentiment in finance: A survey of methods and models. *International Review of Financial Analysis, 33*, 171–185. https://doi.org/10.1016/j.irfa.2014.02.006

Lopez-Lira, A., & Tang, Y. (2023). *Can ChatGPT forecast stock price movements? Return predictability and large language models*. arXiv:2304.07619. https://arxiv.org/abs/2304.07619

Loughran, T., & McDonald, B. (2011). When is a liability not a liability? Textual analysis, dictionaries, and 10-Ks. *The Journal of Finance, 66*(1), 35–65.

Loughran, T., & McDonald, B. (2016). Textual analysis in accounting and finance: A survey. *Journal of Accounting Research, 54*(4), 1187–1230. https://doi.org/10.1111/1475-679X.12123

Maia, M., Handschuh, S., Freitas, A., Davis, B., McDermott, R., Zarrouk, M., & Balahur, A. (2018). WWW'18 open challenge: Financial opinion mining and question answering. *Companion Proceedings of The Web Conference 2018*, 1941–1942. https://doi.org/10.1145/3184558.3192301

Malo, P., Sinha, A., Korhonen, P., Wallenius, J., & Takala, P. (2014). Good debt or bad debt: Detecting semantic orientations in economic texts. *Journal of the Association for Information Science and Technology, 65*(4), 782–796. https://doi.org/10.1002/asi.23062

Mishev, K., Gjorgjevikj, A., Vodenska, I., Chitkushev, L. T., & Trajanov, D. (2020). Evaluation of sentiment analysis in finance: From lexicons to transformers. *IEEE Access, 8*, 131662–131682. https://doi.org/10.1109/ACCESS.2020.3009626

Nie, Y., et al. (2024). *A survey of large language models for financial applications: Progress, prospects and challenges*. arXiv:2406.11903. https://arxiv.org/abs/2406.11903 *(danh sách tác giả đầy đủ cần bổ sung từ bài gốc)*

Tetlock, P. C. (2007). Giving content to investor sentiment: The role of media in the stock market. *The Journal of Finance, 62*(3), 1139–1168. https://doi.org/10.1111/j.1540-6261.2007.01232.x

Wu, S., Irsoy, O., Lu, S., et al. (2023). *BloombergGPT: A large language model for finance*. arXiv:2303.17564. https://arxiv.org/abs/2303.17564 *(bổ sung đủ tác giả theo bài gốc)*

Xing, F. Z., Cambria, E., & Welsch, R. E. (2018). Natural language based financial forecasting: A survey. *Artificial Intelligence Review, 50*(1), 49–73. https://doi.org/10.1007/s10462-017-9588-9

Yang, H., Liu, X.-Y., & Wang, C. D. (2023). *FinGPT: Open-source financial large language models*. arXiv:2306.06031. https://arxiv.org/abs/2306.06031

Yang, Y., Uy, M. C. S., & Huang, A. (2020). *FinBERT: A pretrained language model for financial communications*. arXiv:2006.08097. https://arxiv.org/abs/2006.08097

*Nguồn tiếng Việt / thị trường Việt Nam (cần xác minh trước khi trích chính thức):*

- [Tác giả cần xác minh]. (2023). Sentiments extracted from news and stock market reactions in Vietnam. *International Journal of Financial Studies, 11*(3), 101.
- 209sontung. (không rõ năm). *Vietnamese stock article classification* [Kho mã nguồn GitHub]. https://github.com/209sontung/Vietnamese-stock-article-classification
- Nghiên cứu tinh chỉnh PhoBERT/ViT5/BARTPho cho lĩnh vực ngân hàng, *Vietnam Journal of Science (VJS)*. [Tên, tác giả, năm cần xác minh]
- Bản thảo dùng PhoBERT và kiểm định Granger/VAR ngưỡng với giá cổ phiếu 2018–2023. [Nguồn, tác giả, tình trạng bình duyệt cần xác minh]

---

## Ghi chú về độ tin cậy và việc còn lại

- Thông tin thư mục các bài chính đã được đối chiếu với trang kho lưu trữ hoặc cơ sở dữ liệu, nhưng **chưa đọc toàn văn** hầu hết các bài. Số liệu là số do tác giả công bố.
- Taxonomy ở Mục 3 là cách đọc của tôi từ tóm tắt; cần đối chiếu từng công trình với toàn văn trước khi dùng chính thức. Hàng "lập trường" và "báo cáo phân tích/họp báo kết quả" ghi nhận chỗ chưa có công trình nào được kiểm tra, không phải kết luận rằng chưa có nghiên cứu.
- Chưa thực hiện: truy vấn có hệ thống trên các cơ sở dữ liệu học thuật, sơ đồ sàng lọc, khảo sát nghiên cứu 2024 trở đi, và khảo sát đầy đủ FSA tiếng Việt (Mục 8).
- Các mục "cần xác minh" ở phần tài liệu tham khảo cần được bổ sung trước khi nộp hoặc đăng.
