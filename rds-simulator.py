# AWS RDS Connection Simulator

print("welcome to rds")
db_engine = input("which database your using (mysql /postgres) : ")
username = input("Enter your username : ")
password = input("Enter your password : ")

print("\n<<<<<<connecting to rds >>>>>>")

if db_engine == "mysql" or db_engine == "postgres":
    if username == "admin" and password == "1234":
        print("successfully connecting to your rds : ")
    else:
        print("Access Denied. Incorrect username or password.")
else:
    print("Error , unsupported database engine")
