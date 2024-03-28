# - Creates a program that ask the bidders of an auction their bid and prints the
#   highest bid.
# - There'll be a dictionary that contains the name and bid as Key and Value pairs.
# - A new bidder will be added to the dictionary each time the user answers
#   'yes' when the program asks it.
# - For secrecy purposes, the console will clear prior inputs each time the user
#   enters a new bidder.

# Import required modules
import os

# Function to clear console
def clear_console():
    os.system('cls')

# Dictionary containing the name and bid of each person
bidders = {}

# Loop through the user inputs new bidders
new_bidder = True

while new_bidder == True:
    clear_console() # clear console
    name = input("Whats your name?: ")
    bid = int(input("What is your bid? $$$: "))
    # Append the name and bid to the dictionary
    bidders[name] = bid
    
    # Ask the user if adding a new bid
    add_bid = input("Do you want to add a new bidder? (yes/no): ")
    if add_bid == "no":
        # Initialize variables to track the highest bid and bidder's name
        highest_bid = 0
        highest_bidder = ""
        # Iterate through the bidders to find the highest bid and bidder
        for bidder, bid in bidders.items(): # bidder.items() returns both keys and values
            if bid > highest_bid:
                highest_bid = bid
                highest_bidder = bidder
        
        new_bidder = False
        
print("The final list of persons subscribed for the auction is: ", bidders)
print(f"The highest bet is {highest_bid} and it was done by {highest_bidder}")