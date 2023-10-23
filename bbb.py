# Name: Abigail Bang
# Name: Afsana Nawrozi
# Name: Amir Salamatolla
# Prog Purpose: This program finds the cost of barbecue.
#   Price per adult: $19.95
#   Price per child: $11.95
#   Sales tax rate: 6.2%
#   Service fee rate: 10%

import datetime
 
############ define global variables ############
# define tax rate and prices
SALES_TAX_RATE = .062
SERVICE_FEE_RATE = .10
PR_ADULT = 19.95
PR_CHILDREN = 11.95

num_adults = 0
num_children = 0
adult_cost = 0
child_cost = 0
subtotal = 0
sales_tax = 0
service_fee = 0
total = 0

############ define program functions #########

def main():
    more_orders = True

    while more_orders:
        get_user_data()
        perform_calculations()
        display_results()

        yesno = input ("\nWould you like to order again (Y or N)?")
        if yesno == "N" or yesno == "n":
            more_orders = False
            print ("Thank you for your order. Enjoy your meal!")
        


    

def get_user_data():
    global num_adults
    global num_children
    num_adults = int(input("Number of Adults: "))
    num_children = int(input("Number of Children: "))

def perform_calculations():
    global subtotal, sales_tax, total, adult_cost, child_cost, service_fee
    adult_cost = num_adults * PR_ADULT
    child_cost = num_children * PR_CHILDREN
    subtotal = adult_cost + child_cost
    sales_tax = subtotal * SALES_TAX_RATE
    service_fee = subtotal * SERVICE_FEE_RATE
    total = subtotal + sales_tax + service_fee

def display_results():
    moneyformat = '8,.2f'
    line = '---------------------------------'
    print(line)
    print('****Branch Barbecue Buffet****')
    print('Your neighborhood barbecue buffet')
    print(line)
    print('Adults        $ ' + format(adult_cost, moneyformat))
    print('Children      $ ' + format(child_cost, moneyformat))
    print(line)
    print('Subtotal      $ ' + format(subtotal, moneyformat))
    print('Sales Tax     $ ' + format(sales_tax, moneyformat ))
    print('Service Fee   $ ' + format(service_fee, moneyformat))
    print('Total         $ ' + format(total, moneyformat))
    print(line)
    print(str(datetime.datetime.now()))
######### call on main program to execute ########
main ()

######### call on main program to execute #####
main()
