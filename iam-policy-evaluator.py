action = input("Enter action (read_s3, write_s3, delete_s3): ")
allow = input("Is there an Allow policy? (yes/no): ")
deny = input("Is there a Deny policy? (yes/no): ")

print("\nIAM Policy Evaluation")
print("Action:", action)
print("Allow Policy:", allow)
print("Deny Policy:", deny)

if deny == "yes":
    print("Result: Access denied")
elif allow == "yes":
    print("Result: Access granted")
else:
    print("Result: Access denied")
