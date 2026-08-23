name = input("Enter the s3 bucket name : ")
status = input("Do You want to allow the public access (yes/NO) : ")
if status == "yes":
    print("public access is allowed _ Security risk!")
else:
    print("Bucket is private and it is safe......")
