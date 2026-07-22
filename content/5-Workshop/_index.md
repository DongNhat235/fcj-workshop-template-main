---
title: "Workshop"
date: 2026-07-19
weight: 5
chapter: false
pre: " <b> 5. </b> "
---


# Deploying BravelSport on AWS

BravelSport is an e-commerce and sports facility booking platform. Its source code includes a React/Vite frontend and a NestJS backend; the backend uses MongoDB through Mongoose, JWT for authentication, and Socket.IO for real-time chat.

This workshop describes the **target architecture and hands-on deployment process**. It does not claim that the current website is already running on the complete AWS architecture unless supporting evidence from the AWS Console is available.

## Target architecture

- The frontend is built into static files, stored in a private S3 Frontend Bucket, and distributed through CloudFront.
- AWS WAF is associated with CloudFront to inspect requests at the edge layer.
- CloudFront forwards `/api/*` and `/socket.io/*` to an Application Load Balancer.
- The ALB forwards requests through an `ip`-type Target Group to ECS Fargate tasks on port `3000`.
- Socket.IO uses `/socket.io/*` as its transport path; the chat application uses the `/chat` namespace.
- ECS Fargate runs in Private Subnets without public IP addresses.
- ECS connects to MongoDB Atlas outside the VPC through a NAT Gateway and an Internet Gateway.
- The Amazon EC2 Ubuntu instance is only a build and deployment machine; it does not receive production requests.
- S3 Media is a migration or extension component in this workshop because the current source code supports Cloudinary and local `/uploads` storage.

![BravelSport AWS Architecture](/images/5-Workshop/architecture/bravelsport-aws-architecture.png)

## Workshop contents

1. [5.1. Workshop overview](./5.1-Workshop-overview/)
2. [5.2. Prerequisites](./5.2-Prerequisite/)
3. [5.3. Building the network infrastructure](./5.3-Network-infrastructure/)
4. [5.4. Backend deployment](./5.4-Backend-deployment/)
5. [5.5. Frontend deployment](./5.5-Frontend-deployment/)
6. [5.6. Database and media](./5.6-Data-and-media/)
7. [5.7. End-to-end testing](./5.7-Testing/)
8. [5.8. Security and cost](./5.8-Security-and-cost/)
9. [5.9. Resource cleanup](./5.9-Cleanup/)

### Notes

Do not include access keys, secrets, MongoDB connection strings, JWT secrets, authentication cookies, or full Account IDs in the documentation. Values that have not been confirmed by the team must remain as `[TO BE CONFIRMED]`.

## Verification

- The Hugo menu displays all sections from 5.1 to 5.9 in the correct order.
- Every image path begins with `/images/5-Workshop/`.
- No `notice` shortcode remains.
- The pages clearly distinguish the EC2 Build Machine from the ECS Fargate runtime.

## Common issues

| Issue | Cause | Resolution |
|---|---|---|
| Menu items are in the wrong order | Incorrect `weight` or `pre` values | Check the front matter of each chapter |
| Images are not displayed | Incorrect directory under `static/` | Compare the path with the image inventory |
| Child-page links are broken | A directory was renamed without updating links | Verify relative links before building Hugo |

## Summary

This workshop covers preparation, network design, backend and frontend deployment, testing, security, cost management, and cleanup.

## Navigation

- Next section: [5.1. Workshop overview](./5.1-Workshop-overview/)
