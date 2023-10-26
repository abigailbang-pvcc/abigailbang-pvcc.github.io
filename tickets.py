# Name: Abigail Bang
# Prog Purpose: This program finds the cost of movie tickets.
#   Price per ticket: $10.99
#   Sales tax rate: 5.5%

import datetime
 
############ define global variables ############
# define tax rate and prices
SALES_TAX_RATE = .055
PR_TICKET = 10.99

# define global variables
num_tickets = 0
ticket_cost = 0
subtotal = 0
sales_tax = 0
total = 0
############ define program functions #########
def main():
    more_tickets = True

    while more_tickets:
        get_user_data()
        perform_calculations()
        display_results()

        yesno = input ("\nWould you like to order again (Y or N)?")
        if yesno == "N" or yesno == "n":
            more_orders = False
            print ("Thank you for your order. Enjoy your movie!")

def get_user_data():
    global num_tickets
    num_tickets = int(input("Number of movie tickets: "))

def perform_calculations():
    global subtotal, sales_tax, total, ticket_cost
    ticket_cost = num_tickets * PR_TICKET
    subtotal = ticket_cost
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax

def display_results():
    print('---------------------------------')
    print('****CINEMA HOUSE MOVIES****')
    print('Your neighborhood movie house')
    print('---------------------------------')
    print('Tickets     $ ' + str(subtotal))
    print('---------------------------------')
    print('Sales Tax   $ ' + str(sales_tax))
    print('Total       $ ' + str(total))
    print('---------------------------------')
    print(str(datetime.datetime.now()))

######### call on main program to execute #####
main()
