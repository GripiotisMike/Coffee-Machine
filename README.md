# Coffee Machine

Overview
This is a simple coffee machine simulation program that allows users to choose between three coffee types: Espresso, Latte, and Cappuccino. The machine checks if there are enough resources (water, milk, and coffee) to make the selected coffee and if the user has inserted enough money. The program also provides the option to generate a report of available resources.

## Features
Choose from three coffee types: Espresso, Latte, or Cappuccino.
Check available resources (water, milk, coffee, and money) with the report command.
Make sure there are sufficient resources (water, milk, coffee) to prepare the coffee.
Insert coins (quarters, dimes, nickels, pennies) to pay for your coffee.
The machine gives change if you overpay and alerts if there is insufficient money.
The machine keeps track of money earned from selling coffee.

## Coffee Types & Prices
Espresso:
Ingredients: 50 ml of water, 18g of coffee

Price: $1.50
Latte:
Ingredients: 200 ml of water, 150 ml of milk, 24g of coffee
Price: $2.50

Cappuccino:
Ingredients: 250 ml of water, 100 ml of milk, 24g of coffee
Price: $3.00

## How It Works
When you run the program, you will be asked to select a coffee type. The options are:

-espresso
-latte
-cappuccino
The machine will check if there are enough resources (water, milk, and coffee) to prepare the coffee. If any ingredient is missing, you will be informed.

The program will then ask you to insert coins:

-Quarters
-Dimes
-Nickels
-Pennies
The machine will check if the money inserted is sufficient to cover the cost of the selected coffee. If the amount is enough, it will deduct the ingredients, give you your coffee, and provide any change if necessary. If the amount is insufficient, the money will be refunded.

You can check available resources at any time by typing report. The machine will display the current amounts of water, milk, coffee, and the money collected.

To turn off the machine, type off.
