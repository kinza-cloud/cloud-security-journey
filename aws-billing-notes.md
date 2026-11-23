# AWS Billing & Cost Explorer – Theory

## What is AWS Cost Explorer?
Cost Explorer is a tool that visualizes your AWS spending. It shows charts of where your money is going (like EC2, S3, etc.) and helps you forecast future bills.

## What is a Billing Alarm?
A Billing Alarm is a limit you set (e.g., $10). If your AWS bill goes above that limit, CloudWatch sends you an email alert. 

## Why is this important?
If a hacker gets into your account, they might spin up hundreds of servers to mine cryptocurrency. Without a billing alarm, you wouldn't know until you get a massive bill. Billing alarms protect you financially.
