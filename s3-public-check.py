bucket = input("Enter S3 bucket name: ")
status = input("Is this bucket public? (yes/no): ")

if status == "yes":
    print("SECURITY RISK: Make it private!")
else:
    print("Bucket is secure.")
