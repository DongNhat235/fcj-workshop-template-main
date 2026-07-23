---
title: "Blog 2"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 3.2. </b> "
---

# Đơn giản hóa truy cập dữ liệu doanh nghiệp với AWS Transfer Family Web Apps và Terraform
Trong nhiều doanh nghiệp, dữ liệu quan trọng thường được lưu trữ trên Amazon S3 để phục vụ phân tích, báo cáo, cộng tác nội bộ hoặc lưu trữ tài liệu. Tuy nhiên, một vấn đề rất thực tế là không phải người dùng nào cũng biết sử dụng AWS Console, CLI hay các công cụ kỹ thuật để truy cập dữ liệu trên S3.
Vậy làm thế nào để nhân viên có thể upload, download và truy cập file trên Amazon S3 một cách đơn giản, an toàn và dễ quản lý?
AWS đưa ra một kiến trúc rất phù hợp: AWS Transfer Family Web Apps kết hợp với AWS IAM Identity Center, Amazon S3 Access Grants, Amazon S3, AWS CloudTrail và Terraform. Transfer Family Web Apps cung cấp một cổng truy cập dạng web, giúp người dùng đã xác thực có thể duyệt, tải lên và tải xuống dữ liệu S3 mà không cần dùng AWS Console hoặc tự xây dựng một cổng nội bộ phức tạp.



{{< img "images/3-Blog/blog2.png" "anh tu bai blog" >}}

**Kiến trúc tổng quan**

Nhìn vào sơ đồ, luồng hoạt động có thể hiểu theo 5 bước chính:

1. End User xác thực với AWS IAM Identity Center - Người dùng cuối truy cập hệ thống và đăng nhập thông qua AWS IAM Identity Center. Đây là nơi quản lý danh tính tập trung cho người dùng doanh nghiệp. Trong trường hợp doanh nghiệp đã có hệ thống định danh riêng, IAM Identity Center cũng có thể tích hợp với External Identity Provider như Azure AD, Okta hoặc các IdP hỗ trợ SAML.
   
2. Sau khi xác thực, người dùng truy cập AWS Transfer Family Web Apps - Sau khi đăng nhập thành công, người dùng được chuyển vào AWS Transfer Family Web Apps. Đây là giao diện web thân thiện, giúp người dùng thao tác với dữ liệu trên S3 mà không cần hiểu sâu về AWS. Thay vì phải vào AWS Console, người dùng chỉ cần mở trình duyệt, đăng nhập và thao tác với file như một cổng file portal nội bộ.
   
3. AWS Transfer Family Web Apps lấy quyền truy cập từ Amazon S3 Access GRANTS - Điểm quan trọng của kiến trúc này là quyền truy cập không được cấp một cách thủ công, rời rạc hoặc quá rộng. Thay vào đó, hệ thống dùng Amazon S3 Access Grants để cấp quyền chi tiết theo danh tính người dùng hoặc nhóm người dùng.
   
4. Người dùng upload hoặc download object trên Amazon S3 - Sau khi quyền được kiểm tra, người dùng có thể truy cập dữ liệu trong Amazon S3. Tùy vào vai trò, họ có thể tải file lên, tải file xuống hoặc chỉ xem danh sách file. Điều này giúp doanh nghiệp giữ được sự đơn giản ở phía người dùng, nhưng vẫn đảm bảo kiểm soát chặt chẽ ở phía hệ thống.
5. AWS CloudTrail ghi log hoạt động - Mọi hoạt động như upload, download hoặc delete file đều có thể được ghi nhận bởi AWS CloudTrail. Đây là thành phần quan trọng với các hệ thống cần kiểm toán, tuân thủ bảo mật hoặc điều tra khi có sự cố.
Vai trò của Terraform trong kiến trúc này
Một điểm rất hay trong giải pháp là sử dụng Terraform để triển khai hạ tầng theo hướng Infrastructure as Code.

Thay vì cấu hình thủ công từng thành phần như IAM Identity Center, S3 bucket, Access Grants, CloudTrail hay Transfer Family Web Apps, Terraform giúp đóng gói toàn bộ kiến trúc thành một deployment có thể lặp lại. Điều này đặc biệt hữu ích khi doanh nghiệp cần triển khai nhiều môi trường như Development, Staging và Production, hoặc áp dụng cùng một mô hình truy cập dữ liệu cho nhiều phòng ban khác nhau.

**Giá trị bảo mật và vận hành**

Kiến trúc này giải quyết được nhiều vấn đề quan trọng:
Người dùng không cần truy cập AWS Console.
Không cần xây dựng custom portal từ đầu.
Phân quyền chi tiết theo user hoặc group.
Hỗ trợ tách biệt nhiệm vụ giữa các vai trò.
Có audit log phục vụ giám sát và compliance.
Có thể tích hợp hệ thống định danh doanh nghiệp hiện có.
Triển khai lặp lại bằng Terraform.

**Kết luận**

AWS Transfer Family Web Apps giúp biến Amazon S3 thành một cổng truy cập dữ liệu thân thiện hơn cho người dùng doanh nghiệp. Khi kết hợp với IAM Identity Center, S3 Access Grants, CloudTrail và Terraform, giải pháp này vừa đơn giản cho người dùng cuối, vừa an toàn và dễ quản trị cho đội ngũ IT.
Đây là một kiến trúc rất đáng tham khảo nếu doanh nghiệp đang muốn xây dựng một hệ thống chia sẻ file nội bộ, bảo mật, có phân quyền rõ ràng và có khả năng mở rộng trên AWS.

[...Link...](https://www.facebook.com/photo/?fbid=1533670831545926)

