#Final Project..
import calendar
import P
#Entry menu where it introduces what the store has to offer
print('Welcome into our Funko & More Store electronic store.....')
def menu():
    print('Please select from the following....')
    print('[1] Purchase')
    print('[2] Store Information & Shipping Information')
    print('[0] Exit..')    
menu()

option = int(input('Please make your selection... '))

while option != 0:
    if option == 1:
                    #Menu selection of what is offered using dictionary
        print('Welcome to the Funko & More Store..., Please make your selection...')

        product ={1:('Common Funko Pop', 11.99), 2:('Grail Funko Pop', 99.99), 3:('Mid-Range Funko Pop',49.99), 4:('PlayStation 5 Game', 59.99),
                  5:('Nintendo Switch Game', 49.99),6:('Xbox Series X Game', 59.99), 7:('Retro Game', 39.99),
                  9:('Manga', 9.99), 10:('Booster Pack', 3.99), 11:('Booster Box', 11.99), 12:('Autographed Funko pop', 149.99)}
        print('These are products offered in our store.... ')


        #Prints the listed items in the dictionary
        for a, b in product.items():
            print('{}) {}: ${}'.format(a, b[0], b[1]))

        choice = []
        #Implements selection of the user
        keep_choosing = 'Y'
        while keep_choosing == 'Y':
            pick = int(input('\nWhat is your choice: '))
            # if else, generated and notes the choices of the user
            if pick in product.keys():
                choice.append((product[pick][0], product[pick][1]))
            else:
                print('Invalid Choice, Select from the list of products...')
                while pick <= 0 or pick > 9:
                    pick = int(input('What is your choice: '))
                    choice.append((product[pick][0], product[pick][1]))
            #Promt the user if they want to continue purchasing        
            keep_choosing = input('Keep Choosing(Y for yes, N for no): ').upper()

        P.salestax(choice)


        print('\nPlease Enter your information below...')
        #Asks for the users information and home directions
        try:
            fname = input('Enter your first name: ')
            assert fname.isalpha()
        except:
            raise ValueError('Number has numbers!')

        try:
            lname = input('Enter your last name: ')
            assert lname.isalpha()
        except:
            raise ValueError('Number has numbers!')

        try:
            streetnum = input('Enter your street number: ')
            assert streetnum.isdigit()
        except:
            raise ValueError('Number has letters!')
            
        try:
            address = input('Enter your address name: ')
            assert address.isalpha()
        except:
            raise ValueError('Number has all letters or all numbers!')

        try:
            zip = input('Enter your zip: ')
            assert zip.isdigit()
        except:
            raise ValueError('Number has letters!')
            
        try:
            number = input('Enter your phone number: ')
            assert number.isdigit()
            print('{}-{}-{}'.format(number[:3],number[3:6],number[6:]))
        except:
            raise ValueError('Number has letters!')

        P.cusinfo(fname,lname,streetnum,address,zip,number)


        # Ask user for prefered delivery date with while methods
        print('\nShipping: 7 days a week, within a year of purchase date...')
        #Validates the year input
        year = input('Input desired year for shipping: ')
        while  year != "2022" and year != "2023":
            year = input('Invalid: Enter year from till next avialable purchase date: ')
        #Validates the month input
        month = input('Input desired month for shipping: ')
        while month != "1" and month != "2" and month != "3" and month != "4" and month != "5" and month != "6" and month != "7" and month != "8"and month != "9" and month != "10" and month != "11" and month != "12":
            month = input('Invalid: Input desired month for shipping: ')
        #Gaps the users selection within a years purchase    
        while month == '1' and year == '2022':
            print("Invalid, Month unavailable, make another selection..")
            month = input('Input desired delivery month: ')  
        while month == '3' and year == '2023':
            print("Invalid, coming soon.. Pick another month...")
            month = input('Input desired delivery month: ')

        # displays a calander for a better view and selection of date    
        mm = int(month)
        yy = int(year)
        print(calendar.month(yy,mm))
        #validates the date input
        date = input('Enter desired date of delivery: ')
        while date < '1' or date > '31': 
            print("Invalid, Pick another date...")
            date = input('Enter desired date of delivery: ')

        P.delivery(date,month,year)


        # Asks the user when is the best time for delivery implementing while methods
        print("\nTimes of delievery are start at 12:00pm and end at 5:00pm...")

        devtimes = ['12:00pm', '12:30pm', '1:00pm', '1:30pm', '2:00pm',
                    '3:00pm','3:30pm','4:00pm','4:30pm', '5:00pm','5:30pm']  
        print(*devtimes, sep = "\n")

        print('Please select the best time for delivery....')
        #Validates the hour  slot input
        hour = input('Enter desired hour for delivery: ')
        while  hour != '12' and hour != '1' and hour !='2' and  hour != '3' and hour !='4' and hour != '5':
            hour = input('Invalid: Enter valid delivery hour: ')
        #Validates the minute slot input
        min = input('Enter desired minute slot for delivery: ')
        while min != '30' and min !='00':
            min = input('Invalid: Enter valid desired minute slot for delivery: ')

        P.times(hour,min)
        P.information(date,month,year,hour,min)
        P.r_info()

        break
    elif option == 2:
        #Class used to store the store information
        class parent():
            def __init__ (self):
                self.name = None
        class storeinfo(parent):
            def __init__ (self):
                super().__init__()
                self.address = None
                self.phone = None
         #Information written and printed out
        store1 = storeinfo()
        store1.name = '\nFunko & More Store: Small mom and pop shop located in the Heat of IE'
        store1.address = '2309 Python st, Riverside CA 92506'
        store1.phone = '(951)888-9000'
        print(store1.name, '\nAddress:',store1.address,'\nPhone:', store1.phone)
        #Class written store the delivery and shipping information
        class shipping():
            def __init__(self):
                self.shipcost = None
                self.shiptime = None
                self.deliverytime = None
        #Information writen and printed as the user has choosen        
        storeI = shipping()
        storeI.shipcost = 'The cost for shipping items averages to be 5% of the subtotal'
        storeI.shiptime = 'Shipping is 7 days a week, within a year of purchase date'
        storeI.deliverytime = 'We deliver 7 days a week between the hours of 12:00 pm to 6:00pm'
        print('\nCost of shipping:', storeI.shipcost, '\nDelivery dates:',storeI.shiptime,'\nTime of delivery:', storeI.deliverytime)
        
    else:
        #invalid selection has been selected
        print ('Invalid selection....')
    menu()
    option = int(input('\nPlease make your selection... '))

print('Thank you, Please come again....')
            
    
    
    
    
    