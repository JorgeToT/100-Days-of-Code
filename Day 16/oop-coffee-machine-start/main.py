from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo


def main():
    print(logo)
    isOn = True
    moneyMachine = MoneyMachine()
    menu = Menu()
    coffeeMaker = CoffeeMaker()
    while isOn == True:
        answer = input(f"\nWhat would you like? {menu.get_items()} ").lower()
        if answer == "off":
            isOn = False
            print("Shutting down...")
        elif answer == "report":
            coffeeMaker.report()
            moneyMachine.report()
        elif menu.find_drink(answer) != None:
            drink = menu.find_drink(answer)
            if coffeeMaker.is_resource_sufficient(drink):
                if moneyMachine.make_payment(drink.cost):
                    coffeeMaker.make_coffee(drink)
                else:
                    print("Not enough money")
            else:
                print("Not enough resources")


main()
