# MFA Simulator

username = input("Enter username: ")
password = input("Enter password: ")
mfa_code = input("Enter MFA code: ")

print("\nMFA VERIFICATION")
print("username :", username)
print("password :", password)
print("mfa_code :", mfa_code)

if password != "" and mfa_code != "":
    print("Status : Access granted")
else:
    print("Status : Access denied")
