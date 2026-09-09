# IAM Role Simulator

role = input("Enter role name: ")
service = input("Enter service that will assume the role (Lambda, EC2, User): ")
action = input("Enter action (read_s3, write_s3, delete_s3): ")

print("\nIAM Role Created")
print("Role Name:", role)
print("Trusted Service:", service)
print("Allowed Action:", action)
print("Status: Role ready for use")
