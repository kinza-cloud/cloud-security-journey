username=input("Enter IAM username:")
role=input("Enter your role (admin/developer/viewer):")
print("\n Access Details:")
print("......")
print("user : ",username)
if role == "admin":
    print("......Role is Admin......")
    print("can create, read, update, and delete any resource")
elif role == "developer":
    print("......Role is developer......")
    print("can create, read, update ")
    print("cannot delete any resource")
elif role == "viewer":
    print("......Role is viewer......")
    print("can read only ")
    print("cannot create , update, delete any resource")
else:
    print("Unknown role......Please enter admin,developer,viewer......")
