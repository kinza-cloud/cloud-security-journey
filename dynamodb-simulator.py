# AWS DynamoDB Simulator

print(".............Welcome to dynamodb.............")
user_id = input("Enter the user_id (it is key ) : ")
user_name = input("Enter the user_name ( it is the value) : ")

print("\n<<<<<<Success! Data is saved>>>>>>>")

if user_id == "":
    print("Error: User ID (Key) cannot be empty! DynamoDB requires a Primary Key.")
else:
    print("Table: Users")
    print("key is equal to :", user_id)
    print("value is equal to :", user_name)
