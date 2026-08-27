# VPC Security Simulator – Security Group Rule Checker

port = input("Enter the port number: ")
decision = input("Allow or Deny? (allow/deny): ")

if decision == "allow":
    print("✅ Port", port, "is open.")
else:
    print("❌ Port", port, "is blocked.")
