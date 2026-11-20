# AWS Shield DDoS Simulator

print("welcome to aws shield")
website = input("Enter the website : ")
traffic = int(input("enter the traffic : "))

print("\naws shield traffic analyzer")

if traffic > 1000:
    print("lot of traffic")
    print("alarm ddos attack is happening")
    print("website status : online and protected")
else:
    print("Traffic looks normal")
    print("website status : online")
