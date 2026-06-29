# AWS IAM Roles

## What is an IAM Role?

An IAM Role is like an identity that gives temporary permissions to users, applications, or AWS services. Instead of giving permanent access, a role gives access for a specific task.

## Analogy:

- You wear a badge to enter a building → Role gives temporary access
- You return the badge when you leave → Permissions expire after use
- Different badges for different areas → Different roles for different tasks

## Why it matters for security:

- Without IAM Roles: Users have permanent access (risky)
- With IAM Roles: Users have temporary access (safer)
- Less risk if credentials are stolen

## One sentence to remember:

IAM Roles give temporary permissions to users, applications, or services instead of permanent access.
