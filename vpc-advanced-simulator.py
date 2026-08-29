resource = input("Enter resource type (web/database): ")
subnet = input("Enter subnet type (public/private): ")
protocol = input("Enter protocol (TCP/UDP): ")
port = input("Enter port number: ")

print("\n Security Rule Summary:")
print("Resource:", resource)
print("Subnet:", subnet)
print("Protocol:", protocol)
print("Port:", port)

if subnet == "public":
    print("Action: ALLOW")
    print("Status:  Rule applied successfully.")
else:
    print("Action: DENY")
    print("Status: Rule blocked for security.")
