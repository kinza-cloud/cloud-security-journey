# MFA Checker with OR logic

username = input("enter the username : ")
password = input("Do you have password ? (yes or no ) :")
mfa = input("is mfa enabled (yes or no ) :")

if password == "yes" or mfa == "yes":
    print("Access granted")
else:
    print("Access denied")
