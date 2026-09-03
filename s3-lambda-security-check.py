# S3 + Lambda Security Check Simulator

bucket = input("Enter S3 bucket name: ")
public = input("Is the bucket public? (yes/no): ")
lambda_name = input("Enter Lambda function name: ")

print("\nSecurity Check Complete")
print("Bucket:", bucket)
print("Public:", public)
print("Lambda:", lambda_name)

if public == "yes":
    print("Status: Alert sent (simulated)")
else:
    print("Status: Bucket is secure")
