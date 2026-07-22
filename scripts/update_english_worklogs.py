from pathlib import Path

weeks = [
    (1, '2026-04-17', [
        ('Objectives', [
            'Get acquainted with the internship environment and company policies.',
            'Set up a personal AWS account and explore core AWS services.'
        ]),
        ('Tasks', [
            ('Mon', 'Review internship policies, meet the mentor, and clarify project requirements.', '17/04/2026', '17/04/2026', 'Internship orientation materials'),
            ('Tue', 'Create a personal AWS account and explore the AWS Management Console.', '18/04/2026', '18/04/2026', 'CloudJourney AWS study group'),
            ('Wed', 'Study AWS IAM fundamentals, create IAM users and groups, and assign basic permissions.', '19/04/2026', '20/04/2026', 'CloudJourney AWS study group'),
            ('Thu', 'Complete EC2 lab tasks, launch an instance, configure SSH key pairs, and connect to the server.', '21/04/2026', '21/04/2026', 'CloudJourney AWS study group'),
            ('Fri', 'Practice Amazon S3 object storage, create buckets, and research the internship project topic.', '22/04/2026', '23/04/2026', 'CloudJourney AWS study group')
        ]),
        ('Achievements', [
            'Successfully set up a personal AWS account and learned AWS Console basics.',
            'Completed introductory labs for IAM, EC2, and S3.',
            'Understood company culture, internship rules, and mentor expectations.',
            'Defined the initial direction for the internship project.'
        ])
    ]),
    (2, '2026-04-24', [
        ('Objectives', [
            'Learn AWS networking fundamentals and managed database concepts.',
            'Understand architecture patterns for reliable cloud deployment.'
        ]),
        ('Tasks', [
            ('Mon', 'Study Amazon RDS fundamentals and database deployment models.', '24/04/2026', '24/04/2026', 'Training materials'),
            ('Tue', 'Review AWS VPC concepts and design a secure network topology.', '25/04/2026', '25/04/2026', 'Training materials'),
            ('Wed', 'Learn architecture patterns such as monolithic, microservices, and high availability.', '26/04/2026', '26/04/2026', 'Architecture references'),
            ('Thu', 'Build a VPC and deploy an EC2 instance connected to an RDS database.', '27/04/2026', '27/04/2026', 'Hands-on lab'),
            ('Fri', 'Study the AWS Well-Architected Framework and best practice pillars.', '28/04/2026', '28/04/2026', 'AWS documentation')
        ]),
        ('Achievements', [
            'Practiced VPC and RDS configuration on AWS.',
            'Deployed an EC2 instance with an attached managed database.',
            'Understood cloud architecture patterns and reliability concepts.',
            'Reviewed the AWS Well-Architected Framework.'
        ])
    ]),
    (3, '2026-05-01', [
        ('Objectives', [
            'Explore load balancing, auto scaling, and monitoring for scalable applications.',
            'Understand DNS routing for cloud services.'
        ]),
        ('Tasks', [
            ('Mon', 'Study Elastic Load Balancing (ELB) and Auto Scaling service capabilities.', '01/05/2026', '01/05/2026', 'AWS service docs'),
            ('Tue', 'Deploy a web server with Auto Scaling and configure ELB traffic distribution.', '02/05/2026', '02/05/2026', 'Hands-on lab'),
            ('Wed', 'Configure CloudWatch monitoring for EC2 and create resource alarms.', '03/05/2026', '03/05/2026', 'Monitoring lab'),
            ('Thu', 'Research Amazon Route 53 and DNS configuration for cloud applications.', '04/05/2026', '04/05/2026', 'AWS documentation'),
            ('Fri', 'Review high availability deployment best practices.', '05/05/2026', '05/05/2026', 'Study notes')
        ]),
        ('Achievements', [
            'Learned how ELB and Auto Scaling support scalable AWS applications.',
            'Deployed a sample auto-scaling web application.',
            'Configured CloudWatch monitoring and alarms for EC2.',
            'Studied Route 53 DNS routing for cloud services.'
        ])
    ]),
    (4, '2026-05-08', [
        ('Objectives', [
            'Build a fault-tolerant AWS application using core infrastructure services.',
            'Practice command-line AWS management and NoSQL database basics.'
        ]),
        ('Tasks', [
            ('Mon', 'Complete a lab building a highly available web application with VPC, EC2, RDS, ELB, and Auto Scaling.', '08/05/2026', '08/05/2026', 'Hands-on lab'),
            ('Tue', 'Practice AWS CLI commands to manage cloud resources from the terminal.', '09/05/2026', '09/05/2026', 'AWS CLI lab'),
            ('Wed', 'Learn DynamoDB basics and perform NoSQL database operations.', '10/05/2026', '10/05/2026', 'DynamoDB lab'),
            ('Thu', 'Research AWS migration tools such as VM Import/Export and AWS DMS.', '11/05/2026', '11/05/2026', 'Migration documentation'),
            ('Fri', 'Review migration theory and prepare next-week implementation plans.', '12/05/2026', '12/05/2026', 'Study materials')
        ]),
        ('Achievements', [
            'Completed a fault-tolerant web application lab demonstration.',
            'Practiced AWS CLI management and resource automation.',
            'Gained basic knowledge of DynamoDB and NoSQL databases.',
            'Reviewed migration tools such as VM Import/Export and AWS DMS.'
        ])
    ]),
    (5, '2026-05-15', [
        ('Objectives', [
            'Understand virtualization migration workflows from on-premises to AWS.',
            'Practice VM import/export and cloud storage integration.'
        ]),
        ('Tasks', [
            ('Mon', 'Research AWS VM Import/Export capabilities and plan virtualization migration.', '15/05/2026', '15/05/2026', 'Migration documentation'),
            ('Tue', 'Prepare VMware Workstation environment and package virtual machines for upload.', '16/05/2026', '16/05/2026', 'VMware guides'),
            ('Wed', 'Use Amazon S3 and AWS CLI to upload VM images and import them into EC2 AMIs.', '17/05/2026', '17/05/2026', 'AWS CLI instructions'),
            ('Thu', 'Configure S3 bucket ACLs to support secure export and recovery workflows.', '18/05/2026', '18/05/2026', 'Storage config notes'),
            ('Fri', 'Verify permissions, validate migration steps, and clean up temporary resources.', '19/05/2026', '19/05/2026', 'Validation checklist')
        ]),
        ('Achievements', [
            'Researched VM Import/Export procedures for on-premises migration.',
            'Uploaded virtual server images to Amazon S3 and imported EC2 AMIs.',
            'Validated secure storage ACLs and migration permissions.',
            'Prepared the migration workflow for cloud deployment.'
        ])
    ]),
    (6, '2026-05-22', [
        ('Objectives', [
            'Learn AWS Database Migration Service (DMS) and migration infrastructure setup.',
            'Perform sample database migration and document the process.'
        ]),
        ('Tasks', [
            ('Mon', 'Study AWS DMS components including replication instances and endpoints.', '22/05/2026', '22/05/2026', 'DMS documentation'),
            ('Tue', 'Configure a replication instance and connect source and target databases.', '23/05/2026', '23/05/2026', 'Hands-on DMS lab'),
            ('Wed', 'Deploy a migration task and monitor sample data transfer to Amazon RDS.', '24/05/2026', '24/05/2026', 'Migration task setup'),
            ('Thu', 'Review AWS Application Migration Service (MGN) concepts for server migration.', '25/05/2026', '25/05/2026', 'MGN documentation'),
            ('Fri', 'Document lessons learned from the migration process and plan next deployment steps.', '26/05/2026', '26/05/2026', 'Study notes')
        ]),
        ('Achievements', [
            'Prepared AWS DMS infrastructure and endpoint configuration.',
            'Executed a sample database migration to Amazon RDS.',
            'Gained practical experience with cloud database migration workflows.',
            'Reviewed AWS MGN server migration capabilities.'
        ])
    ]),
    (7, '2026-05-29', [
        ('Objectives', [
            'Implement secure private access paths between on-premises and AWS resources.',
            'Automate infrastructure deployment using IaC and hybrid DNS solutions.'
        ]),
        ('Tasks', [
            ('Mon', 'Configure EC2 Instance Connect Endpoints for secure private access to instances.', '29/05/2026', '29/05/2026', 'AWS networking guide'),
            ('Tue', 'Implement hybrid DNS with Amazon Route 53 for cross-environment name resolution.', '30/05/2026', '30/05/2026', 'Route 53 documentation'),
            ('Wed', 'Explore AWS CloudFormation and write templates to automate infrastructure setup.', '31/05/2026', '31/05/2026', 'CloudFormation guide'),
            ('Thu', 'Create key pairs, initialize CloudFormation stacks, and configure security groups.', '01/06/2026', '01/06/2026', 'IaC lab'),
            ('Fri', 'Validate the hybrid infrastructure and document secure access configuration.', '02/06/2026', '02/06/2026', 'Implementation notes')
        ]),
        ('Achievements', [
            'Enabled secure private instance access with EC2 Instance Connect Endpoints.',
            'Implemented hybrid DNS routing using Route 53.',
            'Deployed infrastructure automation using CloudFormation.',
            'Standardized secure network and access configurations.'
        ])
    ]),
    (8, '2026-06-05', [
        ('Objectives', [
            'Configure private subnet outbound access and audit deployed network solutions.',
            'Optimize infrastructure and reduce unnecessary resource costs.'
        ]),
        ('Tasks', [
            ('Mon', 'Complete the NAT Gateway lab and configure secure outbound traffic for private subnets.', '05/06/2026', '05/06/2026', 'Network lab'),
            ('Tue', 'Configure route tables so private instances can access the internet for updates.', '06/06/2026', '06/06/2026', 'Routing configuration'),
            ('Wed', 'Review security and audit hybrid DNS and private access deployments.', '07/06/2026', '07/06/2026', 'Security review'),
            ('Thu', 'Optimize infrastructure deployment and remove unused test resources.', '08/06/2026', '08/06/2026', 'Cost optimization'),
            ('Fri', 'Verify the remaining architecture and document cleanup results.', '09/06/2026', '09/06/2026', 'Review notes')
        ]),
        ('Achievements', [
            'Configured NAT Gateway and route tables for secure outbound access.',
            'Verified hybrid DNS and private access solutions.',
            'Cleaned up unused resources to optimize costs.',
            'Completed a security review of network architecture.'
        ])
    ]),
    (9, '2026-06-12', [
        ('Objectives', [
            'Deploy project frontend and backend in a secure AWS environment.',
            'Validate service routing, access, and infrastructure security.'
        ]),
        ('Tasks', [
            ('Mon', 'Deploy the frontend to a private Amazon S3 bucket and configure CloudFront distribution.', '12/06/2026', '12/06/2026', 'Frontend deployment'),
            ('Tue', 'Deploy backend services on Amazon ECS Fargate and connect them to an Application Load Balancer.', '13/06/2026', '13/06/2026', 'ECS deployment'),
            ('Wed', 'Set up API and WebSocket routes through CloudFront and test end-to-end access.', '14/06/2026', '14/06/2026', 'Application routing'),
            ('Thu', 'Configure IAM roles, security groups, and environment variables for services.', '15/06/2026', '15/06/2026', 'Security configuration'),
            ('Fri', 'Review logs, resolve deployment issues, and update the architecture diagram.', '16/06/2026', '16/06/2026', 'Troubleshooting')
        ]),
        ('Achievements', [
            'Deployed the frontend through CloudFront from a private S3 bucket.',
            'Launched backend services on ECS Fargate behind an ALB.',
            'Validated API/WebSocket routing and service access.',
            'Secured the deployment with IAM and network configuration.'
        ])
    ]),
    (10, '2026-06-19', [
        ('Objectives', [
            'Document technical learning and refine business workflow diagrams.',
            'Research advanced network connectivity solutions to support the architecture.'
        ]),
        ('Tasks', [
            ('Mon', 'Research Amazon Cognito identity management and Vonage Network API integration.', '19/06/2026', '19/06/2026', 'Technical research'),
            ('Tue', 'Draft a technical blog post describing the integration solution.', '20/06/2026', '20/06/2026', 'Blog writing'),
            ('Wed', 'Design business workflow diagrams for authentication and automated notifications.', '21/06/2026', '21/06/2026', 'Workflow design'),
            ('Thu', 'Standardize workflow diagrams and review documentation handover details.', '22/06/2026', '22/06/2026', 'Documentation review'),
            ('Fri', 'Study AWS Transit Gateway capabilities and deployment use cases.', '23/06/2026', '23/06/2026', 'Network study')
        ]),
        ('Achievements', [
            'Authored a technical article summarizing Cognito and Vonage integration.',
            'Created standardized business workflow diagrams.',
            'Documented authentication and notification flows.',
            'Learned advanced AWS network architecture concepts.'
        ])
    ]),
    (11, '2026-06-26', [
        ('Objectives', [
            'Implement cost monitoring and cleanup best practices for AWS resources.',
            'Finalize technical documentation and project handover materials.'
        ]),
        ('Tasks', [
            ('Mon', 'Configure AWS Budgets and Cost Explorer to monitor spending and detect anomalies.', '26/06/2026', '26/06/2026', 'Billing tools'),
            ('Tue', 'Review active AWS resources and clean up temporary trial deployments.', '27/06/2026', '27/06/2026', 'Resource audit'),
            ('Wed', 'Document cleanup procedures and cost monitoring results.', '28/06/2026', '28/06/2026', 'Documentation notes'),
            ('Thu', 'Write and finalize a technical article on ransomware defense architecture.', '29/06/2026', '29/06/2026', 'Article drafting'),
            ('Fri', 'Share findings with the mentor and prepare final handover materials.', '30/06/2026', '30/06/2026', 'Presentation preparation')
        ]),
        ('Achievements', [
            'Configured AWS cost monitoring using Budgets and Cost Explorer.',
            'Performed a resource audit and cleaned up trial infrastructure.',
            'Completed security documentation and a technical article.',
            'Prepared final handover materials for the project.'
        ])
    ]),
    (12, '2026-07-03', [
        ('Objectives', [
            'Complete the final internship report and finalize project documentation.',
            'Review results, lessons learned, and improvement opportunities.'
        ]),
        ('Tasks', [
            ('Mon', 'Review all weekly worklogs and consolidate the final internship report.', '03/07/2026', '03/07/2026', 'Final report preparation'),
            ('Tue', 'Update architectural diagrams, service selection rationale, and operational workflows.', '04/07/2026', '04/07/2026', 'Documentation update'),
            ('Wed', 'Summarize achieved results, project limitations, and future improvement ideas.', '05/07/2026', '05/07/2026', 'Project summary'),
            ('Thu', 'Compile supporting data, verify references, and finalize evaluation documentation.', '06/07/2026', '06/07/2026', 'Quality review'),
            ('Fri', 'Submit the final report to the supervisor and complete the internship handover.', '07/07/2026', '07/07/2026', 'Final submission')
        ]),
        ('Achievements', [
            'Completed the internship final report and documentation.',
            'Updated architecture diagrams and operational workflows.',
            'Summarized results, limitations, and future improvements.',
            'Prepared the project for evaluation and handover.'
        ])
    ])
]

root = Path('content/1-Worklog')
for week, date, sections in weeks:
    folder = root / f'1.{week}-Week{week}'
    file_path = folder / '_index.md'
    if not folder.exists():
        print(f'Missing folder {folder}')
        continue
    lines = [
        '---',
        f'title: "Week {week} Worklog"',
        f'date: {date}',
        f'weight: {week}',
        'chapter: false',
        f'pre: " <b> 1.{week}. </b> "',
        '---',
        ''
    ]
    for section_title, items in sections:
        lines.append(f'### Week {week} {section_title}:')
        if section_title == 'Tasks':
            lines.append('| Day | Task | Start Date | End Date | Reference |')
            lines.append('| --- | --- | --- | --- | --- |')
            for day, task, start, end, ref in items:
                lines.append(f'| {day} | {task} | {start} | {end} | {ref} |')
            lines.append('')
            continue
        for item in items:
            lines.append(f'* {item}')
        lines.append('')
    file_path.write_text('\n'.join(lines).rstrip() + '\n', encoding='utf-8')
    print(f'Updated {file_path}')
