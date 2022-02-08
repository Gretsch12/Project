fout = open('p.txt', 'w' )
tax = 0.0775    



#Implements the sales system and adds the numbers with the users selection
def salestax (choice):
    sub = 0
    for i in choice:
        sub +=(i[1])
    print(choice)
    print('Subtotal: ${:.2f}'.format(sub))
    
    shipping = sub * .05
    print('Shipping: $ {:.2f}'.format(shipping))
    
    amount = tax*sub
    print('tax: \t ${:.2f}' .format(amount))
    
    total = sub + amount + shipping
    print('Total: \t $ {:.2f}'.format(total))
    
    P(choice, sub, total, shipping)


#Prints out the receipt by writing on the file selected for storage
def P(choice, sub, total, shipping):
    fout.write('      Funko & More Store...      \n')
    for i in choice:
        fout.write('{} $ {}\n'.format(i[0],i[1]))
    fout.write('''
_______________________________
Subtotal:  $ {:.2f}
Shipping:  $ {:.2f}
Tax:       %{}
Total:     ${:.2f}
________________________________
Thank you for shopping at your friendly NeighboorHood Store :)!!...
'''.format(sub,shipping,tax*100,total))
    
    fout.close()
    


#implements the users information into the selected file
def cusinfo(fname,lname,streetnum,address,zip,number):
    file = open('p.txt', 'a+')
    file.write('\n........Buyers Information........\n')
    file.write('\nName:'+fname+' ' +lname)
    file.write('\nAddress:'+streetnum+' '+address)
    file.write('\nZipcode:'+zip)
    file.write('\nPhone number: '+'{}-{}-{}'.format(number[:3],number[3:6],number[6:])+'\n')


#Verifies users input for the delivery date
def delivery(date,month,year):
    if date.isdigit():
        print('Delivery date:', date)
    else:
        input('Enter a valid date: ')
    if month.isdigit():
        print('Delivery month:', month)
    else:
        input('Enter a valid month: ')
    if year.isdigit():
        print('Delivery year:', year)
    else:
        input('Enter a valid year: ')
    
        
#Verifies user input for the time of delivery
def times (hour,min):
    if hour.isdigit():
        print('Delivery month:', hour)
    else:
        input('Enter a valid month: ')
    if min.isdigit():
        print('Delivery min:', min)
    else:
        input('Enter a valid min: ')
   
    
#Implements user information onto the selected file
def information (date, month, year,hour,min):
    file = open('p.txt', 'a+')
    file.write('\n____________Shipping & Delivery Information__________\n')
    file.write('\nDelivery date: '+ month +','+ date +','+ year)
    file.write('\nTime of delivery:'+hour+':'+min+'pm')
    file.seek(0)


#Prints out the user information 
def r_info():
    with open('p.txt', 'r')as f:
        print(f.read())


