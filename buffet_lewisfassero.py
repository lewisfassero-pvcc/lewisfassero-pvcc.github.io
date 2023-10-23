#Name: Lewis Fassero
#Program Purpose: This program finds the cost of a buffet visit.
#   Price per adult: $19.95
#   Price per child: $11.95
#   Service fee rate: 10%
#   Sales tax rate: 6.2%

import datetime

##### define global variables #####
# define tax rate and prices
SALES_TAX_RATE=0.062
SERVICE_FEE_RATE=0.10
PR_ADULT=19.95
PR_CHILD=11.95
HYPHEN_LINE='------------------------------'

# define global variables
num_adults=0
num_children=0
adulttotal=0
childtotal=0
subtotal=0
service_fee=0
sales_tax=0
total=0

##### define program functions #####

def main():

    more_meals=True

    while more_meals:
        get_user_data()
        perform_calculations()
        display_results()

        askagain=input("\nWould you like to order again (Y or N)?: ")
        if askagain.upper()=="N":
            more_meals=False
            print("\nThank you for choosing BRANCH BARBECUE BUFFET!\n\n\n")

def get_user_data():
    global num_adults, num_children
    num_adults=int(input("Welcome to CINEMA HOUSE MOVIES!\n\nHow many adults are there in your party?: "))
    num_children=int(input("How many children are in your party?: "))

def perform_calculations():
    global adulttotal, childtotal, subtotal, service_fee, sales_tax, total
    adulttotal=num_adults*PR_ADULT
    childtotal=num_children*PR_CHILD
    subtotal=adulttotal+childtotal
    service_fee=subtotal*SERVICE_FEE_RATE
    sales_tax=subtotal*SALES_TAX_RATE
    total=subtotal+service_fee+sales_tax

def display_results():
    moneyformat='8,.2f'
    qtyformat='2'
    print(HYPHEN_LINE)
    print('*** BRANCH BARBECUE BUFFET ***')
    print('  Your neighborhood barbecue  ')
    print(HYPHEN_LINE)
    print(format(num_adults, qtyformat) + '  Adults          $ ' + format(adulttotal, moneyformat))
    print(format(num_children, qtyformat) + '  Children        $ ' + format(childtotal, moneyformat))
    print('\n    Subtotal:       $ ' + format(subtotal, moneyformat))
    print('    Service fee:    $ ' + format(service_fee, moneyformat))
    print('    Tax:            $ ' + format(sales_tax, moneyformat))
    print('    Total:          $ ' + format(total, moneyformat))
    print(HYPHEN_LINE)
    print('Thank you for your order.\nEnjoy your meal!')
    print(str(datetime.datetime.now()))

##### call on main program to execute #####

main()
