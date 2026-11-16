# AWS CloudWatch Alarm Simulator

print("Welcome to cloud watch")
server_name = input("Entre the servr_Name  web server: ")
cpu_usage = int(input("Enter the current cpu percent : "))

if cpu_usage > 80:
    print("Warning to please check it")
    print("something goes wrong so check it")
elif cpu_usage > 50:
    print("cpu is moderate")
else:
    print("ok cpu is good not so high", cpu_usage, "% (healthy)")
