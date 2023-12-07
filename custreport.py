# Name: Lewis Fassero
# Prog Purpose: Read in a list of customers and display a report that will
#   increase the amount they owe by 10%

cust=[]

def main():
    readincustfile()
    displaycustlist()

def readincustfile():
    custdata=open('customer_data_file.csv', 'r')
    custin=custdata.readlines()
    custdata.close

    for i in custin:
        cust.append(i.split(','))

def displaycustlist():
    total=0
    fcurrency='8,.2f'
    line='--------------------------------'

    print(line)
    print('***** CUSTOMER SALES REPORT ****\n')
    for i in range(len(cust)):
        amtowed=float(cust[i][2])*1.10 #Increase amount by 10%.
        total+=amtowed
        print(cust[i][1]+'      \t'+cust[i][0]+'\t'+format(amtowed,fcurrency))

    print(line)
    print('**** TOTAL AMOUNT:     $'+format(total,fcurrency))

main()
