# AWS WAF Traffic Simulator

print("welcome to aws waf")
ip_address = input("Enter the ip address : ")
request = input("Enter the request (normal/sql_injection/xss) : ")

print("\nanalizing the request from the ip_address", ip_address)

if request == "sql_injection" or request == "xss":
    print("malicious request come :")
    print("action : blocking the request", ip_address)
    print("status: Traffic denied by waf")
else:
    print("request look normal:")
    print("Action : allowing the traffic")
    print("status: request sent to the server")
