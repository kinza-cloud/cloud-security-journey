# CloudTrail Log Simulator

user = input("Enter your name: ")
service = input("What AWS service did you access? (S3/EC2/IAM): ")
action = input("What action did you perform? (read/write/delete): ")

print("\n📋 CloudTrail Log Entry:")
print("User:", user)
print("Service:", service)
print("Action:", action)
print("Status: Logged successfully ✅")
print("Timestamp: 2026-08-25 10:54 PM")
