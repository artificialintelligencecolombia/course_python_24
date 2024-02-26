# This program calculates the total amount to be paid per person, considering a given bill amount
# and a specified tip percentage.

# 1. Input the required values for the calculation
total_bill_str = input("What's the total bill to pay?: $")
groups_number = input("What's the number of people to pay  the bill?: ")
tip_percentage = input("What's the tip percentage (%) you want to pay? (10 - 12 - 15): ")

# 2. Perform the calculation -> total_bill * 1,<tip_percentage> / total_of_people
bill_per_person = round((float(total_bill_str) * (1 + (float(tip_percentage)/100))) / int(groups_number), 2)


print(f"\nEach person should pay ${bill_per_person} dollars.")