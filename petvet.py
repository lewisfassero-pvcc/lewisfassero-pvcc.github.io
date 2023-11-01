#Name: Lewis Fassero
#Program Purpose: This program finds the cost of a vet visit.

#Note: Pet medications prescribed by licensed veterinarians are not subject to sales tax in Virginia.

# Canine vaccines
#   Bordatella: $30.00
#   DAPP: $35.00
#   Influenza: $48.00
#   Leptospirosis: $21.00
#   Lyme disease: $41.00
#   Rabies: $25.00
#   Full vaccine package (includes all vaccines): 15% discount
# Canine heartworm preventative chews (price per chew; one chew per month)
#   Small dogs, up to 25 lb.: $9.99
#   Medium-sized dogs, 26-50 lb.: $11.99
#   Large dogs, 51-100 lb.: $13.99

# Feline vaccines
#   Feline Leukemia: $35.00
#   Feline Viral Rhinotracheitis: $30.00
#   Rabies (one year): $25.00
#   Full vaccine package (includes all vaccines): 10% discount
# Feline heartworm preventative chews (price per chew; one chew per month)
#   (one size): $8.00

import datetime

#################### define global variables #####################
# define tax rate and prices
PRBORD=30.00
PRDAPP=35.00
PRINFL=48.00
PRLEPT=21.00
PRLYME=41.00
PRRABI=25.00

DISCRATE=0.15

PRCHEWSM=9.99
PRCHEWMD=11.99
PRCHEWLG=13.99

PRLEUK=35.00
PRVIRA=30.00
PRFRABI=25.00

FDISCRATE=0.10

PRFCHEW=8.00

HYPHEN_LINE='------------------------------'

# define global variables
numchews=0

vaxamt=0
chewamt=0
discamt=0
total=0

################ define program functions ##################

def main():

    more=True

    while more:
        get_user_data()
        if pettype.upper()=="D" or pettype.upper()=="DOG":
            get_dog_data()
            perform_dog_calculations()
            display_results()
        elif pettype.upper()=="C" or pettype.upper()=="CAT":
            get_cat_data()
            perform_cat_calculations()
            display_results()
        else:
            print('We apologize, but we are unable to provide care for pets other than dogs and\ncats at this time. We recommend that you take '+petname.upper()+' to a provider who accepts\nyour pet type.')

        askagain=input("\nWould you like to process another pet (Y or N)?: ")
        if askagain.upper()=="N":
            more=False
            print("\nThank you for trusting PET CARE MEDS with your pet vaccines and medications.\n\n\n")

def get_user_data():
    global petname, pettype, petweight
    petname=input("Welcome to PET CARE MEDS.\n\nWhat is your pet's name?: ")
    pettype=input("Is "+petname.upper()+" a dog (D) or a cat (C)?: ")
    petweight=int(input("How much does "+petname.upper()+" weigh (in pounds)?: "))

################# dog functions ####################

def get_dog_data():
    global petvax, numchews, petvaxinitial

    dogvm1="\nWhich, if any, of the following dog vaccines would you like for "+petname.upper()+"?\n\t1. Bordatella\n\t2. DAPP\n\t3. Influenza\n\t4. Leptospirosis\n\t5. Lyme disease"
    dogvm2="\n\t6. Rabies\n\t7. Full Vaccine Package\n\t8. NONE"
    dogvaxmenu=dogvm1+dogvm2
    petvaxinitial=int(input(dogvaxmenu+"\n** Enter the vaccine number: "))
    
    if petvaxinitial==1:
        initialselection="BORDATELLA VACCINE"
    elif petvaxinitial==2:
        initialselection="DAPP VACCINE"
    elif petvaxinitial==3:
        initialselection="INFLUENZA VACCINE"
    elif petvaxinitial==4:
        initialselection="LEPTOSPIROSIS VACCINE"
    elif petvaxinitial==5:
        initialselection="LYME DISEASE VACCINE"
    elif petvaxinitial==6:
        initialselection="RABIES VACCINE"
    elif petvaxinitial==7:
        initialselection="FULL VACCINE PACKAGE"
    else:
        initialselection="NONE"
    
    petvaxconfirmation=input("You selected "+initialselection+". Is this correct (Y/N)? ")
    if petvaxconfirmation.upper()=="Y" or petvaxconfirmation.upper()=="YES":
        petvax=petvaxinitial
    else:
        petvax=int(input(dogvaxmenu+"\n** Enter the vaccine number for the vaccine you would like to select: "))

    print("\nMonthly heartworm prevention medication is recommended for all dogs.")
    heartyesno=input("Would you like to purchase monthly heartworm medication for "+petname.upper()+" (Y/N)? ")
    if heartyesno.upper()=="Y" or heartyesno.upper()=="YES":
        numchews=int(input("How many heartworm chews would you like to purchase? "))

