# Tổng quan tài liệu về Phân tích cảm xúc trong tài chính (Financial Sentiment Analysis): từ từ điển đến mô hình ngôn ngữ lớn

## Tóm tắt

Phân tích cảm xúc tài chính (Financial Sentiment Analysis – FSA) là bài toán xác định thái độ, quan điểm hoặc sắc thái (tích cực, tiêu cực, trung lập) trong các văn bản liên quan đến tài chính, như tin tức, báo cáo thường niên, bài đăng mạng xã hội và diễn đàn đầu tư. Bài tổng quan này khảo sát tài liệu giai đoạn 2000 đến nay theo ba trục: (1) phương pháp, từ từ điển, học máy, học sâu đến mô hình ngôn ngữ lớn (LLM); (2) dữ liệu và nguồn văn bản; (3) ứng dụng, chủ yếu là dự báo thị trường và nghiên cứu tài chính thực nghiệm. Bài cũng tóm tắt các bộ dữ liệu chuẩn, các thách thức còn tồn tại và hướng nghiên cứu tiếp theo, trong đó có bối cảnh tiếng Việt. Một xu hướng xuyên suốt là mức độ hiểu ngữ cảnh của mô hình tăng dần, kéo theo những vấn đề mới như thiên lệch nhìn trước (look-ahead bias), khả năng tái lập và tính diễn giải.

**Từ khóa:** phân tích cảm xúc, tài chính, xử lý ngôn ngữ tự nhiên, FinBERT, mô hình ngôn ngữ lớn, dự báo thị trường chứng khoán

---

## 1. Giới thiệu

Thị trường tài chính phản ứng với thông tin, và phần lớn thông tin đó ở dạng văn bản. Nhà đầu tư đọc tin tức, báo cáo doanh nghiệp, nhận định của chuyên gia và thảo luận trên mạng. Từ những năm 2000, một nhánh nghiên cứu phát triển nhằm chuyển các văn bản này thành chỉ báo định lượng về cảm xúc, để kiểm tra xem cảm xúc có liên quan đến lợi suất, biến động hay khối lượng giao dịch hay không.

Phân tích cảm xúc tài chính khác với phân tích cảm xúc đại chúng (ví dụ đánh giá phim hoặc sản phẩm) ở ít nhất ba điểm. Thứ nhất, từ vựng mang nghĩa chuyên ngành: một từ trung tính trong đời sống có thể mang sắc thái khác trong báo cáo tài chính. Thứ hai, cảm xúc của văn bản không đồng nghĩa với tác động lên giá. Một tin "công ty cắt giảm nhân sự" có thể làm giá tăng. Thứ ba, nhãn dữ liệu đắt đỏ vì cần chuyên gia tài chính gán nhãn (Malo và cs., 2014).

Mục tiêu của bài là cung cấp bức tranh có hệ thống về sự phát triển của lĩnh vực, chỉ ra điểm mạnh và hạn chế của từng nhóm phương pháp, và xác định khoảng trống nghiên cứu. Một số khảo sát trước đây đã bao quát từng phần của chủ đề: Kearney và Liu (2014) tập trung vào cảm xúc văn bản trong tài chính, Loughran và McDonald (2016) tổng quan phân tích văn bản trong kế toán và tài chính, Xing và cs. (2018) khảo sát dự báo tài chính dựa trên ngôn ngữ tự nhiên, còn Nie và cs. (2024) khảo sát LLM trong các ứng dụng tài chính, trong đó phân tích cảm xúc là một mảng.

**Phương pháp tìm kiếm và giới hạn.** Các tài liệu trong bài được tìm qua tìm kiếm web theo tên công trình và chủ đề, rồi đối chiếu thông tin thư mục (tác giả, năm, tạp chí, trang) với trang kho lưu trữ hoặc cơ sở dữ liệu. Nhiều công trình chỉ được kiểm tra qua tóm tắt và trang thông tin, không đọc toàn văn. Vì vậy bài **không trích số liệu chi tiết** ngoài những gì tóm tắt công bố, và các con số về độ chính xác do tác giả gốc tự báo cáo. Đây không phải là một tổng quan hệ thống theo chuẩn PRISMA, nên có thể bỏ sót tài liệu.

---

## 2. Nền tảng: vì sao cảm xúc văn bản quan trọng với tài chính

