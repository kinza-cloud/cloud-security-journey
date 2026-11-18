# AWS GuardDuty Threat Simulator

print("Welcome to aws guard duty")
username = input("Enter the username : ")
location = input("Enter the location (russia, pakistan): ")
failed_attempt = int(input("Enter the failed attempt : "))

print("\nanalyzing behaviour with machine learning")

if location == "russia" or failed_attempt > 5:
    print("Threat detectd : suspicious login activity from russia")
    print("Action: blocking ip and alerting the administrator")
else:
    print("access granted")
