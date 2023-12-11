#Name: Abigail Bang
#Prog purpose: This program reads in a hotel data file, performs calculations, and creates an HTML file for the results

import datetime

####### Define rate tuples #######

#             SR  DR  SU
#             0    1   2
ROOM_RATES = (195,250,350)

#           s-tax  occ-tax
#              0     1
TAX_RATES = (0.065,0.1125)

############define files and list #########
infile = "emerald.csv"
outfile = "emerald-web-page.html"

guest = []
Lsales_tax = []
Loccupancy = []
Ltotal = []



total = 0
grandtotal = 0
#############define program functions ############
def main():
    read_in_guest_file()
    perform_calculations()
    open_out_file()
    create_output_html()

def read_in_guest_file():
    global infile
    guest_data = open(infile, "r")
    guest_in = guest_data.readlines()
    guest_data.close()

    ## split the data and insert in the list called: guest
    for i in guest_in:
        guest.append(i.split(","))
room = ["SR","SR","DR","SU","DR","SR","SU","DR","SU","DR","DR","SU","SR","DR","DR","SR","SR","SR","SU","DR","SU","DR","DR","SU","SU","DR","SR","SR","SR","SR",]   
stay = ["2", "1", "1", "6", "7", "8", "3", "4", "4", "5", "1", "3", "4", "5", "1", "1", "5", "2", "7", "5", "7", "1", "1", "1", "8", "5", "2", "4", "1", "1",] 
def perform_calculations():
    global grandtotal
    grandtotal = 0

    for i in range(len(guest)):
            room_type = str(guest[i][2])
            num_nights = int(guest[i][3])

            if room_type =="SR":
                subtotal = ROOM_RATES[0] * num_nights

            elif room_type =="DR":
                subtotal = ROOM_RATES[1] * num_nights

            else:
                subtotal = ROOM_RATES[2] * num_nights


            salestax = subtotal * TAX_RATES[0]
            occupancy = subtotal * TAX_RATES[1]
            total = subtotal + salestax + occupancy

            grandtotal += total

            guest[i].append(subtotal)
            Lsales_tax.append(salestax)
            Loccupancy.append(occupancy)
            Ltotal.append(total)
            

def open_out_file():
    global f
    f = open(outfile, 'w')
    f.write('<html> <head> <title> Emerald Beach Hotel & Resort </title>\n')
    f.write('<style> td{text-align: right} </style> </head>\n')
    f.write('<body style =''>\n')

def create_output_html():
    global f

    currency="8,.f"
    currency2="12,.f"
    today = str(datetime.datetime.now())
    day_time = today[0:16]

    tr = '<tr><td>'
    td = '</td><td>'
    endtr = '</td></tr>\n'
    colsp = '<tr><td colspan = "3">'
    sp = " "


    f.write('\n<table border="3" style ="background-color: #d5e9e8; font-family: arial; margin: auto;">\n')
    f.write(colsp + '\n')
    f.write('<h2>Emerald Beach Hotel & Resort</h2></td></tr>')
    f.write(colsp + '\n')
    f.write(tr + 'Subtotal' + endtd + format(subtotal, moneyformat) + endtr)
    f.write(tr + 'Sales Tax' + endtd + format(salestax, moneyformat) + endtr)
    f.write(tr + 'Occupancy' + endtd + format(occupancy, moneyformat) + endtr)
    f.write(tr + 'Total' + endtd + format(total, moneyformat) + endtr)
    f.write(colsp + 'Date/Time: ' + day_time + endtr)
    f.write('</table><br />')
    f.write('</body></html>')
    f.close()
    print('Open ' + outfile + ' to view data.')

main()
