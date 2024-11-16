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
    """Display current resources in the coffee machine."""
    for item in resources:
        print(f"{item.capitalize()}: {resources[item]}")


def resource_check(coffee_type):
    """Check if there are enough resources for the selected coffee type."""
    recipe = MENU[coffee_type]["ingredients"]
    # Check ingredients
    for ingredient in recipe:
        if ingredient != "cost":  # Skip the cost
            if resources[ingredient] < recipe[ingredient]:
                print(f"Sorry, there is not enough {ingredient}.")
                return False
            resources[ingredient] -= recipe[ingredient]
    return True


def money_check(coffee_type):
    """Check if the user has inserted enough money for the selected coffee."""
    cost = MENU[coffee_type]["cost"]
    print(f"Please insert ${cost:.2f}.")
    
    # Input handling for coin values
    try:
        quarters = float(input("How many quarters? :"))
        dimes = float(input("How many dimes? :"))
        nickels = float(input("How many nickels? :"))
        pennies = float(input("How many pennies? :"))
    except ValueError:
        print("Invalid input. Please enter numeric values for coins.")
        return False
    
    total_money = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickels) + (0.01 * pennies)
    
    if total_money >= cost:
        change = total_money - cost
        if change > 0:
            print(f"Here is ${change:.2f} in change.")
        resources["money"] += cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def coffee_machine():
    """Main function to run the coffee machine."""
    while True:
        selected = input("What would you like? (espresso/latte/cappuccino): ").lower()
        
        if selected == "off":
            print("Turning off the coffee machine. Goodbye!")
            break
        elif selected == "report":
            report_resources()
        elif selected in MENU:
            if resource_check(selected):
                if money_check(selected):
                    print(f"Here is your {selected} ☕️. Enjoy!")
        else:
            print("Invalid selection. Please choose a valid coffee or type 'report' to check resources.")

if __name__ == "__main__":
    coffee_machine()
