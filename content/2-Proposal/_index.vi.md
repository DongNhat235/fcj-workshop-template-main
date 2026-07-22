---

title: "Đề xuất dự án"
date: 2026-07-19
weight: 2
chapter: false
pre: " <b> 2. </b> "
--------------------

# Nền tảng web thể thao BravelSport

## Đề xuất kiến trúc AWS cho hệ thống triển khai an toàn và có khả năng mở rộng

### 1. Tóm tắt dự án

BravelSport là nền tảng web thể thao được triển khai tại địa chỉ:

`https://bravelsport.com/`

Hệ thống hướng đến các nhóm người dùng như khách hàng, người chơi thể thao, câu lạc bộ, chủ sân và quản trị viên.

Các chức năng chính của BravelSport gồm:

* Xem danh sách và thông tin chi tiết sản phẩm thể thao.
* Tìm kiếm và lọc sản phẩm.
* Đăng ký và đăng nhập tài khoản.
* Quản lý giỏ hàng.
* Đặt hàng và theo dõi đơn hàng.
* Đặt sân thể thao.
* Quản lý thông tin sân và lịch đặt sân.
* Tải lên hình ảnh sản phẩm và sân thể thao.
* Quản lý người dùng, sản phẩm, đơn hàng, sân và nội dung hệ thống.

Đề xuất này trình bày phương án triển khai BravelSport trên AWS theo kiến trúc tách biệt giữa frontend, backend, hệ thống mạng, lưu trữ, giám sát và cơ sở dữ liệu.

Frontend được build thành static files, lưu trên Amazon S3 và phân phối qua Amazon CloudFront. Domain `bravelsport.com` được nhóm đăng ký và quản lý bằng Amazon Route 53. AWS WAF được sử dụng để kiểm tra các request đầu vào.

Backend được đóng gói bằng Docker, lưu trên Amazon ECR và chạy bằng Amazon ECS Fargate trong private subnet. Application Load Balancer nhận request API và chuyển tiếp request đến ECS task.

MongoDB Atlas được sử dụng làm cơ sở dữ liệu bên ngoài AWS. Amazon S3 lưu hình ảnh, media và tệp cấu hình của ứng dụng. AWS IAM quản lý quyền truy cập, trong khi Amazon CloudWatch thu thập logs và metrics.

Kiến trúc này phù hợp với mục tiêu workshop, MVP và hệ thống có quy mô nhỏ hoặc trung bình.

---

### 2. Vấn đề cần giải quyết

BravelSport không chỉ là một website tĩnh mà bao gồm nhiều thành phần như frontend, backend API, cơ sở dữ liệu, media upload, đặt hàng, đặt sân và quản trị nội dung.

Nếu không có kiến trúc triển khai rõ ràng, hệ thống có thể gặp những vấn đề sau:

* Backend bị public trực tiếp ra Internet.
* Frontend và backend phụ thuộc vào cùng một máy chủ.
* Media bị lưu trên local storage và có thể mất khi container được thay thế.
* Khó quản lý và rollback phiên bản backend.
* Không có logs tập trung để kiểm tra lỗi.
* Khó mở rộng khi số lượng người dùng tăng.
* Credential có nguy cơ bị lộ nếu lưu trong source code.
* Tài nguyên AWS có thể tiếp tục phát sinh chi phí sau workshop.

Giải pháp được đề xuất là tách riêng frontend, backend, media và cơ sở dữ liệu. Frontend được triển khai bằng S3 và CloudFront, backend chạy trên ECS Fargate trong private subnet, còn dữ liệu được lưu trên MongoDB Atlas.

---

### 3. Mục tiêu triển khai

Các mục tiêu chính của dự án gồm:

* Triển khai BravelSport trên AWS theo kiến trúc rõ ràng.
* Tách biệt frontend, backend, media và database.
* Không public trực tiếp ECS task ra Internet.
* Sử dụng Docker để đóng gói backend.
* Quản lý Docker image bằng Amazon ECR.
* Lưu media bằng Amazon S3.
* Thu thập logs và metrics bằng CloudWatch.
* Quản lý quyền truy cập bằng AWS IAM.
* Hỗ trợ mở rộng bằng cách tăng số lượng ECS task.
* Theo dõi chi phí và xóa tài nguyên không còn sử dụng.

