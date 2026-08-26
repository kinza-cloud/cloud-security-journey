# AWS CloudTrail – Complete Notes

## What is CloudTrail?

CloudTrail keeps an eye on every activity in your AWS account. It records who did what, when, and from where. It's like a **security camera** for your cloud.

## Why CloudTrail Matters:

- You can see **who** did **what** and **when**
- Provides **proof** if something goes wrong
- Helps with **security investigations**
- Important for **AWS exams and real-world jobs**

## Types of Events CloudTrail Records:

| Event Type | What It Logs |
|------------|--------------|
| **Management Events** | Actions that change resources (like launching EC2) |
| **Data Events** | Actions on data (like reading a file from S3) |
| **Insight Events** | Unusual activity (like unexpected API calls) |

## Who Can View CloudTrail Logs?

- Only users with **IAM permissions** can access CloudTrail logs
- IAM controls who can view or manage logs

## One Sentence to Remember:

> *CloudTrail records every action in your AWS account — like a security camera for your cloud.*
