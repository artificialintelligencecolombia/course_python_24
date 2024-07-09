# Coffee machine script
#

# import libraries from secondary scripts
from intermediate.coffee_machine_procedural.coffee_machine_menu import MENU
from intermediate.coffee_machine_procedural.coffee_machine_resources import inventory
from intermediate.coffee_machine_procedural.coffee_machine_resources import profit


is_on = True # Loop's flag
profit = 0 # Money on the machine

# Function for checking ingredients availability
def ingredients_available(order_ingredients):
    """Check if the required ingredients are available in the inventory.
    This function iterates through a dictionary of order ingredients and checks if each required ingredient quantity is available in the inventory. If any ingredient is insufficient, it prints an error message and returns False immediately. If all ingredients are sufficient, it returns True.

    Args:
        order_ingredients (dict): A dictionary where the keys are ingredient names and the values are the quantities required for the order.

    Returns:
        bool: True if all required ingredients are available in the required quantities, False otherwise.
    
    """
    for item in order_ingredients:
        if order_ingredients[item] >= inventory[item]:
            print(f"Sorry, there is not enough {item}") 
            return False
    return True


# Function for calculating the coins inserted by user
def process_coins():
    """Prompts the user to insert the coins and returns the money amount.

    Returns:
        float: the total amount of money inserted in coins
    """
    print("Please insert coins.")
    total = int(input("How many quarters ($0.25): ")) * 0.25
    total += int(input("How many dimes ($0.1): ")) * 0.1
    total += int(input("How many nickels ($0.05): ")) * 0.05
    total += int(input("How many pennies ($0.01): ")) * 0.01
    return total
   
  
def transaction_checking(money_received, drink_cost):
    """Returns True if the money received is enough o

    Args:
        money_received (float): _description_
        drink_cost (dict value): _description_

    Returns:
        _type_: _description_
    """
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is you change_ ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, there is not enough money.") 
        return False
  
def make_coffee(drink_name, order_ingredients):
    
    for item in order_ingredients:
        inventory[item] -= order_ingredients[item]
        print(f"Here is your {drink_name}")
        
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
            if ingredients_available(drink["ingredients"]):
                user_payment = process_coins()
                if transaction_checking(user_payment, drink["price"]):
                   make_coffee(drink, drink["ingredients"])
                   