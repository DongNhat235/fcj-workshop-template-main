---
title: "Project Proposal"
date: 2026-07-19
weight: 2
chapter: false
pre: " <b> 2. </b> "
---

# BravelSport Web Platform

## AWS Architecture Proposal for a Secure and Scalable Deployment

### 1. Project Summary

BravelSport is a sports web platform deployed at:

`https://bravelsport.com/`

The system targets user groups such as customers, athletes, clubs, court owners, and administrators.

The main features of BravelSport include:

* Viewing the list and details of sports products.
* Searching and filtering products.
* Registering and logging in to an account.
* Managing the shopping cart.
* Placing orders and tracking order status.
* Booking sports courts.
* Managing court information and booking schedules.
* Uploading images for products and sports courts.
* Managing users, products, orders, courts, and system content.

This proposal presents a deployment plan for BravelSport on AWS using an architecture separated across frontend, backend, networking, storage, monitoring, and database layers.

The frontend is built into static files, stored on Amazon S3, and distributed through Amazon CloudFront. The domain `bravelsport.com` is registered and managed by the team through Amazon Route 53. AWS WAF is used to inspect incoming requests.

The backend is packaged with Docker, stored in Amazon ECR, and run with Amazon ECS Fargate in a private subnet. An Application Load Balancer receives API requests and forwards them to ECS tasks.

MongoDB Atlas is used as the external database. Amazon S3 stores images, media, and application configuration files. AWS IAM manages access permissions, while Amazon CloudWatch collects logs and metrics.

This architecture fits the workshop goals, MVP needs, and small-to-medium-scale systems.

---

### 2. Problems to Solve

BravelSport is not just a static website; it includes many components such as frontend, backend APIs, database, media upload, order processing, court booking, and content management.

Without a clear deployment architecture, the system may face the following issues:

* The backend is exposed directly to the Internet.
* The frontend and backend depend on the same server.
* Media is stored locally and may be lost when containers are replaced.
* Backend version management and rollback are difficult.
* There are no centralized logs to inspect errors.
* Scaling becomes difficult as user traffic increases.
* Credentials may be exposed if stored in source code.
* AWS resources may continue to generate costs after the workshop.

The proposed solution is to separate frontend, backend, media, and database. The frontend is deployed via S3 and CloudFront, the backend runs on ECS Fargate in a private subnet, and data is stored in MongoDB Atlas.

---

### 3. Implementation Objectives

The main objectives of the project are:

* Deploy BravelSport on AWS using a clear architecture.
* Separate frontend, backend, media, and database.
* Avoid exposing ECS tasks directly to the Internet.
* Use Docker to package the backend.
* Manage Docker images with Amazon ECR.
* Store media in Amazon S3.
* Collect logs and metrics through CloudWatch.
* Manage access permissions with AWS IAM.
* Support scaling by increasing the number of ECS tasks.
* Monitor costs and remove unused resources.

---

### 4. Solution Architecture

The BravelSport architecture consists of three main areas:

1. Edge and Frontend.
2. VPC and Backend.
3. Supporting services and data storage.

<!--
Place the architecture image at:
static/images/2-Proposal/bravelsport_aws_architecture.png
-->

{{< img "images/2-Proposal/bravelsport_aws_architecture.png" "BravelSport AWS Architecture" >}}

#### 4.1. Edge and Frontend

The domain `bravelsport.com` is registered and managed by the team through Amazon Route 53.

When users access the website, Route 53 performs DNS resolution and routes the domain to Amazon CloudFront.

AWS WAF is associated with CloudFront to inspect requests and reduce the risk of invalid traffic or common web attacks.

CloudFront distributes the static frontend stored in the S3 Frontend Bucket. The bucket is set to private mode and does not allow direct user access.

#### 4.2. VPC and Backend

Amazon VPC creates the network boundary for the BravelSport backend.

The Application Load Balancer and NAT Gateway are placed in a public subnet. ECS Fargate tasks are placed in a private subnet and do not have a public IP.

The Application Load Balancer is the entry point for backend traffic. The ALB forwards API requests to ECS through a target group and performs health checks to verify the status of ECS tasks.