---

### 4. Kiến trúc giải pháp

Kiến trúc BravelSport gồm ba khu vực chính:

1. Edge và Frontend.
2. VPC và Backend.
3. Các dịch vụ hỗ trợ và lưu trữ dữ liệu.

<!--
Đặt ảnh kiến trúc tại:
static/images/2-Proposal/bravelsport_aws_architecture.png
-->

![Kiến trúc AWS BravelSport](/images/2-Proposal/bravelsport_aws_architecture.png)

#### 4.1. Edge và Frontend

Domain `bravelsport.com` được nhóm đăng ký và quản lý bằng Amazon Route 53.

Khi người dùng truy cập website, Route 53 thực hiện DNS resolution và trỏ domain đến Amazon CloudFront.

AWS WAF được liên kết với CloudFront để kiểm tra request và giảm rủi ro từ các request không hợp lệ hoặc các kiểu tấn công web phổ biến.

CloudFront phân phối static frontend được lưu trong S3 Frontend Bucket. Bucket được đặt ở chế độ private và không cho phép người dùng truy cập trực tiếp.

#### 4.2. VPC và Backend

Amazon VPC tạo ranh giới mạng cho backend BravelSport.

Application Load Balancer và NAT Gateway được đặt trong public subnet. ECS Fargate task được đặt trong private subnet và không có public IP.

Application Load Balancer là điểm nhận backend traffic. ALB chuyển request API đến ECS thông qua target group và thực hiện health check để kiểm tra trạng thái của ECS task.

ECS chỉ nhận inbound traffic từ security group của ALB. Người dùng không thể truy cập trực tiếp vào ECS task.

Khi ECS cần truy cập Amazon ECR, Amazon CloudWatch, Amazon S3, MongoDB Atlas hoặc các public endpoint khác, traffic outbound được chuyển qua NAT Gateway và Internet Gateway.

#### 4.3. Dịch vụ hỗ trợ và lưu trữ

Các dịch vụ hỗ trợ hệ thống gồm:

* Amazon ECR lưu Docker image của backend.
* Amazon CloudWatch lưu application logs và runtime metrics.
* Amazon S3 Frontend Bucket lưu static frontend.
* Amazon S3 Media Upload lưu hình ảnh và media.
* Amazon S3 Private Configuration Bucket lưu tệp cấu hình.
* AWS IAM quản lý quyền truy cập.
* MongoDB Atlas lưu dữ liệu ứng dụng.

Database credential và application secret không được lưu trực tiếp trong source code hoặc Docker image.

Theo phương án hiện tại của nhóm, tệp cấu hình chứa credential được lưu trong một S3 bucket private. Bucket này cần:

* Bật S3 Block Public Access.
* Bật mã hóa dữ liệu.
* Chỉ cho phép ECS Task Role truy cập.
* Không cung cấp URL public.
* Không sử dụng chung với S3 Frontend Bucket.
* Không commit credential lên GitHub.

ECS kết nối MongoDB Atlas thông qua luồng:

`ECS Fargate → NAT Gateway → Internet Gateway → MongoDB Atlas`

MongoDB Atlas nên giới hạn kết nối theo Elastic IP của NAT Gateway thay vì cho phép toàn bộ địa chỉ IP bằng `0.0.0.0/0`.

---

### 5. Các dịch vụ được sử dụng

