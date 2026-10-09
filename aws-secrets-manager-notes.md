# AWS Secrets Manager – Theory

## What is AWS Secrets Manager?

AWS Secrets Manager is a service that stores and protects secrets like passwords, API keys, and database credentials. It helps you avoid hard-coding secrets in your code.

## What Can Be Stored?

| Secret Type | Example |
|-------------|---------|
| Database Credentials | Username and password for RDS |
| API Keys | Third-party service keys |
| Passwords | Application passwords |
| Tokens | OAuth tokens |

## Why is Secrets Manager Important?

- Protects sensitive credentials
- Encrypts secrets using KMS
- Can rotate secrets automatically
- Works with RDS, Redshift, and other services
- Reduces risk of leaked credentials

## One Sentence to Remember

> AWS Secrets Manager keeps your passwords and keys safe — and rotates them automatically.
