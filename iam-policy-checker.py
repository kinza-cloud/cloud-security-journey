username = input("Enter username: ")
action = input("Enter action (read_s3, write_s3, delete_s3): ")
allowed = input("Is this action allowed? (yes/no): ")

print("\nIAM Policy Check")
print("User:", username)
print("Action:", action)
print("Allowed:", allowed)

if allowed == "yes":
    print("Status: Access granted")
else:
    print("Status: Access denied")