* **Amazon Route 53:** Đăng ký, quản lý domain và phân giải DNS đến CloudFront.
* **Amazon CloudFront:** Phân phối frontend và chuyển request API đến ALB.
* **AWS WAF:** Kiểm tra và lọc request đầu vào.
* **Amazon S3 Frontend Bucket:** Lưu static frontend.
* **Amazon VPC:** Tạo ranh giới mạng cho backend.
* **Public Subnet:** Chứa ALB và NAT Gateway.
* **Private Subnet:** Chứa ECS Fargate task.
* **Application Load Balancer:** Chuyển API traffic đến ECS.
* **Target Group:** Quản lý ECS task và thực hiện health check.
* **NAT Gateway:** Cung cấp outbound access cho ECS.
* **Internet Gateway:** Kết nối public subnet với Internet.
* **Elastic IP:** Cung cấp địa chỉ IP cố định cho NAT Gateway.
* **Amazon ECS Fargate:** Chạy backend container.
* **Amazon ECR:** Lưu Docker image của backend.
* **AWS IAM:** Quản lý role và quyền truy cập.
* **Amazon CloudWatch:** Thu thập logs và metrics.
* **Amazon S3 Media Upload:** Lưu hình ảnh và media.
* **Amazon S3 Private Configuration Bucket:** Lưu tệp cấu hình và credential.
* **MongoDB Atlas:** Lưu dữ liệu ứng dụng bên ngoài AWS.

---

### 6. Luồng hoạt động chính

1. Người dùng truy cập domain `bravelsport.com`.
2. Route 53 phân giải DNS đến CloudFront.
3. AWS WAF kiểm tra request.
4. CloudFront lấy static frontend từ S3.
5. CloudFront chuyển request API đến ALB.
6. ALB chuyển request đến ECS Fargate.
7. ECS xử lý logic nghiệp vụ.
8. IAM Role cấp quyền để ECS truy cập các tài nguyên AWS.
9. ECS pull Docker image từ Amazon ECR khi khởi tạo.
10. ECS đọc hoặc ghi media trên Amazon S3.
11. ECS gửi logs và metrics đến Amazon CloudWatch.
12. ECS kết nối MongoDB Atlas thông qua NAT Gateway.
13. Kết quả được trả về người dùng qua ALB và CloudFront.

IAM là quan hệ cấp quyền, không phải luồng truyền dữ liệu mạng. Trong sơ đồ, đường kết nối IAM với ECS nên được thể hiện bằng nét đứt.

---

### 7. Thiết kế bảo mật

Kiến trúc sử dụng hai security group chính.

#### SG-ALB

* Cho phép inbound traffic cần thiết đến ALB.
* Cho phép outbound đến backend port của ECS.
* Không mở các cổng quản trị không cần thiết.

#### SG-ECS

* Chỉ cho phép inbound từ SG-ALB.
* Không mở backend port trực tiếp cho `0.0.0.0/0`.
* Cho phép outbound đến các dịch vụ cần thiết.

Các biện pháp bảo mật khác gồm:

* ECS không có public IP.
* Các S3 bucket bật Block Public Access.
* IAM áp dụng nguyên tắc least privilege.
* Credential trong S3 được mã hóa.
* Chỉ ECS Task Role được đọc tệp cấu hình.
* MongoDB Atlas giới hạn theo Elastic IP của NAT Gateway.
* Credential không được commit lên GitHub.
* AWS WAF được kiểm thử trước khi bật chế độ chặn.

---

### 8. Lộ trình ba tháng

#### Tháng 1 – Tìm hiểu dịch vụ AWS

Nhóm tìm hiểu Route 53, CloudFront, WAF, S3, VPC, ALB, NAT Gateway, ECS Fargate, ECR, IAM và CloudWatch. Nhóm đồng thời phân tích yêu cầu BravelSport và xây dựng sơ đồ kiến trúc ban đầu.

**Kết quả:** Hoàn thành tài liệu dịch vụ AWS và sơ đồ kiến trúc sơ bộ.

#### Tháng 2 – Nghiên cứu và thử nghiệm

Nhóm container hóa backend bằng Docker, thử nghiệm ECR và ECS, triển khai thử frontend trên S3 và CloudFront, thiết kế VPC, security group, ALB và kiểm tra kết nối MongoDB Atlas.

**Kết quả:** Hoàn thiện sơ đồ kiến trúc, Docker image và bản thử nghiệm các thành phần.

#### Tháng 3 – Triển khai và hoàn thiện

Nhóm triển khai frontend, backend và hệ thống mạng trên AWS; tích hợp S3, MongoDB Atlas, IAM và CloudWatch; kiểm thử BravelSport và hoàn thiện tài liệu workshop.

**Kết quả:** BravelSport hoạt động trên AWS và có tài liệu hướng dẫn hoàn chỉnh.

