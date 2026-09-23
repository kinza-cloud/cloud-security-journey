# MFA (Multi-Factor Authentication) – Theory

## What is MFA?

MFA stands for Multi-Factor Authentication. It means using two or more ways to verify your identity before you can log in.

## Why is MFA Important for Cloud Security?

Even if someone steals your password, they still cannot log in without the second factor — like a code from your phone. This adds an extra layer of security.

## Types of MFA Factors

| Factor | Examples |
|--------|----------|
| Something you know | Password, PIN |
| Something you have | Phone, hardware key (YubiKey) |
| Something you are | Fingerprint, face recognition |

## What is a Recovery Code?

A recovery code is a backup code you can use if you lose access to your MFA device. It lets you log in once, and then you should set up MFA again.

## Why is MFA Important in AWS?

- Protects the root account
- Protects IAM users
- Reduces risk of stolen passwords
- Recommended by AWS best practices

## One Sentence to Remember

> MFA adds an extra layer of security — even if your password is stolen, your account stays protected.
