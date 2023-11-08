#Name: Lewis Fassero
#Program Purpose: This program calculates semi-annual personal property tax owed for a vehicle.

import datetime

##### define global variables #####
TAXRATE=0.042
RELIEFRATE=0.33
DUEDATE='Dec. 05, 2023'

# define global variables
reliefeligible=0
assessment=0
taxamt=0
reliefamt=0
amtdue=0

##### define program functions #####

def main():

    more=True

    while more:
        get_user_data()
        perform_calculations()
        display_results()

        yesno=input("\nWould you like to calculate personal property tax for another vehicle? (Y or N): ")
        if yesno.upper()=="N":
            more=False
            print('Please be sure to pay in full by '+DUEDATE+'.')

def get_user_data():
    global reliefeligible, assessment
    reliefeligible=input("Some vehicles are eligible for tax relief. Eligible\nvehicles must be owned or leased and predominantly\nused for non-business purposes and have passenger\nlicense plates.\nIs your vehicle eligible for tax relief? (Y or N): ")
    assessment=int(input("What is the assessed value of your vehicle?: "))

def perform_calculations():
    global taxamt, reliefamt, amtdue
    if reliefeligible.upper()=='Y' or reliefeligible.upper()=='YES':
        reliefamt=assessment*TAXRATE*RELIEFRATE/2
    else: reliefamt=0
    taxamt=assessment*TAXRATE/2
    amtdue=taxamt-reliefamt
    
def display_results():
    moneyformat='12,.2f'
    qtyformat='2'
    print('-----------------------------------------')
    print('*** City of Charlottesville, Virginia ***')
    print('***** Jason A. Vandever, Treasurer ******')
    print('************** PO Box 2854 **************')
    print('***** Charlottesville, VA 22902-2854 ****')
    print('-----------------------------------------')
    print('Months taxed: 6')
    print('Due date: '+DUEDATE)
    print('-----------------------------------------')
    print('Assessed value             $ ' + format(assessment, moneyformat))
    print('Full tax amount            $ ' + format(taxamt, moneyformat))
    print('Relief                     $ ' + format(reliefamt, moneyformat))
    print('\nTotal amount due           $ ' + format(amtdue, moneyformat))
    print('-----------------------------------------')
    print('Total due '+DUEDATE+': $'+format(amtdue, moneyformat))
    print(str(datetime.datetime.now()))

##### call on main program to execute #####

main()
