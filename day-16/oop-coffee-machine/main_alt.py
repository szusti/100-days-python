from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
money_machine = MoneyMachine()
coffe_maker = CoffeeMaker()

while True:
    print(menu.get_items())
    userInput = input("What would you like Sir/Madam\n")
    if userInput == "off":
        break
    menuDrink = menu.find_drink(userInput)
    if menuDrink:
        coffe_maker.report()
        if coffe_maker.is_resource_sufficient(menuDrink) and money_machine.make_payment(menuDrink.cost):
                coffe_maker.make_coffee(menuDrink)
    elif userInput == "report":
        money_machine.report()
        coffe_maker.report()
