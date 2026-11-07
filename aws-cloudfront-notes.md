# AWS CloudFront – Theory

## What is AWS CloudFront?

AWS CloudFront is a Content Delivery Network (CDN). It delivers content (like data, videos, and websites) to users quickly and securely.

## How Does It Work?

- It stores copies (caches) of your original data in **Edge Locations** around the world.
- When a user requests data, CloudFront delivers it from the Edge Location closest to them.

## Why is CloudFront Important?

- **Faster delivery:** Users get content from a nearby location instead of a distant S3 bucket.
- **Lower latency:** Less delay for the user.
- **Security:** Integrates with AWS Shield for DDoS protection and AWS WAF for firewall security.

## One Sentence to Remember

> AWS CloudFront is a global delivery system that caches your data near users so they can access it faster.
