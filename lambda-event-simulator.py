# Lambda Event Simulator

source = input("Enter event source (s3, api, cloudtrail, schedule): ")
name = input("Enter your name: ")

print("\nLambda Event Log")
print("Event Source:", source)
print("Triggered By:", name)

if source == "s3":
    print("Action: File uploaded successfully")
elif source == "api":
    print("Action: API request processed")
elif source == "cloudtrail":
    print("Action: API call logged")
elif source == "schedule":
    print("Action: Scheduled task executed")
else:
    print("Action: Unknown event source")

print("Status: Success")
