# Route 53 DNS Simulator with While Loop

print("<<<<<<Welcome to the domain r53 route>>>>>")
print("Type exist if you want to move out from it")

while True:
    domain = input("Enter the your web name : ")
    
    if domain == "exit":
        print("goodbye.........you will be out of DNS")
        break
        
    elif domain == "google.com":
        print("found ip address is 142.250.190.46")
        
    elif domain == "amazon.com":
        print("found ip address is 205.251.242.103")
        
    elif domain == "myweb.com":
        print("found ip address is 192.168.1.50")
        
    else:
        print("Error domain not found in route53")