def perform_dog_calculations():
    global vaxamt, chewamt, total

    ##### find vax amt #####
    if petvax==1:
        vaxamt=PRBORD
    elif petvax==2:
        vaxamt=PRDAPP
    elif petvax==3:
        vaxamt=PRINFL
    elif petvax==4:
        vaxamt=PRLEPT
    elif petvax==5:
        vaxamt=PRLYME
    elif petvax==6:
        vaxamt=PRRABI
    elif petvax==7:
        vaxamt=(PRBORD+PRDAPP+PRINFL+PRLEPT+PRLYME+PRRABI)*(1-DISCRATE)
    else:
        vaxamt=0

    ##### find chews amt #####
    if petweight<=25:
        chewamt=PRCHEWSM*numchews
    elif petweight<=50:
        chewamt=PRCHEWMD*numchews
    else:
        chewamt=PRCHEWLG*numchews

    #### find total #####
    total=vaxamt+chewamt

################# cat functions ####################

def get_cat_data():
    global petvax, numchews, petvaxinitial

    catvm1="\nWhich, if any, of the following cat vaccines would you like for "+petname.upper()+"?\n\t1. Feline Leukemia\n\t2. Feline Viral Rhinotracheitis\n\t3. Rabies (one year)"
    catvm2="\n\t4. Full Vaccine Package\n\t5. NONE"
    catvaxmenu=catvm1+catvm2
    petvaxinitial=int(input(catvaxmenu+"\n** Enter the vaccine number: "))
    
    if petvaxinitial==1:
        initialselection="FELINE LEUKEMIA VACCINE"
    elif petvaxinitial==2:
        initialselection="FELINE VIRAL RHINOTRACHEITIS VACCINE"
    elif petvaxinitial==3:
        initialselection="RABIES VACCINE (ONE YEAR)"
    elif petvaxinitial==4:
        initialselection="FULL VACCINE PACKAGE"
    else:
        initialselection="NONE"
    
    petvaxconfirmation=input("You selected "+initialselection+". Is this correct (Y/N)? ")
    if petvaxconfirmation.upper()=="Y" or petvaxconfirmation.upper()=="YES":
        petvax=petvaxinitial
    else:
        petvax=int(input(catvaxmenu+"\n** Enter the vaccine number for the vaccine you would like to select: "))

    print("\nMonthly heartworm prevention medication is recommended for all cats.")
    heartyesno=input("Would you like to purchase monthly heartworm medication for "+petname.upper()+" (Y/N)? ")
    if heartyesno.upper()=="Y" or heartyesno.upper()=="YES":
        numchews=int(input("How many heartworm chews would you like to purchase? "))

def perform_cat_calculations():
    global vaxamt, chewamt, total

    ##### find vax amt #####
    if petvax==1:
        vaxamt=PRLEUK
    elif petvax==2:
        vaxamt=PRVIRA
    elif petvax==3:
        vaxamt=PRFRABI
    elif petvax==4:
        vaxamt=(PRLEUK+PRVIRA+PRFRABI)*(1-FDISCRATE)
    else:
        vaxamt=0

    ##### find chews amt #####
    chewamt=PRFCHEW*numchews
    
    #### find total #####
    total=vaxamt+chewamt

########## display results ##########

def display_results():
    moneyformat='8,.2f'
    qtyformat='2'
    print(HYPHEN_LINE)
    print('******* PET CARE MEDS ********')
    print('        Vets who Care         ')
    print(HYPHEN_LINE)
    print('    Vax #'+str(petvax)+'          $ ' + format(vaxamt, moneyformat))
    print(format(numchews, qtyformat) + '  Chews           $ ' + format(chewamt, moneyformat))
    print('    Total:          $ ' + format(total, moneyformat))
    print(HYPHEN_LINE)
    print("Thank you for trusting\nPET CARE MEDS with "+petname.upper()+"'s\nhealthcare!")
    print(str(datetime.datetime.now()))

##### call on main program to execute #####

main()
