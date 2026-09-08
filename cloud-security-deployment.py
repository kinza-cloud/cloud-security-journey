# Cloud Security Deployment - IAM + Lambda + S3 Simulator

bucket = input("Enter bucket name: ")
public = input("Is the bucket public? (yes/no): ")
lambda_name = input("Enter Lambda function name: ")
role = input("Enter IAM role name: ")

print("\nCloud Security Deployment")
print("Bucket:", bucket)
print("Public:", public)
print("Lambda:", lambda_name)
print("IAM Role:", role)
print("Status: Deployment simulated successfully")
