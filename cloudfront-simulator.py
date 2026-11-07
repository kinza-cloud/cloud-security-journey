# CloudFront Delivery Simulator

print("\n <<<<<<cloud fromat delivery >>>>>>")
content = input("enter the content : ")
location = input("enter the location : ")

print("<<<<<<requested content>>>>> ")

if location == "pakistan":
    print("pakistan delivery edge near the karachiii")
elif location == "usa":
    print("usa delivery then edge near the new york")
elif location == "uk":
    print("uk delivery then edge near the london")
else:
    print("deliver slow from the s3 bucket")

print("Delivery Complete")
