# NAME: Joshua Vernon 
# NAME :Abigail Bang
# Prog purpose: This program finds the cost of pizzas, drinks, and breadsticks
#   Small Pizza: 9.99
#   Medium Pizza: 12.99
#   Large Pizza: 17.99
#   Xlarge Pizza: 21.99
#   Drink: 3.99
#   Breadsticks: 6.99
#   Sales tax rate: 5.5%

import datetime
from re import L, M, S

########## define global variables ##########
# define tax rate and prices
SALES_TAX_RATE = 0.055
SMALL_PIZZA = 9.99
MEDIUM_PIZZA = 12.99
LARGE_PIZZA = 17.99
XLARGE_PIZZA = 21.99
DRINK = 3.99
BREADSTICKS = 6.99

# define global variables
num_pizza = 0
size_pizza = 's'
num_small_pizza = 0
num_medium_pizza = 0
num_large_pizza = 0
num_xlarge_pizza = 0 
num_drink = 0
num_breadsticks = 0
ssubtotal = 0
lsubtotal = 0
msubtotal = 0
xlsubtotal = 0
dsubtotal = 0
bsubtotal = 0
subtotal = 0
sales_tax = 0
total = 0

##### define program functions #####
def main():
    more = True

    while more:
        get_user_data()
        perform_calculations()
        display_results()

        askAgain = input("\nWould you like to order again (Y or N)?: ")
        if askAgain.upper() == "N" or askAgain.upper() == "NO": 
            more = False
            print("Thank you for your order. Enjoy your meal!")

def get_user_data():
    global num_pizza, num_drink, num_breadsticks, size_pizza
    size_pizza = str(input("Size pizza (S $9.99) (M $ 12.99) (L $17.99) (XL $21.99): "))
    num_pizza = int(input("Amount of pizzas: "))
    num_drink = int(input("Number of drinks ($3.99): "))
    num_breadsticks = int(input("Number of breadsticks ($6.99): "))

def perform_calculations():
    global ssubtotal, sales_tax, total, msubtotal, lsubtotal, xlsubtotal, dsubtotal, bsubtotal, subtotal, size_pizza

    if size_pizza.upper() == "S":
        ssubtotal = num_pizza * SMALL_PIZZA

    elif size_pizza.upper() == "M":
        msubtotal = num_pizza * MEDIUM_PIZZA

    elif size_pizza.upper() == "L":
        lsubtotal = num_pizza * LARGE_PIZZA

    elif size_pizza.upper() == "XL":
        xlsubtotal = num_pizza * XLARGE_PIZZA
    
    dsubtotal = num_drink * DRINK
    bsubtotal = num_breadsticks * BREADSTICKS
    subtotal = ssubtotal + msubtotal + lsubtotal + xlsubtotal + dsubtotal + bsubtotal
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax

def display_results():
    line = '--------------------------------'
    moneyf = '8,.2f'
    print(line)
    print('**** Palermo Pizza ****')
    print('Your neighborhood pizza place')
    print(line)
    print('Number of pizzas         : ' + str(num_pizza))
    print('Number of drinks         : ' + str(num_drink))
    print('Number of breadsticks    : ' + str(num_breadsticks))
    print(line)
    print('Pizza total              $ ' + format(ssubtotal + msubtotal + lsubtotal + xlsubtotal,moneyf))
    print('Drink total              $ ' + format(dsubtotal,moneyf))
    print('Breadstick total         $ ' + format(bsubtotal,moneyf))
    print('Subtotal                 $ ' + format(subtotal,moneyf))
    print('Sales Tax                $ ' + format(sales_tax,moneyf))
    print('Total                    $ ' + format(total,moneyf))
    print(str(datetime.datetime.now()))

###### call on main program to execute ########
main()



