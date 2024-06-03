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
    "money": 0
}


def report_resources():
    for i in resources:
        print(f"{i} : {resources[i]}")


def resource_check(coffe_type):
    a = True
    recipie = MENU[coffe_type]["ingredients"]
    cof_need = recipie["coffee"]
    wat_need = recipie["water"]
    if coffe_type != "espresso":
        milk_need = recipie["milk"]
        if milk_need > resources["milk"]:
            print("Sorry, there is not enough milk.")
            a = False
        else:
            resources["milk"] = resources["milk"] - milk_need
    if cof_need > resources["coffee"]:
        print("Sorry, there is not enough coffee.")
        a = False
    else:
        resources["coffee"] = resources["coffee"] - cof_need
    if wat_need > resources["water"]:
        print("Sorry, there is not enough water.")
        a = False
    else:
        resources["water"] = resources["water"] - wat_need
    return a


def money_check(coffe_type):
    a = True
    print("Please insert coin.")
    mon_need = MENU[coffe_type]["cost"]
    q = float(input("How many quarters? :"))
    d = float(input("How many dimes? :"))
    n = float(input("How many nickels? :"))
    p = float(input("How many pennies? :"))
    dora = (0.25 * q) + (0.1 * d) + (0.5 * n) + (0.01 * p)
    if dora >= mon_need:
        print(f"Here is ${dora-mon_need} in change.")
        resources["money"] += mon_need
    else:
        print("Sorry, that's not enough money. Money refunded.")
        a = False
    return a


while True:
    selected = input("What would you like? (espresso/latte/cappuccino):")
    if selected in MENU:
        if resource_check(selected):
            if money_check(selected):
                print(f"Here is your {selected} ☕️. Enjoy!")
    elif selected == "report":
        report_resources()
    elif selected == "off":
        break
    else:
        print("Invalid coffee/command.Please read the menu!")
        continue
