# Account Security Checker

root_mfa = input("Is MFA enabled on root account? (yes/no): ")
access_keys_rotated = input("Have access keys been rotated recently? (yes/no): ")
cloudtrail_enabled = input("Is CloudTrail enabled? (yes/no): ")
billing_alarm = input("Is a billing alarm set? (yes/no): ")

print("\nAccount Security Report")
print("Root MFA:", root_mfa)
print("Access Keys Rotated:", access_keys_rotated)
print("CloudTrail Enabled:", cloudtrail_enabled)
print("Billing Alarm Set:", billing_alarm)

if root_mfa == "yes" and cloudtrail_enabled == "yes":
    print("Status: Account is secure")
else:
    print("Status: Account needs improvement")
