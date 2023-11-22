#Name: Lewis Fassero
#Program Purpose: This program uses lists to calculate the semi-annual personal property tax owed for vehicles in Charlottesville
#   and produces a report which displays all data and the total tax due.

import datetime

##### define global variables #####
TAXRATE=0.042
RELIEFRATE=0.33
DUEDATE='Dec. 05, 2023'

########### create list data ############
vehicle=['2019 Volvo ',
         '2018 Toyota',
         '2022 Kia   ',
         '2020 Ford  ',
         '2023 Honda ',
         '2019 Lexus ']
assessedvalue=[13000,10200,17000,21000,28000,16700]
reliefeligible=['Y','Y','N','Y','N','Y',]
ownername=['Washington, George',
           'Adams, John       ',
           'Jefferson, Thomas ',
           'Madison, James    ',
           'Monroe, James     ',
           'Adams, John Quincy']
taxesdue=[]
numvehicles=len(vehicle)
taxamt=0
taxdue=0
total=0
         
##### define program functions #####

def main():
    perform_calculations()
    display_results()

def perform_calculations():
    global total
    for i in range(numvehicles):
        taxamt=assessedvalue[i]*TAXRATE/2
        if reliefeligible[i].upper()=='Y':
            taxdue=taxamt*(1-RELIEFRATE)
        else:
            taxdue=taxamt
        taxesdue.append(taxdue)
        total=total+taxdue


def display_results():
    moneyformat='8,.2f'
    largemoneyformat='16,.2f'
    line=('------------------------------------------------------------------------')
    tab=('\t')
    qtyformat='2'
    print(line)
    print('********************* PERSONAL PROPERTY TAX REPORT *********************')
    print('******************** Charlottesville, VA 22902-2854 ********************')
    print('\nRun date/time: '+str(datetime.datetime.now()))
    print('\nName'+tab+tab+tab+'Vehicle'+tab+tab+'Value'+tab+tab+'Relief'+tab+'Tax due')
    print(line)
    for i in range(numvehicles):
         dataline1=ownername[i]+tab+vehicle[i]+tab+format(assessedvalue[i], moneyformat)+tab
         dataline2=reliefeligible[i]+tab+format(taxesdue[i], moneyformat)
         print(dataline1+dataline2)
    print(line)
    print('************************************** Total tax due: '+tab+format(total, largemoneyformat))

##### call on main program to execute #####

main()
