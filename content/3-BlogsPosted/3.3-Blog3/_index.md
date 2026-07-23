---
title: "Blog 3"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 3.3. </b> "
---

# Modernizing SignalR with AWS AppSync Event API

Hi everyone, I recently came across a very interesting topic regarding Modernizing SignalR with AWS AppSync Event API. Simply put, it explores how to modernize the real-time architecture of a .NET/React application by migrating from a traditional SignalR setup to the AWS AppSync Event API.

In real-time applications—such as order notifications, live dashboards, delivery status updates, chat apps, or publish/subscribe systems—SignalR is commonly used to maintain WebSocket connections between the server and clients. However, as the system scales, development teams often run into operational hurdles. These include managing hundreds of thousands of concurrent WebSocket connections, keeping servers constantly running, and configuring sticky sessions or a Redis backplane to scale out across multiple server instances.

Looking at the diagram, the new architecture is streamlined into 4 main flows:

Flow 1:
Users access the application via the React Client. When a real-time action occurs—such as placing an order or triggering a new event—the React Client initiates a request to the .NET API Server.

Flow 2:
Instead of hard-coding AppSync connection details into the source code, the .NET API Server fetches essential information like API keys or endpoints securely from AWS Secrets Manager. This ensures secure secret management and simplifies credential rotation.

Flow 3:
After processing the business logic, the .NET API Server publishes the event to the AWS AppSync Event API via a standard HTTP request. Instead of the backend server manually managing individual WebSocket connections (as it would with SignalR), it offloads that responsibility by simply pushing the event to AppSync.

Flow 4:
AWS AppSync takes care of the pub/sub (publish/subscribe) mechanism and pushes the events to Subscribers in real time over WebSockets. Users or clients subscribed to the channel receive instant updates without the need for constant polling.

The beauty of this architecture lies in decoupling the backend from WebSocket connection management. In a traditional SignalR environment, the server must keep track of connection states, manage groups, map user connections, and handle infrastructure scale-out. With the AppSync Event API, AWS fully manages the connections, event distribution, elasticity, and infrastructure high availability.

**To put it simply:**
Traditional SignalR: The server handles both business logic and WebSocket connection management.

AWS AppSync Event API: The .NET API Server focuses solely on business logic and publishing events. AppSync takes over the heavy lifting of real-time event distribution to all subscribers.

This architecture is a perfect fit for use cases like real-time notifications, live dashboards, order tracking, collaborative applications, IoT data distribution, or any system requiring fan-out event delivery (broadcasting an event to multiple clients simultaneously).

Furthermore, leveraging AWS Secrets Manager separates sensitive configuration from the codebase. In a production environment, you can seamlessly integrate IAM for access control, CloudWatch and CloudTrail for monitoring publish/subscription errors, and isolated dev/staging/prod environments to enhance security and operational control.

**Key Takeaway**
The key takeaway from this diagram is that modernizing SignalR doesn't mean abandoning real-time capabilities. Instead, it means offloading the complexities of WebSocket infrastructure to a fully managed, serverless AWS service. This drastically reduces operational overhead, simplifies scaling, and allows the team to focus entirely on core business logic.

**Conclusion**
AWS AppSync Event API offers a compelling alternative for .NET/React applications that require real-time, pub/sub communication. With this architecture, your backend stays lean, your frontend still gets instant updates, and AWS manages the complex WebSocket infrastructure behind the scenes.

{{< img "images/3-Blog/blog3.png" "images from blog" >}}

[...Link...](https://www.facebook.com/groups/awsstudygroupfcj/permalink/2206455833452710/?rdid=geoKRLwi2jjUs3tZ#)
