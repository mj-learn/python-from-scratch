from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine


def machine_prompt():
    machine = CoffeeMaker()
    menu = Menu()
    money_machine = MoneyMachine()
    prompt = ""
    while prompt not in ["off", "report", "espresso", "latte", "cappuccino"]:
        prompt = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()

        if prompt == "report":
            machine.report()
            money_machine.report()
            prompt = ""

        if prompt in ["espresso", "latte", "cappuccino"]:
            drink = menu.find_drink(prompt)

            if machine.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                machine.make_coffee(drink)

            prompt = ""


machine_prompt()
