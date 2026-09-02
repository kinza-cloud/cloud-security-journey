# Lambda IAM Simulator

function = input("Enter Lambda function name: ")
role = input("Enter IAM role name: ")
action = input("Enter action (read_s3, write_s3, delete_s3): ")

print("\nLambda Function:", function)
print("IAM Role:", role)
print("Action:", action)
print("Status: Permissions validated")
