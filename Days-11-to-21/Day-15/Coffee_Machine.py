from data import MENU, resources
from random import choice

# coffee machine

water = int(resources["water"])
milk = int(resources["milk"])
coffee = int(resources["coffee"])
cost = float(0)


def coffee_machine(user_input):
    global water, milk, coffee, cost

    def resources_checker():
        empty_items = []
        if water < user_required_water:
            empty_items.append("milk")
        if milk < user_required_milk:
            empty_items.append("water")
        if coffee < user_required_coffee:
            empty_items.append("coffee")
        return empty_items  

    def transaction(quarters, dimes, nickels, pennies):
        quarters *= 25
        dimes *= 10
        nickels *= 5
        pennies *= 1
        total = float((quarters + dimes + nickels + pennies)/100)
        if total < coffee_cost:
            print("Sorry, that's not enough money. Money refunded.")
        elif total > coffee_cost:
            print(f'Here is ${round(total - coffee_cost , 2)} in change')
            print("Here is your latte ☕. Enjoy!")
        else:
            print("Here is your latte ☕. Enjoy!")

    if user_input in MENU:
        user_required_water = MENU[user_input]["ingredients"]["water"]
        user_required_milk = MENU[user_input]["ingredients"]["milk"]
        user_required_coffee = MENU[user_input]["ingredients"]["coffee"]
        coffee_cost = MENU[user_input]["cost"]
        resources_check = resources_checker()
        if len(resources_check) > 0:
            print(f"Sorry there is not enough {choice(resources_check)}.")
        elif not len(resources_check) > 0:
            print("Please insert coins")
            q = int(input("How many quarters?: "))
            d = int(input("How many dimes?: "))
            n = int(input("How many nickles?: "))
            p = int(input("How many pennies?: "))
            x = transaction(q, d, n, p)
            if x  != "Sorry, that's not enough money. Money refunded.":
                milk -= user_required_milk
                coffee -= user_required_coffee
                water -= user_required_water
                cost += coffee_cost

    elif user_input == "report":
        print(f"Water: {water}ml\nMilk: {milk}ml")
        print(f"Coffee: {coffee}g\nMoney: ${cost}")

    elif user_input == "off":
        print("Machine turned off.")
        exit()

    else:
        print("Invalid input!")


while True:
    coffee_machine(input("What would you like? (espresso/latte/cappuccino): "))