---

### 9. Chi phí và tối ưu

Các nhóm chi phí chính gồm:

* Amazon Route 53.
* Amazon CloudFront.
* Amazon S3.
* AWS WAF.
* Application Load Balancer.
* Amazon ECS Fargate.
* NAT Gateway.
* Elastic IP.
* Amazon ECR.
* Amazon CloudWatch.
* MongoDB Atlas.

**Chi phí dự kiến:** **[CẦN XÁC NHẬN]**

Các biện pháp tối ưu chi phí:

* Chọn kích thước ECS task phù hợp.
* Giảm thời gian chạy tài nguyên thử nghiệm.
* Xóa NAT Gateway và ALB khi không còn sử dụng.
* Xóa Elastic IP không được gắn.
* Xóa Docker image cũ trong ECR.
* Giới hạn thời gian lưu CloudWatch Logs.
* Tối ưu CloudFront cache.
* Theo dõi chi phí thường xuyên.
* Xóa tài nguyên workshop sau khi hoàn thành.

---

### 10. Rủi ro và phương án giảm thiểu

* **S3 bị public:** Bật Block Public Access và kiểm tra bucket policy.
* **Credential bị truy cập trái phép:** Mã hóa dữ liệu và giới hạn quyền cho ECS Task Role.
* **ECS không pull được image:** Kiểm tra ECR, IAM và NAT Gateway.
* **ALB health check thất bại:** Kiểm tra port, health check path và security group.
* **Không kết nối được MongoDB Atlas:** Kiểm tra Elastic IP, NAT route và database credential.
* **WAF chặn request hợp lệ:** Kiểm thử rule ở chế độ Count trước khi Block.
* **Chi phí NAT Gateway tăng:** Theo dõi outbound traffic và clean-up sau workshop.
* **Media upload thất bại:** Kiểm tra IAM, CORS, kích thước và loại file.
* **Credential bị lộ:** Không lưu trong source code, Docker image hoặc GitHub.

---

### 11. Kết quả kỳ vọng

Sau khi hoàn thành dự án:

* BravelSport được triển khai trên AWS.
* Domain được đăng ký và quản lý bằng Route 53.
* Frontend được lưu trên S3 và phân phối qua CloudFront.
* Backend chạy bằng ECS Fargate trong private subnet.
* API traffic đi qua Application Load Balancer.
* Docker image được quản lý trong Amazon ECR.
* Media được lưu trên Amazon S3.
* Dữ liệu được lưu trong MongoDB Atlas.
* Logs và metrics được thu thập trong CloudWatch.
* Quyền truy cập được kiểm soát bằng IAM.
* Nhóm có quy trình kiểm thử và clean-up tài nguyên rõ ràng.

---

### 12. Cải tiến trong tương lai

* Thêm CloudWatch Alarms.
* Thêm AWS Budgets.
* Xây dựng CI/CD pipeline.
* Thêm ECS Service Auto Scaling.
* Triển khai nhiều Availability Zone.
* Thêm VPC Endpoint để giảm traffic qua NAT Gateway.
* Chuyển credential sang dịch vụ quản lý secret chuyên dụng.
* Bổ sung backup cho Amazon S3 và MongoDB Atlas.

---

### 13. Kết luận

Kiến trúc đề xuất giúp BravelSport tách biệt frontend, backend, media và cơ sở dữ liệu.

Frontend được triển khai bằng Amazon S3 và CloudFront. Backend được đóng gói bằng Docker và chạy trên ECS Fargate trong private subnet.

Domain của dự án được đăng ký và quản lý bằng Route 53. Application Load Balancer nhận backend traffic, NAT Gateway cung cấp outbound access, ECR quản lý Docker image, CloudWatch hỗ trợ giám sát và MongoDB Atlas lưu dữ liệu ứng dụng.

Lộ trình ba tháng giúp nhóm lần lượt tìm hiểu dịch vụ AWS, nghiên cứu kiến trúc và triển khai hoàn chỉnh BravelSport. Kiến trúc đáp ứng mục tiêu workshop và có thể tiếp tục mở rộng trong tương lai.
