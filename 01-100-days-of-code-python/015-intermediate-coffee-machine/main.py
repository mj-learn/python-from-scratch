from data import MENU, profit, resources


def print_report():
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${profit}")


def check_resources(drink_type):
    """Returns True when order can be made, False if ingredients are insufficient."""
    ingredients = MENU[drink_type]["ingredients"]
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_transaction(price):
    """Return True when the payment is accepted, or False if money is insufficient."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    if total < price:
        print("Sorry that's not enough money. Money refunded.")
        return False
    if total >= price:
        global profit
        profit += price
        change = round(total - price, 2)
        print(f"Here is ${change} in change.")

    return True


def make_coffee(drink_type):
    """Deduct the required ingredients from the resources."""
    ingredients = MENU[drink_type]["ingredients"]
    for res in ingredients:
        resources[res] -= ingredients[res]
    print(f"Here is your {drink_type}. Enjoy!")


def machine_prompt():
    prompt = ""
    while prompt not in ["off", "report", "espresso", "latte", "cappuccino"]:
        prompt = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()

        if prompt == "report":
            prompt = ""
            print_report()

        if prompt in ["espresso", "latte", "cappuccino"]:
            enough_resources = check_resources(prompt)

            if enough_resources:
                transaction_successful = process_transaction(MENU[prompt]["cost"])

                if enough_resources and transaction_successful:
                    make_coffee(prompt)

            prompt = ""


machine_prompt()
