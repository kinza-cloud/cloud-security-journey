# S3 + CloudTrail Simulator

bucket = input("Enter bucket name: ")
user = input("Who accessed it? ")
action = input("What action did they perform? (upload/download/delete): ")

print("\n CloudTrail Event:")
print("Bucket:", bucket)
print("User:", user)
print("Action:", action)
print("Status: Logged Successfully ")
