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
infile = 'emerald.csv'
outfile = "emerald-web-page.html"

guest = []
lname = []
fname = []
nights = []
subtotal = []
Lsales_tax = []
Loccupancy = []
Ltotal = []



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
            guest[i].append(salestax)
            guest[i].append(occupancy)
            guest[i].append(total)
        


def open_out_file():
    global f
    f = open(outfile, 'w')
    f.write('<html> <head> <title> Emerald Beach Hotel & Resort </title>\n')
    f.write('<style> td{text-align: right} </style> </head>\n')
    f.write('<body style ="background-color: #5f8785; background-image: url(capecod.jpg);  padding-top:5%; padding-bottom:5%;color: #00555b;">\n')


def create_output_html():
    global f

    moneyformat ="8,.2f"
    currency2 ="12,.2f"
    today = str(datetime.datetime.now())
    day_time = today[0:16]

    sttr = '<tr><td>'
    td = '</td><td>'
    endtr = '</td></tr>\n'
    endtd = '</td><td>'
    sp = " "
    csttr = '<tr><td style="text-align:center";>'
    ctd = '</td><td style="text-align:center"; >'
    cendtd = '</td><td style="text-align:center"; >'


    f.write('\n<table border="3" style ="background-color: #BCE161; border-color:#00555b; font-family: helvitica; font-size: 22px;margin: auto; width: 70%;">\n')
    f.write('<tr><td colspan = "8" style="text-align:center";>')
    f.write('<h1 style="padding-top: 1%;">Emerald Beach Hotel & Resort</h1></td></tr>')
    f.write('<tr><td colspan = "8" style="text-align:center";>')
    f.write('<h2 style="padding-top: 1%;" >Time Date/Time: ' + day_time + '</h2></td></tr>' + endtr)
    f.write('<tr><td style="text-align:center";>' + 'Last' + cendtd + 'First' + cendtd + 'Room' + cendtd + 'Num Nights' + cendtd + 'Subtotal' + cendtd + 'Sales Tax' + cendtd + 'Occ Tax' + cendtd + 'Total' + endtr)
    for i in range(len(guest)):
        line1 = '<tr><td style="text-align:center";>' + guest[i][0] + cendtd + guest[i][1] + cendtd + guest[i][2] + cendtd + guest[i][3] + endtd
        line2 = str(format(guest[i][4], moneyformat)) + endtd
        line3 = str(format(guest[i][5], moneyformat)) + endtd 
        line4 = str(format(guest[i][6], moneyformat)) + endtd 
        line5 = str(format(guest[i][7], moneyformat)) + endtr
        f.write(line1 + line2 + line3 + line4 + line5)
    
    line6 = '<tr><td colspan="7" style="text-align: right; padding-right: 1%;"> Grand Total: </td><td>' 
    line7 = str(format(grandtotal,moneyformat)) + endtr
    f.write(line6 + line7)
    f.write('</table><br />')
    f.write('</body></html>')
    f.close()
    print('Open ' + outfile + ' to view data.')


main()
