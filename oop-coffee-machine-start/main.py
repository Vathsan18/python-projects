from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    try:
        choice = input("What do you want? (espresso/latte/cappuccino) ").lower()
        if choice == "off":
            break
        elif choice == "report":
            coffee_machine.report()
            money_machine.report()
        else:
            drink = menu.find_drink(choice)
            if coffee_machine.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)
    except:
        print("Enter a valid choice.")
