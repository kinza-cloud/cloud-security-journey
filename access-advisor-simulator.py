# Access Advisor Simulator

username = input("Enter username: ")
service_used = input("Enter service used (S3, EC2, Lambda): ")
last_used_days = int(input("Enter days since last used: "))

print("\nIAM Access Advisor Report")
print("Username:", username)
print("Service Used:", service_used)
print("Days Since Last Used:", last_used_days)

if last_used_days > 90:
    print("Recommendation: Remove unused permission")
else:
    print("Recommendation: Keep permission — recently used")
