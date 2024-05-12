# Coffee machine script
#

# import libraries from secondary scripts
from coffee_machine_menu import MENU
from coffee_machine_resources import inventory
from coffee_machine_resources import profit
   

# Loop's flag
is_on = True

while is_on:
    
    # Prompt the user
    usr_prompt = input("What would you like? (espresso/latte/capuccino): ")

    # Coffee machine turns off by user order
    if usr_prompt == "off":
        is_on = False

    # Prints report when user types "report"
    elif usr_prompt == "report":
        print(f"Water: {inventory["water"]}ml")
        print(f"Coffee: {inventory["coffee"]}gr")
        print(f"Milk: {inventory["milk"]}ml")
        print(f"Money: ${profit}")
    
    # User chooces a drink
    elif usr_prompt == "espresso" or usr_prompt == "latte" or usr_prompt == "capuccino":
        drink = MENU[usr_prompt]
        print(f"Drink: {drink}")
        