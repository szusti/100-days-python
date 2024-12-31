from coffe_machine_resources import MENU
from coffe_machine_resources import resources

def make_drink(drink):
    for ingredient in MENU[drink]["ingredients"]:
        ingredient_needed = MENU[drink]["ingredients"].get(ingredient)
        ingredient_have = resources.get(ingredient)
        ingredient_after_usage = ingredient_have - ingredient_needed
        resources[ingredient] = ingredient_after_usage
    print("Here is your drink")



def pay_for_drink(user_choice):
    money_needed = float(MENU[user_choice]["cost"])
    user_money = 0
    while True:
        added = float(input("Please put money here (for faking purposes 0 means enough)"))
        if added !=0:
            user_money += added
            print("Money in the machine", user_money)
        else:
            break
    print("Money added", user_money, 'money needed', money_needed)
    if money_needed > user_money:
        return False
    else:
        change = 0
        if user_money > money_needed:
            change = user_money - money_needed
            print("returning: ", change)
        resources['money'] += money_needed
        return True



def check_sufficient_resources(drink):
    print(MENU[drink]['cost'])
    for ingredient in MENU[drink]["ingredients"]:
        ingredient_needed = MENU[drink]["ingredients"].get(ingredient)
        ingredient_have = resources.get(ingredient)
        if ingredient_have < ingredient_needed:
            print("Not enough", ingredient)
            return False
    return True

def machine_options():
    available_options = list(MENU.keys())
    available_options.append("off")
    available_options.append("report")
    return available_options

def show_menu():
    print("Available menu options")
    print(*(item for item in MENU), sep=', ')

def home_screen(available_options):
    show_menu()
    while True:
        user_input = input("What would you like? ").lower()
        if user_input in available_options:
            return user_input
        else:
            continue

def show_available_resources():
    print("~~~~~~~~~~")
    for item in resources:
        print(item, "-", resources[item])
    print("~~~~~~~~~~")

def machine_start():
    available_options = machine_options()
    user_choice = home_screen(available_options)
    if user_choice == "off":
        return
    elif user_choice == "report":
        show_available_resources()
    else:
        if check_sufficient_resources(user_choice) == False:
            print("I'm sorry, I don't have enought ingredients to make your request")
        else:
            if pay_for_drink(user_choice) == False:
                print("Sorry, that's not enough money. Money refunded.")
            else:
                make_drink(user_choice)
    machine_start()


resources['money'] = 0
machine_start()