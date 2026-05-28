# Internet Gateway

An Internet Gateway is like a door that connects your VPC to the internet.

## Why do you need it?
- Without it, your VPC has no internet access
- With it, your public subnet can send and receive internet traffic

## How it works
1. Create an Internet Gateway
2. Attach it to your VPC
3. Tell your public subnet: "Use this gateway for internet traffic"

## One sentence to remember
An Internet Gateway is the door that connects your VPC to the internet.
