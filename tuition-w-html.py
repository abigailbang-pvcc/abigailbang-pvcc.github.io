# Name: Abigail Bang
# Prog Purpose: This program computes PVCC college tuition & fees based ond number of credits
# PVCC fee rates are from: https://www.pvcc.edu/tuition-and-fees
# Rates are: per credit

import datetime
# dafine tuition and fee rates
RATE_TUITION_IN = 159.61
RATE_TUITION_OUT =  336.21
RATE_CAPITAL_FEE = 23.50
RATE_INSTITUTION_FEE = 1.75
RATE_ACTIVITY_FEE = 2.90

# define global variables
inout = 1 # 1 means in-state, 2 means out-of-state
numcredits = 0
scholarshipamt = 0

tuition_amt = 0
cap_fee_amt = 0
inst_fee_amt = 0
act_fee_amt = 0
total_amt = 0
balance_amt = 0

outfile = 'tuition2.html'
########### define program functions #######
def main():
    open_outfile()
    more = True
    while more:
        get_user_data()
        perform_calculations()
        create_output_file()
       
        yesno = input("\nWould you like to calculate tuition and fees for another student (Y/N) :")
        if yesno == "n" or yesno == "N" :
            more = False
            print('\n** Open this file in a browser window to see your results: ' + outfile)
            f.write('</body></html>')
            f.close()


def open_outfile():
    global f
    f = open(outfile, 'w')
    f.write('<html><head><title>Tuition</title>\n')
    f.write('<style> td{text-align: right} </style> </head>\n')
    f.write('<body style ="background-color: #d5e9e8; background-image: url(sea.png); color: #143d55;">\n')

def get_user_data():
    global inout,numcredits, scholarshipamt
    inout = int(input("Enter a 1 for IN-STATE; enter 2 for OUT-OF-STATE: "))
    numcredits = int(input("Number of credits registered for : "))
    scholarshipamt = float(input("Scholarship amount recived : "))

def perform_calculations():
    global total, balance, in_state, out_state, tuition_amt, inst_fee_amt, cap_fee_amt, act_fee_amt, total_amt, balance_amt
    if inout == 1:
        tuition_amt = numcredits * RATE_TUITION_IN
        cap_fee_amt = 0
    else:
        tuition_amt = numcredits * RATE_TUITION_OUT
        cap_fee_amt = numcredits * RATE_CAPITAL_FEE
   
    inst_fee_amt = numcredits * RATE_INSTITUTION_FEE
    act_fee_amt = numcredits * RATE_INSTITUTION_FEE
    total_amt =  tuition_amt + cap_fee_amt + inst_fee_amt + act_fee_amt
    balance_amt = total_amt - scholarshipamt
   
def create_output_file():
    moneyformat = '8,.2f'
    today = str(datetime.datetime.now())
    day_time = today[0:16]

    tr = '<tr><td>'
    endtd = '</td><td>'
    endtr = '</td></tr>\n'
    colsp = '<tr><td colspan = "3">'
    sp = " "

    #create output file
 
    f.write('\n<table border="3" style ="background-color: #d5e9e8; font-family: arial; margin: auto;">\n')
    f.write(colsp + '\n')
    f.write('<h2>Piedmont Virginia Community College</h2></td></tr>')
    f.write(colsp + '\n')
    f.write(tr + 'Tuition Fee' + endtd + format(tuition_amt, moneyformat) + endtr)
    f.write(tr + 'Capital Fee' + endtd + format(cap_fee_amt, moneyformat) + endtr)
    f.write(tr + 'Institution Fee' + endtd + format(inst_fee_amt, moneyformat) + endtr)
    f.write(tr + 'Activity Fee' + endtd + format(act_fee_amt, moneyformat) + endtr)
    f.write(tr + 'Total' + endtd +   format(total_amt, moneyformat) + endtr)
    f.write(tr + 'Balance' + endtd + format(balance_amt, moneyformat) + endtr)

    f.write(colsp + 'Date/Time: ' + day_time + endtr)
    f.write('</table><br />')

########## call on main program to execute ########
main()
