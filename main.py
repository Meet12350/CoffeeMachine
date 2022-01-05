from menu import MENU, resources

money = 0
is_machine_on = True


def is_resource_sufficient(drink):
    for key in drink.keys():
        if resources[key] < drink[key]:
            print(f"Sorry there is not enough {key}.")
            return False
    return True


def process_coins():
    print("Please Insert Coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    total = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickels) + (0.01 * pennies)
    return total


def is_transaction_successful(total, cost):
    if total < cost:
        print("Sorry, that's not enough money. Money Refunded")
        return False
    elif total > cost:
        print(f"Here is ${round(total - cost, 2)} in change.")
        return True
    else:
        return True


def make_coffee(drink, res):
    for key in drink['ingredients'].keys():
        res[key] -= drink['ingredients'][key]
    return True


while is_machine_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == "report":
        print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: {money}")
    elif user_choice == "off":
        is_machine_on = False
    else:
        if is_resource_sufficient(MENU[user_choice]['ingredients']):
            user_money = process_coins()
            if is_transaction_successful(user_money, MENU[user_choice]['cost']):
                money += MENU[user_choice]['cost']
                if make_coffee(MENU[user_choice], resources):
                    print(f"Here's your {user_choice}, enjoy it!")






