# AWS Security Hub Dashboard Simulator

print("welcome to the aws security hub ")
guardduty_alerts = int(input("Enter the number the guardduty threat alerts : "))
inspector_alerts = int(input("Enter the num of the inspector alerts : "))
iam_alerts = int(input("Enter the number of the iam_alerts : "))

print("guardduty is :", guardduty_alerts)
print("iam alerts :", iam_alerts)
print("inspectors :", inspector_alerts)

total_alerts = guardduty_alerts + inspector_alerts + iam_alerts

if total_alerts > 0:
    print("warning check the security : ")
    print("something abnormal going in it")
else:
    print("Security is perfect.")
