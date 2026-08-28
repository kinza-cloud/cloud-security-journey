resources = input("Enter the resources (web / database): ").strip().lower()
subnet = input("Enter subnet type (private / public): ").strip().lower()

if resources == "web" and subnet == "public":
    print(" Accessible from internet")
elif resources == "database" and subnet == "private":
    print(" Secure — no direct internet access")
elif resources == "web" and subnet == "private":
    print(" Not accessible from internet — check routing")
elif resources == "database" and subnet == "public":
    print(" Security risk! Database should not be public.")
else:
    print(" Unknown configuration. Please check your input.")
