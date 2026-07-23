---
title: "Workshop"
date: 2026-07-19
weight: 5
chapter: false
pre: " <b> 5. </b> "
---


# Triển khai BravelSport trên AWS

BravelSport là nền tảng thương mại điện tử và đặt sân thể thao. Mã nguồn gồm frontend React/Vite và backend NestJS; backend sử dụng MongoDB qua Mongoose, JWT cho xác thực và Socket.IO cho chức năng chat realtime.

Workshop này mô tả **kiến trúc mục tiêu và quy trình triển khai thực hành**. Nội dung không khẳng định website hiện tại đang chạy trên toàn bộ kiến trúc AWS nếu chưa có bằng chứng từ AWS Console.

## Kiến trúc mục tiêu

- Frontend được build thành static files, lưu trong S3 Frontend Bucket private và phân phối qua CloudFront.
- AWS WAF liên kết với CloudFront để kiểm tra request tại lớp edge.
- `/api/*` và `/socket.io/*` được CloudFront chuyển đến Application Load Balancer.
- ALB chuyển request qua Target Group loại `ip` đến ECS Fargate task trên cổng `3000`.
- Socket.IO dùng transport path `/socket.io/*`; ứng dụng chat dùng namespace `/chat`.
- ECS Fargate chạy trong Private Subnet, không có public IP.
- ECS kết nối MongoDB Atlas bên ngoài VPC thông qua NAT Gateway và Internet Gateway.
- Amazon EC2 Ubuntu chỉ là máy build và triển khai, không nhận request production.
- S3 Media là phần chuyển đổi hoặc mở rộng của workshop vì mã nguồn hiện có hỗ trợ Cloudinary và local `/uploads`.

{{< img "images/2-Proposal/bravelsport_aws_architecture.png" "BravelSport AWS Architecture" >}}

## Nội dung workshop

1. [5.1. Tổng quan workshop](./5.1-Workshop-overview/)
2. [5.2. Các bước chuẩn bị](./5.2-Prerequisite/)
3. [5.3. Xây dựng hạ tầng mạng](./5.3-Network-infrastructure/)
4. [5.4. Triển khai backend](./5.4-Backend-deployment/)
5. [5.5. Triển khai frontend](./5.5-Frontend-deployment/)
6. [5.6. Database và media](./5.6-Data-and-media/)
7. [5.7. Kiểm thử end-to-end](./5.7-Testing/)
8. [5.8. Bảo mật và chi phí](./5.8-Security-and-cost/)
9. [5.9. Dọn dẹp tài nguyên](./5.9-Cleanup/)

### Lưu ý

Không đưa access key, secret, MongoDB connection string, JWT secret, cookie đăng nhập hoặc Account ID đầy đủ vào tài liệu. Giá trị chưa được nhóm xác nhận phải giữ nguyên dưới dạng `[TO BE CONFIRMED]`.

## Kiểm tra kết quả

- Menu Hugo hiển thị đủ các phần 5.1–5.9 theo đúng thứ tự.
- Mọi đường dẫn ảnh bắt đầu bằng `/images/5-Workshop/`.
- Không còn shortcode `notice`.
- Các trang phân biệt rõ EC2 Build Machine và ECS Fargate runtime.

## Lỗi thường gặp

| Lỗi | Nguyên nhân | Cách xử lý |
|---|---|---|
| Menu sai thứ tự | `weight` hoặc `pre` sai | Kiểm tra front matter của từng chương |
| Ảnh không hiển thị | Sai thư mục dưới `static/` | Đối chiếu đường dẫn trong danh sách ảnh |
| Liên kết trang con lỗi | Đổi tên thư mục nhưng chưa sửa link | Kiểm tra link tương đối trước khi build Hugo |

## Tóm tắt

Bộ workshop hướng dẫn từ chuẩn bị, thiết kế mạng, triển khai backend và frontend đến kiểm thử, bảo mật, chi phí và clean-up.

## Điều hướng

- Phần tiếp theo: [5.1. Tổng quan workshop](./5.1-Workshop-overview/)
