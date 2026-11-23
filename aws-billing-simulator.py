# AWS Billing Alarm Simulator

print("welcome to the aws billing system")
budget = int(input("enter your monthly budget in dollars (e.g.50) :"))
current_spend = int(input("enter your current aws spending in dollars : "))

print("...analyzing your aws account.....")

if current_spend > budget:
    print("warning budget is exceeded your budget!")
    print("current spend :", current_spend)
    print("budget :", budget)
    print("please check your limit")
else:
    print("Status: Your spending is under control.")
    print("Remaining Budget: $", budget - current_spend)
