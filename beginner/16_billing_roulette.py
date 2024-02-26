# the user will input any number of friends names. Then he will input the total 
# bill of the restaurant and the script will select randomly one of them to pay
# the bill.

import random

print("WELCOME TO THE BILLING ROULETTE")
friends_list = []

while True:
    friend_name = input("\nEnter a friend's name to the list: ")
    friends_list.append(friend_name)
    print(f"{friend_name} was added to the list.")
    add_friends = input("\nDo you want to add a friend? (yes/no): ").lower()
    
    if add_friends == 'no':
        break
print("The total group of friends is: ")
for friend in friends_list:
    print(friend, end= '\n')

total_bill = int(input("What's the bill to pay to the restaurant?: $"))

roulette = random.randint(0, len(friends_list))
print(f"{friends_list[roulette]} is going to pay ${total_bill} for the meals today.")