Cơ sở lý thuyết của lĩnh vực này nằm ở tài chính hành vi: giá có thể bị ảnh hưởng bởi tâm lý nhà đầu tư, không chỉ bởi các yếu tố cơ bản. Tetlock (2007) là một nghiên cứu nền tảng. Ông đo mức độ bi quan của truyền thông từ chuyên mục "Abreast of the Market" trên Wall Street Journal bằng phân tích thành phần chính, trong giai đoạn 1984–1999. Kết quả cho thấy mức bi quan cao đi kèm áp lực giảm giá, sau đó giá hồi về mức cơ bản, và mức bi quan cực đoan (cao hoặc thấp) đi kèm khối lượng giao dịch lớn. Tác giả diễn giải kết quả phù hợp với các mô hình có nhà giao dịch nhiễu (noise traders) và nhà giao dịch thanh khoản, và không phù hợp với việc xem nội dung truyền thông chỉ là đại diện cho thông tin cơ bản mới.

Trước đó, Antweiler và Frank (2004) phân tích hơn 1,5 triệu bài đăng trên bảng tin Yahoo! Finance để xem liệu "những cuộc nói chuyện" này có chứa thông tin về lợi suất, biến động, khối lượng giao dịch hay chênh lệch giá mua–bán. Các nguồn thứ cấp mô tả khả năng dự báo lợi suất là yếu, trong khi mối liên hệ với biến động và khối lượng rõ hơn. Chi tiết này cần đối chiếu với bài gốc vì tôi chưa truy cập toàn văn.

Hai công trình trên đặt ra khung hỏi chung cho cả lĩnh vực: đo cảm xúc thế nào, từ nguồn nào, và cảm xúc đó có mang thông tin hay chỉ là nhiễu.

---

## 3. Phương pháp tiếp cận

### 3.1. Phương pháp dựa trên từ điển (lexicon-based)

Cách làm đơn giản nhất là đếm từ: gán mỗi từ vào một danh mục (tích cực, tiêu cực...) rồi tính tỷ lệ trong văn bản. Trong thời kỳ đầu, nhiều nghiên cứu dùng từ điển tổng quát như Harvard General Inquirer. Loughran và McDonald (2011) chỉ ra vấn đề của cách làm này: khi phân tích 50.115 hồ sơ 10-K của các công ty Mỹ giai đoạn 1994–2008, họ thấy phần lớn các từ mà từ điển Harvard xếp là tiêu cực không mang nghĩa tiêu cực trong ngữ cảnh báo cáo tài chính. Ví dụ các từ như *liability*, *tax*, *board*, *vice* xuất hiện thường xuyên chỉ để nêu tên đối tượng hoặc chức danh. Từ đó họ xây dựng từ điển tài chính riêng (danh sách từ tiêu cực và năm danh mục sắc thái khác) và cho thấy các thước đo dựa trên từ điển này liên hệ rõ hơn với lợi suất quanh ngày nộp báo cáo, khối lượng giao dịch, biến động, gian lận và điểm yếu trọng yếu. Từ điển Loughran–McDonald từ đó trở thành chuẩn tham chiếu trong nghiên cứu tài chính thực nghiệm.

Ưu điểm của phương pháp từ điển là minh bạch, rẻ, dễ tái lập và dễ diễn giải. Nhược điểm là bỏ qua ngữ cảnh: phủ định, so sánh, mỉa mai và cấu trúc câu. Malo và cs. (2014) nhấn mạnh điểm này khi cho rằng cảm xúc của một câu có thể khác với cảm xúc của từng từ riêng lẻ, và đề xuất một mô hình cấu trúc cụm từ để nắm bắt cảm xúc theo ngữ cảnh, kèm một từ điển tài chính mở rộng và bộ cụm từ được chuyên gia gán nhãn.

### 3.2. Học máy truyền thống

Làn sóng thứ hai dùng bộ phân loại học máy trên đặc trưng túi từ (bag-of-words). Das và Chen (2007) xây dựng bộ phân loại cảm xúc cho các bài đăng trên bảng tin chứng khoán bằng cách kết hợp nhiều bộ phân loại qua cơ chế bỏ phiếu. Họ báo cáo độ chính xác tương đương các bộ phân loại Bayes phổ biến nhưng ít dương tính giả hơn, và việc gộp thông điệp theo thời gian và theo cổ phiếu cải thiện chỉ số cảm xúc, nhất là khi có tiếng lóng và nhập nhằng. Họ cũng tìm thấy mối liên hệ giữa cảm xúc đăng tải về nhóm công nghệ với mức chỉ số, khối lượng và biến động.

