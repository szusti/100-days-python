from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def welcome_screen():
    while True:
        print("Choose your drink", machine_menu.get_items())
        user_input = input()
        if user_input == "report":
            money_bank.report()
            resources.report()
        elif user_input == "off":
            quit()
        else:
            drink_item = machine_menu.find_drink(user_input)
            if drink_item != None:
                return drink_item

def run():
    selected_drink = welcome_screen()
    if not resources.is_resource_sufficient(selected_drink):
        run()
    if not money_bank.make_payment(selected_drink.cost):
        run()
    resources.make_coffee(selected_drink)
    run()




machine_menu = Menu()
money_bank = MoneyMachine()
resources = CoffeeMaker()
run()