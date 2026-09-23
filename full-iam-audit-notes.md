# Full IAM Security Audit – Theory

## What is a Full IAM Security Audit?

A full IAM security audit is a complete check of all IAM settings and activity in your AWS account. It helps you make sure everything is secure and no one has unnecessary access.

## Why Audit the Root Account First?

The root account has full access to everything in AWS. It is the most powerful account. If someone gets into it, they can do anything. So it must be:

- Protected with MFA
- Used only for setup (not daily work)
- Monitored carefully

## 3 Things to Check in an IAM Audit

1. Root MFA – Is MFA enabled on the root account?
2. User MFA and Password Age – Do all users have MFA? Are passwords old?
3. Unused Permissions and Access Keys – Are there permissions or keys that are not being used?

## Why is IAM Audit Important for Cloud Security?

- It finds weak spots in your account
- It enforces least privilege
- It removes unnecessary access
- It helps with compliance and auditing
- It reduces the risk of attacks

## One Sentence to Remember

> A full IAM security audit checks everything in your AWS account — starting with the root account — to keep it safe and secure.
