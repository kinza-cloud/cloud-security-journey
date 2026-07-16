# VPC Deep Dive

## What is VPC?

VPC stands for Virtual Private Cloud. It is a private network inside AWS where you can launch your resources (like EC2, RDS).

## Key Components:

| Component | What it does |
|-----------|--------------|
| Subnet | A smaller network inside VPC (public or private) |
| Internet Gateway | Connects VPC to the internet |
| NAT Gateway | Allows private subnet to access internet (outbound only) |
| Route Table | Directs traffic where to go |
| Security Group | Firewall for EC2 instances |
| Network ACL | Firewall for subnets (stateless) |

## Why VPC is Important for Security:

- Resources are isolated and secure
- Full control over traffic
- Easier to protect data

## One sentence to remember:

VPC is your own private network in the cloud where you control IPs, subnets, and firewalls.
