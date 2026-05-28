# Security Groups

A Security Group is a virtual firewall in the cloud. It allows or blocks traffic based on rules.

## Rules need three things:
- Type (service like SSH, HTTP, HTTPS)
- Port (number like 22, 80, 443)
- Source (who is allowed, like your IP address)

## Key feature:
Security Groups are stateful — they remember your rules. You write one rule for traffic in, and the response is automatically allowed out.

## One sentence to remember
A Security Group is a cloud firewall that works based on Type, Port, and Source.