Hạn chế của hướng này là phụ thuộc vào kỹ thuật tạo đặc trưng thủ công và dữ liệu gán nhãn, đồng thời vẫn khó xử lý ngữ cảnh dài.

### 3.3. Học sâu và biểu diễn từ

Khi học sâu phát triển, các nghiên cứu chuyển sang biểu diễn phân tán (word embeddings) và mạng nơ-ron. Ding và cs. (2015) là ví dụ tiêu biểu: họ trích xuất "sự kiện" từ tin tức, biểu diễn thành vectơ bằng mạng tensor nơ-ron, rồi dùng mạng tích chập sâu để mô hình hóa ảnh hưởng ngắn hạn và dài hạn của các sự kiện lên giá. Họ báo cáo cải thiện khoảng 6% độ chính xác so với các baseline trước đó, cho cả dự báo chỉ số S&P 500 và cổ phiếu riêng lẻ, trên dữ liệu tin tức Reuters và Bloomberg. Công trình này nghiêng về dự báo giá từ văn bản hơn là phân loại cảm xúc thuần túy, nhưng minh họa việc học biểu diễn từ dữ liệu thay cho đặc trưng thủ công.

Xing và cs. (2018) tổng quan nhóm nghiên cứu "dự báo tài chính dựa trên ngôn ngữ tự nhiên", sắp xếp các kỹ thuật và ứng dụng và chỉ ra các điểm nóng của lĩnh vực ở giai đoạn trước khi mô hình Transformer phổ biến.

### 3.4. Mô hình ngôn ngữ tiền huấn luyện (BERT và các biến thể tài chính)

Bước ngoặt lớn là các mô hình tiền huấn luyện dựa trên Transformer. Araci (2019) giới thiệu FinBERT, một mô hình dựa trên BERT dành cho NLP tài chính, xuất phát từ hai khó khăn là dữ liệu gán nhãn tài chính khan hiếm và từ vựng chuyên ngành. Tác giả báo cáo kết quả tốt nhất vào thời điểm đó trên FiQA (chấm điểm cảm xúc) và Financial PhraseBank, và cho biết mô hình vượt các phương pháp học máy tiên tiến dù dùng ít dữ liệu huấn luyện hơn và chỉ tinh chỉnh một phần mô hình. Một công trình khác cùng tên, Yang và cs. (2020), tiền huấn luyện BERT trên văn bản giao tiếp tài chính và cho thấy mô hình vượt BERT miền tổng quát trên ba tác vụ phân loại cảm xúc tài chính; đây là mô hình BERT chuyên ngành tài chính đầu tiên được tác giả công bố.

Mishev và cs. (2020) cung cấp một đánh giá có hệ thống "từ từ điển đến Transformer": họ xây dựng nền tảng đánh giá và chạy hơn một trăm thí nghiệm trên các tập dữ liệu công khai do chuyên gia tài chính gán nhãn. Kết luận chính là biểu diễn theo ngữ cảnh vượt trội so với từ điển và bộ mã hóa cố định; ngoài ra các Transformer rút gọn (distilled) cho hiệu năng gần với bản đầy đủ, nên thực tế đáng cân nhắc khi triển khai.

### 3.5. Mô hình ngôn ngữ lớn (LLM)

Từ 2023, LLM mở ra hướng tiếp cận thứ tư. Lopez-Lira và Tang (2023) yêu cầu ChatGPT phân loại tiêu đề tin tức là tốt, xấu hay trung lập đối với giá cổ phiếu của công ty, rồi so sánh với lợi suất sau đó. Họ báo cáo tương quan dương, có ý nghĩa thống kê giữa điểm của ChatGPT và lợi suất ngày kế tiếp. Các mô hình cơ bản hơn như GPT-1, GPT-2 và BERT không dự báo được lợi suất chính xác, trong khi mô hình mạnh hơn (GPT-4) cho khả năng dự báo cao nhất. Khả năng dự báo rõ hơn ở cổ phiếu nhỏ. Chính tác giả chính lưu ý trong phỏng vấn rằng tương quan rất nhỏ dù có ý nghĩa thống kê, nên không nên diễn giải quá mức.

