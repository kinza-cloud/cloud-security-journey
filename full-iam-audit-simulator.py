# Full IAM Audit Simulator

print("Full IAM Security Audit\n")

root_mfa = input("Is MFA enabled on root? (yes/no): ")
users_mfa = input("Do all users have MFA? (yes/no): ")
keys_rotated = input("Have access keys been rotated? (yes/no): ")
unused_permissions = input("Are there unused permissions? (yes/no): ")
cloudtrail_enabled = input("Is CloudTrail enabled? (yes/no): ")

print("\nAudit Report")
print("Root MFA:", root_mfa)
print("Users MFA:", users_mfa)
print("Keys Rotated:", keys_rotated)
print("Unused Permissions:", unused_permissions)
print("CloudTrail Enabled:", cloudtrail_enabled)

if root_mfa == "yes" and users_mfa == "yes" and keys_rotated == "yes" and unused_permissions == "no" and cloudtrail_enabled == "yes":
    print("\nStatus: Account is secure")
else:
    print("\nStatus: Account needs improvement")
