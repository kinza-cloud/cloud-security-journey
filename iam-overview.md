# IAM (Identity and Access Management)

## What is IAM?

IAM stands for Identity and Access Management. It controls who can access what in the cloud.

## Three parts of IAM:

| Part | Meaning |
|------|---------|
| **Identity** | Who are you? (username, password, ID) |
| **Access** | What can you do? (read, write, delete) |
| **Management** | Who gives permissions? (Admin) |

## One sentence to remember:

IAM is like a security guard that checks your ID and says, "You can enter this room, but not that one."
## IAM in One Sentence:

> IAM is like a **security guard** who checks your ID and says:  
> *"You can enter this room, but not that one."*

## Python + IAM (Quick Check):

```python
user = input("Enter your role: ")
if user == "admin":
    print("Full access")
else:
    print("Limited access")
