# Name: Abigail Bang
# Prog purpose: This program finds the personal property tax for vehicles in Charlottesville VA


import datetime

############ define global variables ############
ANNUAL_TAX = .042
QUAL_RELIEF = .33

# define global variables
total = 0
assessed_value = 0
total_owed = 0
relief_amt = 0
relief = 0
annual_amt = 0
tax_total = 0

######### define program functions ###########
def main():
    more = True
    while more:
        get_vehicle_data()
        perform_vehicle_calculations()
        display_vehicle_results()

        askAgain = input("\nWould you like to process another vehicle? (Y/N?: )" )
        if askAgain.upper() == "N":
            more = False
            print('Thank you for completing your personal property taxes.')


def get_vehicle_data():
    global assessed_value, relief_yesno
    assessed_value = int(input("Assessed vehicle value: "))

    print("\nOwned or leased vehicles which are predominately used for non-business purposes & have passenger license plates are elegible for tax relief.")
    relief_yesno = input("Is your vehicle elegible for tax relief(Y or N): ")
   


def perform_vehicle_calculations():
    global annual_amt, tax_total, total_owed, relief_total, assessed_value, relief_amt

    ## find total
    annual_amt = assessed_value * ANNUAL_TAX
    tax_total = annual_amt / 2
    if relief_yesno.upper() == "Y":
        relief_amt = tax_total * QUAL_RELIEF
    else:
        relief_amt = 0
    total_owed =  tax_total - relief_amt
   
        


def display_vehicle_results():
    moneyformat = '10,.2f'
    line = '-------------------------------------------------'
    print(line)
    print('**** Charlottesville Personal Property Taxes ****')
    print(line)
    print('Assessed Vehicle Value   $ ' + format(assessed_value, moneyformat))
    print('Tax Total                $ ' + format(tax_total, moneyformat))
    print('Relief Amount            $ ' + format(relief_amt, moneyformat))
    print(line)
    print('Total                    $ ' + format(total_owed, moneyformat))
    print(line)
    print(str(datetime.datetime.now()))

########### call on main program to execute ##########
main()
