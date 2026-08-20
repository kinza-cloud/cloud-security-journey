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
---

## 🔐 VPC Security Best Practices (For Cloud Security Engineers)

| Practice | Why It Matters |
|----------|----------------|
| **Use Private Subnets for Databases** | Never expose databases to the internet |
| **Restrict Security Groups** | Only open necessary ports (e.g., port 22 only from your IP) |
| **Use Network ACLs as Defense-in-Depth** | Extra layer of security (stateless = more control) |
| **Enable VPC Flow Logs** | Log all traffic for monitoring and audits |
| **Use Bastion Host (Jump Box)** | Securely access private EC2 instances |
| **Avoid Public IPs for Private Resources** | Reduce attack surface |

---

## 🧠 Real-World Security Scenario:

> *"You have a web server in a public subnet and a database in a private subnet. The web server needs to talk to the database."*

**How to do it securely:**
- Web server → Public subnet (port 80/443 open)
- Database → Private subnet (no public access)
- Security Group rule: Allow traffic from web server's SG to database on port 3306 (MySQL)

✅ This keeps your database **isolated** and **secure**!

---

## 🐍 Python + VPC (Simulation)

Write a script that asks:
- "Is this EC2 in a public or private subnet?"
- If public → print "⚠️ Ensure Security Groups are locked down!"
- If private → print "✅ Good — no direct internet access."

---

## 🐧 Linux + VPC (Command to Remember)

Check your own network info:
```bash
ip addr show