Song song, có các mô hình LLM chuyên ngành tài chính. BloombergGPT (Wu và cs., 2023) là mô hình 50 tỷ tham số, huấn luyện trên bộ dữ liệu 363 tỷ token từ nguồn của Bloomberg cộng 345 tỷ token từ dữ liệu tổng quát; tác giả báo cáo mô hình vượt các mô hình cùng cỡ trên tác vụ tài chính và vẫn cạnh tranh trên benchmark tổng quát. FinGPT (Yang và cs., 2023) đi theo hướng mở: nhấn mạnh quy trình thu thập, làm sạch dữ liệu và thích ứng nhẹ bằng LoRA như một phương án thay thế mã nguồn mở cho các mô hình độc quyền.

Một khảo sát LLM cho ứng dụng tài chính (Nie và cs., 2024) phân loại tài liệu theo các nhóm gồm tác vụ ngôn ngữ, phân tích cảm xúc, chuỗi thời gian tài chính, suy luận tài chính và mô hình dựa trên tác tử, đồng thời nêu các vấn đề mở như thiên lệch nhìn trước, ràng buộc pháp lý, ô nhiễm dữ liệu và khả năng diễn giải.

### 3.6. So sánh các nhóm phương pháp

| Nhóm | Đại diện | Điểm mạnh | Hạn chế chính |
|---|---|---|---|
| Từ điển | Loughran & McDonald (2011) | Minh bạch, rẻ, dễ tái lập | Bỏ qua ngữ cảnh, phủ định |
| Học máy truyền thống | Das & Chen (2007) | Học từ dữ liệu, dễ triển khai | Cần đặc trưng thủ công và nhãn |
| Học sâu | Ding và cs. (2015) | Học biểu diễn tự động | Cần nhiều dữ liệu, khó diễn giải |
| Transformer tiền huấn luyện | Araci (2019); Yang và cs. (2020) | Hiểu ngữ cảnh, cần ít nhãn | Cần tinh chỉnh, chi phí tính toán |
| LLM | Lopez-Lira & Tang (2023); Wu và cs. (2023) | Zero/few-shot, linh hoạt | Chi phí, thiên lệch nhìn trước, tái lập |

---

## 4. Dữ liệu và nguồn văn bản

**Báo cáo doanh nghiệp.** Hồ sơ 10-K là nguồn chính trong nghiên cứu theo hướng kế toán–tài chính (Loughran & McDonald, 2011, 2016). Ưu điểm là văn bản có cấu trúc, chính thức; nhược điểm là dài, nhiều văn bản pháp lý lặp lại.

**Tin tức tài chính.** Tetlock (2007) dùng một chuyên mục báo; Ding và cs. (2015) dùng tin Reuters và Bloomberg; Lopez-Lira và Tang (2023) dùng tiêu đề tin. Tin tức có chất lượng biên tập cao nhưng có độ trễ so với giá và chịu ảnh hưởng của nguồn phát hành.

**Diễn đàn và mạng xã hội.** Antweiler và Frank (2004) và Das và Chen (2007) khai thác bảng tin Yahoo! Finance. Bollen và cs. (2011) dùng dữ liệu Twitter để đo các trạng thái tâm trạng tập thể (bằng OpinionFinder và GPOMS) và báo cáo độ chính xác 87,6% khi dự đoán chiều biến động hằng ngày của chỉ số DJIA. Con số này do tác giả công bố, mẫu nhỏ và cần thận trọng khi khái quát, nên không nên xem là bằng chứng chắc chắn về khả năng dự báo. Dữ liệu mạng xã hội có ưu điểm về độ phủ và tốc độ, nhưng nhiễu, nhiều tiếng lóng, biểu tượng cảm xúc và có thể bị thao túng.

**Bộ dữ liệu chuẩn.**
- **Financial PhraseBank** (Malo và cs., 2014): khoảng 5.000 cụm từ/câu từ tin tức kinh tế được chuyên gia tài chính gán nhãn; là chuẩn phổ biến cho phân loại cảm xúc tài chính.
- **FiQA** (Maia và cs., 2018): thử thách mở tại The Web Conference 2018 về khai phá quan điểm tài chính và hỏi đáp. Dữ liệu thu thập từ StackExchange, Reddit và StockTwits giai đoạn 2009–2017, gồm hai tác vụ là phân tích cảm xúc theo khía cạnh và hỏi đáp dựa trên quan điểm. Một khảo sát (arXiv 2402.02315) mô tả phần FiQA-SA có 1.173 bài đăng từ tiêu đề và vi blog.

