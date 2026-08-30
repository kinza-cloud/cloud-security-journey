username = input("Enter IAM username: ")
bucket = input("Enter S3 bucket name: ")
action = input("What action did they perform? (upload/download/delete): ")

print("\nIAM User:", username)
print("S3 Bucket:", bucket)
print("Action:", action)
print("Logged to CloudTrail successfully.")

if action == "delete":
    print("Security Status: Risky action — review immediately.")
else:
    print("Security Status: Secure action — no concern.")
