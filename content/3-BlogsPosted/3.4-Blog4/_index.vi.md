---
title: "Blog 4"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 3.4. </b> "
---

# AWS and Elastio deliver comprehensive ransomware resilience

AWS and Elastio deliver comprehensive ransomware resilience
Chào mọi người, mình tìm hiểu được một chủ đề khá hay về AWS and Elastio deliver comprehensive ransomware resilience — nói đơn giản là cách AWS kết hợp với Elastio để giúp doanh nghiệp tăng khả năng chống chịu và khôi phục dữ liệu khi gặp tấn công ransomware.

Nhìn vào sơ đồ, có thể thấy chiến lược bảo vệ dữ liệu không chỉ dừng lại ở hệ thống đang chạy chính, mà được chia thành nhiều lớp bảo vệ khác nhau: Production, Disaster Recovery, Backup và Vault.

Ở lớp Production, hệ thống chính gồm môi trường Active và Standby, dữ liệu được đồng bộ để đảm bảo dịch vụ vẫn có thể tiếp tục hoạt động khi một phần hệ thống gặp sự cố. Đây là lớp vận hành trực tiếp, nơi người dùng và các dịch vụ nội bộ như AD, DNS, DHCP, SaaS, Network, Monitoring, Workstation và Phones tương tác hằng ngày.

Tiếp theo là lớp Disaster Recovery, gồm các môi trường Warm và Cold. Mục tiêu của lớp này là giúp doanh nghiệp có phương án khôi phục khi môi trường production bị ảnh hưởng. Warm site thường sẵn sàng hơn và phục hồi nhanh hơn, trong khi Cold site tiết kiệm chi phí hơn nhưng cần nhiều thời gian để khởi động lại.

Lớp Backup đóng vai trò lưu trữ các bản sao dữ liệu theo lịch.
Trong hình, backup server tạo bản sao từ dữ liệu chính sang dữ liệu phụ theo cơ chế scheduled backup. Đây là bước quan trọng, nhưng trong bối cảnh ransomware hiện đại, chỉ có backup thôi là chưa đủ, vì ransomware có thể tấn công cả hệ thống backup nếu không được bảo vệ đúng cách.

Điểm quan trọng nhất trong sơ đồ là lớp Vault, cụ thể là Cloud-hosted data vault. Đây có thể hiểu như một “két dữ liệu an toàn” trên cloud, nơi lưu trữ các bản sao dữ liệu quan trọng theo hướng tách biệt và khó bị thay đổi. Lớp vault giúp giảm rủi ro ransomware mã hóa hoặc phá hủy toàn bộ dữ liệu khôi phục.

Trong kiến trúc này, AWS Backup có thể được sử dụng để quản lý chính sách sao lưu tập trung, tạo backup theo lịch và lưu dữ liệu vào các vault an toàn. Bên cạnh đó, AWS Elastic Disaster Recovery hỗ trợ khôi phục workload nhanh khi hệ thống chính gặp sự cố.
Điểm khác biệt khi kết hợp với Elastio là khả năng kiểm tra và xác minh dữ liệu backup/recovery point. Elastio giúp phát hiện dấu hiệu ransomware, dữ liệu bị mã hóa bất thường, corruption âm thầm hoặc những bản backup không còn đủ tin cậy để khôi phục.

**Nói dễ hiểu hơn:**
AWS cung cấp nền tảng backup, disaster recovery và vault an toàn. Elastio bổ sung lớp kiểm chứng để đảm bảo bản backup đó thật sự sạch, an toàn và có thể khôi phục được.
Từ sơ đồ có thể rút ra một ý rất quan trọng: ransomware resilience không chỉ là “có backup”, mà là phải có một chiến lược nhiều lớp, gồm hệ thống vận hành chính, môi trường khôi phục thảm họa, backup theo lịch và vault tách biệt để bảo vệ dữ liệu quan trọng.

**Kết luận**
AWS và Elastio giúp doanh nghiệp xây dựng một chiến lược bảo vệ dữ liệu toàn diện hơn trước ransomware: vừa duy trì hoạt động kinh doanh, vừa đảm bảo có bản sao dữ liệu sạch và đáng tin cậy để khôi phục khi xảy ra sự cố.

{{< img "images/3-Blog/blog4.png" "anh tu bai blog" >}}

[...link...](https://www.facebook.com/groups/awsstudygroupfcj/posts/2205365060228454/?notif_id=1783407018744128&notif_t=group_post_approved)