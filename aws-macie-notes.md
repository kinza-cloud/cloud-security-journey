# AWS Macie – Theory

## What is AWS Macie?

AWS Macie is a service that finds and protects sensitive data in S3. It uses machine learning to discover sensitive data like names, credit card numbers, and passwords.

## What Does Macie Detect?

| Data Type | Example |
|-----------|---------|
| Personal Information | Names, addresses, phone numbers |
| Financial Data | Credit card numbers, bank accounts |
| Credentials | Passwords, API keys |
| Health Data | Medical records |

## Why is Macie Important?

- Finds sensitive data in S3 buckets
- Alerts you if sensitive data is publicly exposed
- Helps with compliance (GDPR, HIPAA, PCI DSS)
- Uses machine learning — no manual checking needed
- Integrates with Security Hub for centralized view

## One Sentence to Remember

> AWS Macie is like a data detective — it finds sensitive data in your S3 buckets and warns you if it's exposed.
