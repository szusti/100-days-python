import coffe_machine_resources
CHOICES = ["off","report","espresso","latte","cappuccino"]

def welcome_screen():
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        if choice in CHOICES:
            return choice

def get_report():
    print(coffe_machine_resources.resources,"\nMoney: ",coffe_machine_resources.money)

def buy_a_coffee(user_choice):
    """Function responsible for checking available resources, process coins and return drink"""
    if check_resources(user_choice):
        if payment(coffe_machine_resources.MENU[user_choice]["cost"]):
            print("Transactions successful")
            get_coffee(user_choice)
        else:
            print("Transactions unsuccessful")

def check_resources(user_choice):
    selected_cofee = coffe_machine_resources.MENU[user_choice]["ingredients"]
    for resource_value in selected_cofee:
        if selected_cofee[resource_value] > coffe_machine_resources.resources[resource_value]:
            print(f"Sorry, there is not enough {resource_value}")
            return False
    return True

def payment(amount_needed):
    print("Amount of money needed", amount_needed)
    while True:
        coins = input("*waiting for coins*\n")
        try:
            coins = float(coins)
            break
        except ValueError:
            print("please insert coins, or to exit, press [e]")
        if coins == "e":
            print("exit")
            return False
    coins = float(coins)
    if coins < amount_needed:
        print("Not enough, here is your money back")
        return False
    if coins > amount_needed:
        print(f"Here is your change {coins - amount_needed}")
    coffe_machine_resources.money+=amount_needed
    return True

def get_coffee(user_choice):
    print("Bzzzzzzzzzzzz making a cofee Bzzzzzzzzz")
    selected_cofee = coffe_machine_resources.MENU[user_choice]["ingredients"]
    for resource_value in selected_cofee:
        coffe_machine_resources.resources[resource_value] -= selected_cofee[resource_value]
    print(f"Here is your drink: {user_choice}. Have a lovely day (❤´艸｀❤)")

def main():
    user_choice = welcome_screen()
    if user_choice == "off":
        return 0
    elif user_choice == "report":
        get_report()
    if user_choice in CHOICES[2:]:
        buy_a_coffee(user_choice)
    main()

main()