# AWS Organizations Simulator

print("welcome to the aws organization ")
org_name = input("enter the name of your organization : ")
account1 = input("enter the first account : ")
account2 = input("enter the second account : ")

print("organizatio created")
print("organization name : ", org_name)
print("account1 : ", account1)
print("account2 : ", account2)

print("applying policy : only admin can delete the s3 bucket")
print("Status : policy applied to all account in", org_name)
