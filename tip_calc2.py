bill_amt = float(input("Total bill amount?"))
service_level = input("Level of service? Enter 'good', 'fair' or 'bad'.")
if (service_level != "good") and (service_level != "fair") and (service_level != "bad"):
    service_level = input("Please enter 'good', 'fair' or 'bad'.")

split = float(input("Split how many ways?"))

if service_level == "good":
    tip_perc = .2
elif service_level == "fair":
    tip_perc = .15
elif service_level == "bad":
    tip_perc = .1


tip = bill_amt * tip_perc
total_bill = bill_amt + tip
cpp = total_bill / split

print(("Tip amount: $%.2f \nTotal amount: $%.2f \nCost per person: $%.2f") %(tip, total_bill, cpp))
