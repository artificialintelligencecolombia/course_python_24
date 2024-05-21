# Recreate the coffee machine script, this time by using OOP paradigm

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Instantiate the objects, allowing to use their methods and attrs
my_menu = Menu()
my_coffee_maker= CoffeeMaker()
my_money_machine = MoneyMachine()

is_on = True

while is_on: 
    # 1. Print report of ingredients and money
    my_coffee_maker.report()
    my_money_machine.report()

    # Take the order and check if correct
    user_order = input(f"What do you want to drink? ({my_menu.get_items()}): ")
    drink = my_menu.find_drink(user_order)
    #print(drink)

    # Check if MenuItem obj exists in menu attr
    if drink:
        # 2. Check availability of resources
        if my_coffee_maker.is_resource_sufficient(drink):
            # 3. Process coins
            # 4. Check success of transaction
            if my_money_machine.make_payment(drink.cost):
                # 5. Make coffe 
                my_coffee_maker.make_coffee(drink)

    # 4. Check success of transaction



