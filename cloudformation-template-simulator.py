# CloudFormation Template Simulator with Parameters

stack_name = input("Enter stack name: ")
bucket_name = input("Enter S3 bucket name: ")
instance_type = input("Enter EC2 instance type (t2.micro, t3.medium): ")

print("\nCloudFormation Template")
print("Stack Name:", stack_name)
print("S3 Bucket:", bucket_name)
print("EC2 Instance:", instance_type)
print("Status: Template ready for deployment")
