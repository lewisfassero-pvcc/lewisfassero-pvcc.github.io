#Name: Lewis Fassero
#Program Purpose: This program finds the cost of movie tickets.
#   Price per ticket: $10.99
#   Price per bucket of popcorn: $8.99
#   Price per drink: $4.99
#   Sales tax rate: 5.3%

import datetime

##### define global variables #####
# define tax rate and prices
SALES_TAX_RATE=0.053
PR_TICKET=10.99
PR_POPCORN=8.99
PR_DRINK=4.99

# define global variables
num_tickets=0
num_popcorn=0
num_drinks=0
tickettotal=0
popcorntotal=0
drinktotal=0
subtotal=0
sales_tax=0
total=0

##### define program functions #####

def main():

    more_tickets=True

    while more_tickets:
        get_user_data()
        perform_calculations()
        display_results()

        askagain=input("\nWould you like to order again (Y or N)?: ")
        if askagain.upper()=="N":
            more_tickets=False
            print("\nThank you for choosing CINEMA HOUSE MOVIES!\n\n\n")

def get_user_data():
    global num_tickets, num_popcorn, num_drinks
    num_tickets=int(input("Welcome to CINEMA HOUSE MOVIES!\n\nHow many movie tickets would you like to purchase?: "))
    num_popcorn=int(input("How many buckets of popcorn would you like?: "))
    num_drinks=int(input("How many drinks?: "))

def perform_calculations():
    global tickettotal, popcorntotal, drinktotal, subtotal, sales_tax, total
    tickettotal=num_tickets*PR_TICKET
    popcorntotal=num_popcorn*PR_POPCORN
    drinktotal=num_drinks*PR_DRINK
    subtotal=tickettotal+popcorntotal+drinktotal
    sales_tax=subtotal*SALES_TAX_RATE
    total=subtotal+sales_tax

def display_results():
    moneyformat='8,.2f'
    qtyformat='2'
    print('-----------------------------')
    print('**** CINEMA HOUSE MOVIES ****')
    print('Your neighborhood movie house')
    print('-----------------------------')
    print(format(num_tickets, qtyformat) + '  Tickets        $ ' + format(tickettotal, moneyformat))
    print(format(num_popcorn, qtyformat) + '  Popcorn        $ ' + format(popcorntotal, moneyformat))
    print(format(num_drinks, qtyformat) + '  Drinks         $ ' + format(drinktotal, moneyformat))
    print('                             ')
    print('    Subtotal:      $ ' + format(subtotal, moneyformat))
    print('    Tax:           $ ' + format(sales_tax, moneyformat))
    print('    Total:         $ ' + format(total, moneyformat))
    print('-----------------------------')
    print('Thank you for your order.\nEnjoy your movie!')
    print(str(datetime.datetime.now()))

##### call on main program to execute #####

main()
