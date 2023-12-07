#Name: Lewis Fassero
#Program Purpose: This program finds the balance of tuition and fees owed by a student and creates an HTML page to display the results.

import datetime

##### define global variables #####
# define tax rate and prices
RATETUITIONIN=159.61
RATETUITIONOUT=336.21
RATECAPITALFEE=23.50
RATEINSTITUTIONFEE=1.75
RATEACTIVITYFEE=2.90

# define global variables
inout=1 #1 means in state, 2 means out of state
num_credits=0
scholarshipamt=0
tuitiontotal=0
capitaltotal=0
institutiontotal=0
activitytotal=0
subtotal=0
total=0


# create output file
outfile = 'tuition-webpage.html'

##### define program functions #####

def main():

    open_outfile()
    more=True

    while more:
        get_user_data()
        perform_calculations()
        create_output_file()

        yesno=input("\nWould you like to calculate tuition and fees for another student? (Y or N): ")
        if yesno.upper()=="N":
            more=False
            print("\n** From your device's file explorer, open the file titled "+'"'+outfile+'" in a\nbrowser window to see your results.')
            f.write('</body></html>')
            f.close()

def open_outfile():
    global f
    f = open(outfile, 'w')
    f.write('<html> <head> <title> Piedmont Virginia Community College </title>\n')
    f.write('<style> td{text-align: right} </style> </head>\n')
    f.write('<body style ="background-color: #28b0b0; background-image: url(wp-tuition.jpg); color: #004b4d;">\n')
    
def get_user_data():
    global inout, num_credits, scholarshipamt
    inout=int(input("Enter a 1 for IN-STATE or a 2 for OUT-OF-STATE: "))
    num_credits=int(input("How many credits did you register for?: "))
    scholarshipamt=float(input("Scholarship amount received: "))

def perform_calculations():
    global tuitiontotal, capitaltotal, institutiontotal, activitytotal, subtotal, total
    if inout==1:
        tuitiontotal=num_credits*RATETUITIONIN
    else: tuitiontotal=num_credits*RATETUITIONOUT
    
    if inout==1:
        capitaltotal=0
    else: capitaltotal=num_credits*RATECAPITALFEE

    institutiontotal=num_credits*RATEINSTITUTIONFEE
    activitytotal=num_credits*RATEACTIVITYFEE
    subtotal=tuitiontotal+capitaltotal+institutiontotal+activitytotal
    total=subtotal-scholarshipamt

def create_output_file():
    currency='8,.2f'
    today = str(datetime.datetime.now())
    day_time = today[0:19]

    tr = '<tr><td>'
    endtd = '</td><td>'
    endtr = '</td></tr>\n'
    colsp = '<tr><td colspan= "3">'
    sp = " "

    f.write('\n<table border="3"   style ="background-color: #8cffff;  font-family: arial; margin: auto;">\n')            
    f.write(colsp + '\n')
    f.write('<h2>Piedmont Virginia Community College</h2></td></tr>')
    f.write(colsp + '\n')
    f.write('***** PVCC is for YOU! *****\n')
    
    f.write(tr + 'Tuition' + endtd + str(num_credits) + endtd + format(tuitiontotal,currency) + endtr)
    f.write(tr + 'Capital fee' + endtd + str(num_credits) + endtd + format(capitaltotal,currency) + endtr)
    f.write(tr + 'Institution fee ' + endtd + str(num_credits) + endtd +  format(institutiontotal,currency)  + endtr)
    f.write(tr + 'Activity fee' + endtd + str(num_credits) + endtd + format(activitytotal,currency) + endtr)

    f.write(tr + 'Total' +  endtd + sp + endtd + format(subtotal,currency)  + endtr)     
    f.write(tr + 'Scholarships' + endtd + sp + endtd + format(scholarshipamt,currency) + endtr)
    f.write(tr + 'Balance' +     endtd + sp + endtd + format(total,currency) + endtr)
    
    f.write(colsp + 'Date/Time: '+ day_time + endtr)
    f.write('</table><br />')

##### call on main program to execute #####

main()
