# Name: Lewis Fassero
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

numemps = len(emp)

############## new lists for calculated amounts ###############
grosspay=[]
fedtax=[]
statetax=[]
socsec=[]
medicare=[]
retirement=[]
netpay=[]

totalgross=0
totalnet=0

############## tuples of constants ##############
#          C      S      J      M
# indexes  0      1      2      3
PAYRATE=(16.50, 15.75, 15.75, 19.50)

#            fed  state   ss     med    ret
# indexes     0     1      2      3      4
DEDRATE=(0.12, 0.03, 0.062, 0.0145, 0.04)

############## define program functions ###############
def main():
    performcalculations()
    displayresults()

def performcalculations():
    global totalgross, totalnet

    for i in range(numemps):
        if job[i]=='C':
            gross=hours[i]*PAYRATE[0]
        elif job[i]=='S':
            gross=hours[i]*PAYRATE[1]
        elif job[i]=='J':
            gross=hours[i]*PAYRATE[2]
        else:
            gross=hours[i]*PAYRATE[3]

        fed=gross*DEDRATE[0]
        state=gross*DEDRATE[1]
        ss=gross*DEDRATE[2]
        med=gross*DEDRATE[3]
        ret=gross*DEDRATE[4]

        net=gross-fed-state-ss-med-ret
        totalgross+=gross
        totalnet+=net

        grosspay.append(gross)
        fedtax.append(fed)
        statetax.append(state)
        socsec.append(ss)
        medicare.append(med)
        retirement.append(ret)

def displayresults():
    currency='8,.2f'
    currencylg='12,.2f'
    line='------------------------------------------------------------------------------------------------'
    tab='\t'
    print(line)
    print('************************************** FRESH FOODS MARKET **************************************')
    print('------------------------------------- WEEKLY PAYROLL REPORT ------------------------------------')
    print(tab+tab+tab+tab+'   '+str(datetime.datetime.now()))
    print(line)
    print('Employee\tCode\tGross\t\t\t\tWithholdings')
    print('\t\t\t\tFederal\t     State\t Soc Sec\tMedicare\t     Net')
    print(line)
    
    for i in range(numemps):
        data1=emp[i]+'  '+job[i]+' '+format(grosspay[i], currency)+'  '+format(fedtax[i], currency)+'   '+format(statetax[i], currency)
        data2=tab+format(socsec[i], currency)+tab+format(medicare[i], currency)+tab+format(retirement[i], currency)
        print(data1+data2)
        
    print(line)
    print('********************************************************************* TOTAL GROSS: $'+format(totalgross, currencylg))
    print('********************************************************************* TOTAL NET  : $'+format(totalnet, currencylg))
    print(line)
    print()
    
########### Call on main program to execute ##############

main()
