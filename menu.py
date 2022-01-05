MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# if resources['water'] >= drink['water']:
#     if resources['milk'] >= drink['milk']:
#         if resources['coffee'] >= drink['coffee']:
#             return True
#         else:
#             print("Sorry there is not enough coffee.")
#             return False
#     else:
#         print("Sorry there is not enough milk.")
#         return False
# else:
#     print("Sorry there is not enough water.")
#     return False