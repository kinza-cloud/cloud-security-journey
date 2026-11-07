# Route 53 (DNS) Simulator

print("<<<<<<Welcome to the r53 DNS>>>>>")
domain = input("which website you are visiting : ")
print("looking up for the search web ip address")

if domain == "google.com":
    print("found ip address is equal to 142.250.190.46")
    print("connecting to the google")
elif domain == "myweb.com":
    print("found ip address of myweb.com is 192.168.1.50")
    print("connecting to web.com")
elif domain == "amazon.com":
    print("found ip address is equal to 205.251.242.103")
    print("connecting to the amazon.com")
else:
    print("Error domain not found in route53")
