# Credential Report Simulator

username = input("Enter username: ")
mfa_enabled = input("Is MFA enabled? (yes/no): ")
password_age = input("Enter password age in days: ")
access_key_used = input("Was access key used recently? (yes/no): ")

print("\nIAM Credential Report")
print("Username:", username)
print("MFA Enabled:", mfa_enabled)
print("Password Age (days):", password_age)
print("Access Key Used Recently:", access_key_used)

if mfa_enabled == "yes" and int(password_age) < 90:
    print("Status: User credentials are secure")
else:
    print("Status: User credentials need attention")
