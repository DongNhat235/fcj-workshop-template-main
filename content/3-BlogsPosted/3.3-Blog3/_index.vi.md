---
title: "Blog 3"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 3.3. </b> "
---


#  Hiện đại hóa SignalR với AWS AppSync Event API

Chào mọi người, mình tìm hiểu được một chủ đề khá hay về Modernizing SignalR with AWS AppSync Event API — nói đơn giản là cách hiện đại hóa kiến trúc real-time của ứng dụng .NET/React bằng cách chuyển từ mô hình SignalR truyền thống sang AWS AppSync Event API.

Trong các ứng dụng real-time như thông báo đơn hàng, live dashboard, cập nhật trạng thái giao hàng, chat hoặc hệ thống publish/subscribe, SignalR thường được dùng để duy trì kết nối WebSocket giữa server và client. Tuy nhiên, khi hệ thống mở rộng, đội phát triển có thể gặp các vấn đề như phải quản lý nhiều WebSocket connection, duy trì server luôn chạy, cấu hình sticky session hoặc Redis backplane để scale nhiều server.

Nhìn vào sơ đồ, kiến trúc mới được đơn giản hóa hơn với 4 luồng chính:
Luồng 1:
Người dùng truy cập ứng dụng thông qua React Client. Khi có hành động cần real-time, ví dụ đặt hàng hoặc gửi một sự kiện mới, React Client sẽ gọi xuống .NET API Server.

Luồng 2:
.NET API Server không hard-code thông tin kết nối AppSync trong source code, mà lấy thông tin cần thiết như API key hoặc endpoint từ AWS Secrets Manager. Cách này giúp quản lý secret an toàn hơn và dễ xoay vòng credential khi cần.

Luồng 3:
Sau khi xử lý logic nghiệp vụ, .NET API Server publish event lên AWS AppSync Event API thông qua HTTP request. Thay vì server phải tự quản lý từng WebSocket connection như SignalR, backend chỉ cần gửi event lên AppSync.

Luồng 4:
AWS AppSync đảm nhiệm phần publish/subscribe và đẩy event đến các Subscribers theo thời gian thực thông qua WebSocket. Người dùng hoặc các client đang subscribe channel sẽ nhận được cập nhật ngay mà không cần polling liên tục.

Điểm hay của kiến trúc này là backend được tách khỏi việc quản lý kết nối WebSocket. Với SignalR truyền thống, server thường phải theo dõi connection state, group, user connection và xử lý scale-out. Còn với AppSync Event API, AWS quản lý phần kết nối, phân phối event, khả năng scale và tính sẵn sàng của hạ tầng.

**Có thể hiểu đơn giản:**
SignalR truyền thống: Server vừa xử lý business logic, vừa quản lý WebSocket connection.
AWS AppSync Event API: .NET API Server chỉ tập trung xử lý nghiệp vụ và publish event. AppSync chịu trách nhiệm phân phối event real-time đến các subscriber.

Kiến trúc này đặc biệt phù hợp với các use case như thông báo real-time, live dashboard, cập nhật trạng thái đơn hàng, collaborative app, IoT data distribution hoặc các hệ thống cần gửi một event đến nhiều client cùng lúc.
Bên cạnh đó, việc dùng AWS Secrets Manager giúp tách thông tin nhạy cảm khỏi source code. Khi triển khai thực tế, hệ thống có thể kết hợp thêm IAM, CloudWatch, CloudTrail và cơ chế tách môi trường dev/staging/production để tăng bảo mật, giám sát lỗi publish/subscription và kiểm soát vận hành tốt hơn.


**Từ sơ đồ có thể rút ra một ý quan trọng**
Hiện đại hóa SignalR không có nghĩa là bỏ hoàn toàn real-time, mà là chuyển phần phức tạp của WebSocket infrastructure sang một dịch vụ managed/serverless của AWS. Điều này giúp team giảm gánh nặng vận hành, dễ scale hơn và tập trung nhiều hơn vào business logic.

Kết luận
AWS AppSync Event API là một hướng tiếp cận phù hợp khi ứng dụng .NET/React cần real-time communication theo mô hình publish/subscribe. Với kiến trúc này, backend gọn hơn, frontend vẫn nhận dữ liệu real-time, còn AWS đảm nhiệm phần hạ tầng WebSocket phía sau.


![anh tu bai blog](/images/3-blog/blog3.png)

[...Link...](https://www.facebook.com/groups/awsstudygroupfcj/permalink/2206455833452710/?rdid=geoKRLwi2jjUs3tZ#)