ECS only accepts inbound traffic from the security group of the ALB. Users cannot access ECS tasks directly.

When ECS needs to access Amazon ECR, Amazon CloudWatch, Amazon S3, MongoDB Atlas, or other public endpoints, outbound traffic is routed through the NAT Gateway and Internet Gateway.

#### 4.3. Supporting Services and Storage

The supporting services include:

* Amazon ECR for storing the backend Docker image.
* Amazon CloudWatch for storing application logs and runtime metrics.
* Amazon S3 Frontend Bucket for storing the static frontend.
* Amazon S3 Media Upload for storing images and media.
* Amazon S3 Private Configuration Bucket for storing configuration files.
* AWS IAM for managing access permissions.
* MongoDB Atlas for storing application data.

Database credentials and application secrets are not stored directly in source code or Docker images.

According to the current team approach, configuration files containing credentials are stored in a private S3 bucket. This bucket should:

* Enable S3 Block Public Access.
* Enable data encryption.
* Allow access only to the ECS Task Role.
* Not provide a public URL.
* Not be shared with the S3 Frontend Bucket.
* Not be committed to GitHub.

ECS connects to MongoDB Atlas through the following path:

`ECS Fargate → NAT Gateway → Internet Gateway → MongoDB Atlas`

MongoDB Atlas should be restricted by the Elastic IP of the NAT Gateway rather than allowing a broad `0.0.0.0/0` IP range.

---

### 5. Services Used

* **Amazon Route 53:** Registers, manages the domain, and resolves DNS to CloudFront.
* **Amazon CloudFront:** Distributes the frontend and routes API requests to the ALB.
* **AWS WAF:** Inspects and filters incoming requests.
* **Amazon S3 Frontend Bucket:** Stores the static frontend.
* **Amazon VPC:** Creates the network boundary for the backend.
* **Public Subnet:** Hosts the ALB and NAT Gateway.
* **Private Subnet:** Hosts the ECS Fargate tasks.
* **Application Load Balancer:** Forwards API traffic to ECS.
* **Target Group:** Manages ECS tasks and performs health checks.
* **NAT Gateway:** Provides outbound access for ECS.
* **Internet Gateway:** Connects the public subnet to the Internet.
* **Elastic IP:** Provides a fixed public IP for the NAT Gateway.
* **Amazon ECS Fargate:** Runs the backend containers.
* **Amazon ECR:** Stores the backend Docker images.
* **AWS IAM:** Manages roles and access permissions.
* **Amazon CloudWatch:** Collects logs and metrics.
* **Amazon S3 Media Upload:** Stores images and media.
* **Amazon S3 Private Configuration Bucket:** Stores configuration files and credentials.
* **MongoDB Atlas:** Stores application data outside AWS.

---

### 6. Main Workflow

1. A user accesses the domain `bravelsport.com`.
2. Route 53 resolves DNS to CloudFront.
3. AWS WAF inspects the request.
4. CloudFront retrieves the static frontend from S3.
5. CloudFront forwards API requests to the ALB.
6. The ALB forwards requests to ECS Fargate.
7. ECS processes the business logic.
8. IAM roles grant ECS access to AWS resources.
9. ECS pulls the Docker image from Amazon ECR during startup.
10. ECS reads or writes media to Amazon S3.
11. ECS sends logs and metrics to Amazon CloudWatch.
12. ECS connects to MongoDB Atlas through the NAT Gateway.
13. The results are returned to the user through the ALB and CloudFront.

IAM is a permission relationship, not a network data path. In the diagram, the IAM connection to ECS should be shown as a dashed line.

---

### 7. Security Design

The architecture uses two main security groups.

#### SG-ALB

* Allows the required inbound traffic to the ALB.
* Allows outbound traffic to the backend port of ECS.
* Does not open unnecessary administrative ports.

#### SG-ECS

* Allows inbound traffic only from SG-ALB.
* Does not expose the backend port directly to `0.0.0.0/0`.
* Allows outbound traffic to the required services.

Other security measures include:

* ECS does not have a public IP.
* S3 buckets have Block Public Access enabled.
* IAM follows the principle of least privilege.
* Credentials stored in S3 are encrypted.
* Only the ECS Task Role can read the configuration files.
* MongoDB Atlas is restricted by the Elastic IP of the NAT Gateway.
* Credentials are not committed to GitHub.
* AWS WAF is tested before enabling blocking mode.

---

### 8. Three-Month Roadmap

#### Month 1 – Learn AWS Services

The team studies Route 53, CloudFront, WAF, S3, VPC, ALB, NAT Gateway, ECS Fargate, ECR, IAM, and CloudWatch. The team also analyzes BravelSport requirements and creates the initial architecture diagram.

**Result:** Completed documentation of AWS services and an initial architecture diagram.

#### Month 2 – Research and Testing

The team containerizes the backend with Docker, tests ECR and ECS, deploys a test frontend on S3 and CloudFront, designs the VPC, security groups, ALB, and verifies the MongoDB Atlas connection.

**Result:** Completed architecture diagram, Docker image, and prototype of the main components.

#### Month 3 – Deployment and Completion

The team deploys the frontend, backend, and networking components on AWS; integrates S3, MongoDB Atlas, IAM, and CloudWatch; tests BravelSport and completes the workshop documentation.

**Result:** BravelSport runs on AWS and the workshop guide is complete.

---

### 9. Cost and Optimization

The main cost categories include:

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

**Estimated cost:** **[TO BE CONFIRMED]**

Cost optimization measures include:

* Choosing an appropriate ECS task size.
* Reducing the run time of test resources.
* Removing NAT Gateway and ALB when no longer needed.
* Removing unused Elastic IP addresses.
* Deleting old Docker images in ECR.
* Limiting CloudWatch Logs retention time.
* Optimizing CloudFront caching.
* Monitoring costs regularly.
* Removing workshop resources after completion.

---

### 10. Risks and Mitigation

* **S3 is public:** Enable Block Public Access and verify the bucket policy.
* **Credentials are accessed improperly:** Encrypt data and limit permissions to the ECS Task Role.
* **ECS cannot pull the image:** Check ECR, IAM, and NAT Gateway configuration.
* **ALB health checks fail:** Check the port, health check path, and security group.
* **Cannot connect to MongoDB Atlas:** Check the Elastic IP, NAT route, and database credentials.
* **WAF blocks legitimate requests:** Test the rules in Count mode before switching to Block.
* **NAT Gateway costs increase:** Monitor outbound traffic and clean up resources after the workshop.
* **Media upload fails:** Check IAM, CORS, file size, and file type rules.
* **Credentials are exposed:** Do not store them in source code, Docker images, or GitHub.

---

### 11. Expected Outcomes

After the project is completed:

* BravelSport is deployed on AWS.
* The domain is registered and managed through Route 53.
* The frontend is stored on S3 and distributed through CloudFront.
* The backend runs on ECS Fargate in a private subnet.
* API traffic passes through the Application Load Balancer.
* Docker images are managed in Amazon ECR.
* Media is stored on Amazon S3.
* Data is stored in MongoDB Atlas.
* Logs and metrics are collected in CloudWatch.
* Access is controlled through IAM.
* The team has a clear testing and resource cleanup process.

---

### 12. Future Improvements

* Add CloudWatch Alarms.
* Add AWS Budgets.
* Build a CI/CD pipeline.
* Add ECS Service Auto Scaling.
* Deploy across multiple Availability Zones.
* Add VPC Endpoints to reduce traffic through the NAT Gateway.
* Move credentials to a dedicated secret management service.
* Add backup solutions for Amazon S3 and MongoDB Atlas.

---

### 13. Conclusion

The proposed architecture helps BravelSport separate frontend, backend, media, and database.

The frontend is deployed using Amazon S3 and CloudFront. The backend is packaged with Docker and runs on ECS Fargate in a private subnet.

The project domain is registered and managed with Route 53. The Application Load Balancer receives backend traffic, the NAT Gateway provides outbound access, ECR manages Docker images, CloudWatch supports monitoring, and MongoDB Atlas stores application data.

The three-month roadmap allows the team to gradually learn AWS services, study the architecture, and complete the full BravelSport deployment. The architecture meets the workshop objectives and can continue to scale in the future.
