# Name: Abigail Bang
# Prog Purpose: This program creates a payroll report

import datetime

############## LISTS of data ############
emp = [
    "Smith, James     ",
    "Johnson, Patricia",
    "Williams, John   ",
    "Brown, Michael   ",
    "Jones, Elizabeth ",
    "Garcia, Brian    ",
    "Miller, Deborah  ",
    "Davis, Timothy   ",
    "Rodriguez, Ronald",
    "Martinez, Karen  ",
    "Hernandez, Lisa  ",
    "Lopez, Nancy     ",
    "Gonzales, Betty  ",
    "Wilson, Sandra   ",
    "Anderson, Margie ",
    "Thomas, Daniel   ",
    "Taylor, Steven   ",
    "Moore, Andrew    ",
    "Jackson, Donna   ",
    "Martin, Yolanda  ",
    "Lee, Carolina    ",
    "Perez, Kevin     ",
    "Thompson, Brian  ",
    "White, Deborah   ",]

job = ["C", "S", "J", "M", "C", "C", "C", "C", "S", "M", "C", "S",
     "C", "C", "S", "C", "C", "M", "J", "S", "S", "C", "S", "M",]

hours = [37, 29, 32, 20, 24, 34, 28, 23, 35, 39, 36, 29, 26, 38,
         28, 31, 37, 32, 36, 22, 28, 29, 21, 31]

num_emps = len(emp)

####### NEW LISTS for calculated amounts ############
Lgross_pay = []
Lfed_tax = []
Lstate_tax = []
Lsoc_sec = []
Lmedicare = []
Lret = []
Lnet_pay = []

total_gross = 0
total_net = 0

################## TUPLES of constants ###########################
#              C       S       J       M
# indexes      0       1       2       3
PAY_RATE = (16.50, 15.75, 15.75, 19.50)

#           fed state ss med ret
#indexes    0    1     2   3    4
DED_RATE = (.12, .03, .062, .0145, .04)


################## define program functions ######################
def main():
    perform_calculations()
    display_results()

   
def perform_calculations():
    global total_gross, total_net, state_tax, fed_tax, soc_sec

    for i in range(num_emps):

    #calculate gross pay
        if job[i] == "C":
            pay = hours[i] * PAY_RATE[0]

        elif job[i] == "S":
            pay = hours[i] * PAY_RATE[1]

        elif job[i] == "J":
            pay = hours[i] * PAY_RATE[2]

        else:
            pay = hours[i] * PAY_RATE[3]

    #calculate deductions
        fed = pay * DED_RATE[0]
        state = pay * DED_RATE[1]
        medicare = pay * DED_RATE[2]
        soc_sec = pay * DED_RATE[3]
        ret = pay * DED_RATE[4]

        net = pay - fed - state - medicare - soc_sec - ret

    #add to totals
        total_gross += pay
        total_net += net

    #append amounts to lists
        Lgross_pay.append(pay)
        Lfed_tax.append(fed)
        Lstate_tax.append(state)
        Lsoc_sec.append(soc_sec)
        Lmedicare.append(medicare)
        Lret.append(ret)
        Lnet_pay.append(net)

def display_results():
    currency = '8,.2f'
    currency2 = '12,.2f'
    line = '------------------------------------------------------'
    tab = "\t"

    print(line)
    print('******************** FRESH FOODS MARKET *********************')
    print('WEEKLY PAYROLL REPORT ')
    print(tab + str(datetime.datetime.now()))
    print(line)
    titles1 = "Emp Name" + tab + "Code" + tab + "Gross" + tab
    titles2 = "Fed Inc Tax" + tab + "State Inc Tax" + tab + "Soc Sec" + tab + "Medicare" + tab + "Net"
    print(titles1 + titles2)

    for i in range(num_emps):
        datal = emp[i] + "  " + job[i]+ format(Lgross_pay[i], currency) + format(Lfed_tax[i], currency) + format(Lstate_tax[i], currency)
        data2 = format(Lsoc_sec[i], currency) + format(Lmedicare[i], currency) + format(Lret[i], currency)
        print(datal + data2)
    print(line)
    print("********************** TOTAL GROSS: $" + format(total_gross, currency2))
    print("********************** TOTAL NET:   $" + format(total_net, currency2))
    print(line)

#########call on main program to execute
main()