Một bài học xuyên suốt: các tập dữ liệu chuẩn nhỏ và thuộc phạm vi hẹp (chủ yếu tiếng Anh, thị trường Mỹ/châu Âu), nên điểm số cao trên benchmark chưa chắc chuyển sang môi trường thực.

---

## 5. Ứng dụng

**Nghiên cứu tài chính thực nghiệm.** Đo giọng điệu báo cáo, tin tức để kiểm tra phản ứng thị trường, gian lận, rủi ro (Loughran & McDonald, 2011; Tetlock, 2007). Kearney và Liu (2014) tổng hợp rằng cảm xúc văn bản liên hệ với hành vi ở cấp cá nhân, doanh nghiệp và thị trường, đồng thời chỉ ra các điểm đồng thuận và còn tranh luận.

**Dự báo thị trường và giao dịch.** Từ Bollen và cs. (2011) đến Ding và cs. (2015) và Lopez-Lira và Tang (2023), mục tiêu chung là biến cảm xúc thành tín hiệu dự báo. Lopez-Lira và Tang báo cáo chiến lược mua–bán dựa trên điểm cảm xúc mang lại lợi nhuận bình quân ngày khoảng 9 điểm cơ bản ở vị thế mua và 29 điểm cơ bản ở vị thế bán trong mẫu nghiên cứu (theo bản 2024). Mức này chưa tính đầy đủ chi phí giao dịch và có thể suy giảm theo thời gian khi nhiều người cùng khai thác tín hiệu.

**Quản trị rủi ro và hỗ trợ ra quyết định.** Cảm xúc có thể là đầu vào cho giám sát rủi ro, phân tích đối thủ hoặc tư vấn tự động. Phần này hiện được thảo luận nhiều trong các khảo sát LLM (Nie và cs., 2024; Yang và cs., 2023) hơn là có bằng chứng thực nghiệm đủ mạnh trong tài liệu tôi đã kiểm tra.

---

## 6. Thảo luận: thách thức và vấn đề mở

**(1) Thiên lệch nhìn trước (look-ahead bias).** LLM được huấn luyện trên dữ liệu có thể đã chứa thông tin về diễn biến giá sau tin tức đang kiểm thử, làm kết quả backtest bị thổi phồng. Glasserman và Lin (2023) dùng GPT-3.5 trên tiêu đề tin của các công ty S&P 500 và so sánh tiêu đề gốc với tiêu đề đã ẩn danh. Trong mẫu, phiên bản ẩn danh cho kết quả tốt hơn, và họ diễn giải rằng "hiệu ứng gây xao nhãng" (kiến thức chung về công ty làm nhiễu phán đoán) lấn át thiên lệch nhìn trước; ngoài mẫu thì thiên lệch nhìn trước không phải mối lo, nhưng sự xao nhãng vẫn có thể xảy ra. Đây là bản thảo arXiv, tôi chưa tìm thấy phiên bản bình duyệt.

**(2) Khả năng tái lập và chi phí.** Mô hình đóng như BloombergGPT không công khai, còn kết quả của API thương mại thay đổi theo phiên bản. Các hướng mở như FinGPT (Yang và cs., 2023) và Transformer rút gọn (Mishev và cs., 2020) là phương án giảm chi phí.

**(3) Ý nghĩa kinh tế so với ý nghĩa thống kê.** Tương quan nhỏ nhưng có ý nghĩa thống kê (Lopez-Lira & Tang, 2023) và các kết quả dự báo ấn tượng trên mẫu hẹp (Bollen và cs., 2011) cho thấy cần kiểm định ngoài mẫu, tính chi phí giao dịch và kiểm tra tính bền vững qua các giai đoạn thị trường.

**(4) Cảm xúc không bằng tác động lên giá.** Đa số mô hình phân loại cảm xúc của văn bản, trong khi nhà đầu tư quan tâm đến tác động lên giá. Hai khái niệm này có thể lệch nhau, và nhãn "tốt/xấu cho giá cổ phiếu" của Lopez-Lira và Tang (2023) là một nỗ lực rút ngắn khoảng cách đó.

**(5) Tính diễn giải.** Từ điển minh bạch nhưng thô, mô hình sâu chính xác hơn nhưng khó giải thích. Điều này quan trọng với các tổ chức chịu yêu cầu quản trị và tuân thủ.

**(6) Đa ngôn ngữ và thị trường mới nổi.** Gần như toàn bộ tài nguyên chuẩn ở trên là tiếng Anh. Phần 7 bàn riêng về tiếng Việt.

---

