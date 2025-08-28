amount_due = 50
while amount_due > 0:
    print("Amount Due:",amount_due)
    payment = int(input("insert coin:"))
    if payment in [25,10,5]:
        amount_due -= payment
    else:
        continue
print("Change Owed:",abs(amount_due))