## 7. Bối cảnh tiếng Việt

Nghiên cứu về FSA tiếng Việt còn ít và nhỏ lẻ. Từ tìm kiếm của tôi, có thể ghi nhận:

- Một nghiên cứu đăng trên *International Journal of Financial Studies* (2023, tập 11, số 3, bài 101) về cảm xúc trích xuất từ tin tức và phản ứng thị trường chứng khoán Việt Nam, dùng PhoBERT để phân loại cảm xúc. Theo mô tả tìm được, bộ huấn luyện gồm gần 40.000 bài viết từ các trang tài chính–kinh tế; kết quả cho thấy phản ứng giá tức thời nhỏ nhưng nhà đầu tư có xu hướng phản ứng thái quá với tin tốt và xấu. Tôi chưa xác minh danh sách tác giả và chi tiết phương pháp từ toàn văn.
- Một tập dữ liệu nhỏ công khai trên GitHub gồm 1.000 tiêu đề bài viết tài chính từ CafeF.vn, gán nhãn thành ba nhóm (187 tiêu cực, 248 không tác động, 565 tích cực), tức là mất cân bằng lớp. Độ chính xác 93% là con số tự báo cáo.
- Một nghiên cứu trong lĩnh vực ngân hàng xây dựng ngữ liệu tài chính tiếng Việt 12.000 mẫu gán nhãn và tinh chỉnh PhoBERT, ViT5, BARTPho; ngữ liệu này dường như chưa được công bố.

Nhìn chung, thiếu một bộ dữ liệu chuẩn tiếng Việt đủ lớn, được công bố và có quy trình gán nhãn rõ ràng, tương đương Financial PhraseBank. Đây là khoảng trống rõ ràng cho nghiên cứu tương lai.

---

## 8. Hướng nghiên cứu tương lai

1. **Xây dựng benchmark chuẩn tiếng Việt** cho cảm xúc tài chính, kèm hướng dẫn gán nhãn và độ đồng thuận giữa người gán nhãn.
2. **Đánh giá LLM không rò rỉ thời gian**: dùng ẩn danh hóa thực thể (Glasserman & Lin, 2023), tập kiểm thử sau thời điểm cắt dữ liệu huấn luyện của mô hình, và báo cáo rõ phiên bản mô hình.
3. **Chuyển từ cảm xúc sang tác động**: mô hình hóa trực tiếp tác động của tin lên giá và rủi ro, kèm kiểm định ngoài mẫu và chi phí giao dịch.
4. **Mô hình nhẹ, mở, có thể diễn giải** cho môi trường hạn chế tài nguyên (Mishev và cs., 2020; Yang và cs., 2023).
5. **Đa phương thức**: kết hợp văn bản với âm thanh trong họp báo cáo kết quả, bảng biểu và dữ liệu giá. Hướng này tôi nêu như một gợi ý, chưa có tài liệu đã kiểm chứng trong bài.

---

## 9. Kết luận

Hai thập kỷ qua, FSA đi từ việc đếm từ trong từ điển, qua bộ phân loại học máy và học sâu, đến mô hình Transformer chuyên ngành và LLM. Mỗi bước nâng khả năng hiểu ngữ cảnh nhưng cũng làm nảy sinh vấn đề mới: chi phí, khả năng tái lập, thiên lệch nhìn trước và tính diễn giải. Các bằng chứng về khả năng dự báo thị trường nhìn chung dương nhưng khiêm tốn, và phần lớn dựa trên mẫu hạn chế, tiếng Anh, thị trường phát triển. Với tiếng Việt và thị trường mới nổi, nhu cầu cấp thiết nhất là dữ liệu chuẩn mở và quy trình đánh giá chặt chẽ.

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

---

## Ghi chú về độ tin cậy

- Thông tin thư mục (tác giả, năm, tạp chí) của các bài chính đã được đối chiếu với trang kho lưu trữ hoặc cơ sở dữ liệu, nhưng **chưa đọc toàn văn** hầu hết các bài. Số liệu kết quả là số do tác giả công bố, lấy từ tóm tắt.
- Các mục đánh dấu "cần xác minh" ở phần tài liệu tham khảo cần được bổ sung trước khi nộp hoặc đăng.
- Tôi không tìm đủ thông tin kiểm chứng về các nghiên cứu cảm xúc tài chính dựa trên LSTM/CNN thuần (ngoài Ding và cs., 2015) nên không đưa vào để tránh trích dẫn sai.
