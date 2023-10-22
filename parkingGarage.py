class ParkingGarage():
    def __init__(self, tickets = 150, parkingSpaces = 150, currentTicket=False):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket


    def runner(self):
        while True:
            choose = input('What would you like to do? (take ticket, pay, leave, quit) ').lower()
            if choose == 'quit':
                print('Have a nice day! Please exit the garage to the left. ')
                break
            elif choose == 'take':
                self.takeTicket() 
            elif choose == 'pay':
                self.payForParking()
            elif choose == 'leave':
                self.leaveGarage()
            else:
                print('Invalid entry, please make a choice.')
                

    def takeTicket(self):
        tic_booth = int(input('Please press 1 to take ticket. '))

        while True:
            if tic_booth == 1:
                print(f'Please pull forward to park')
                self.tickets -= 1
                self.parkingSpaces -= 1
                print(f'There are {self.parkingSpaces} open spaces left.')    
            else:
                print(f'Invalid entry, please press 1 for a ticket')
            break




    
    def payForParking(self):
        pay_now = int(input('Please enter $15 to pay for your day parking '))
       
        while True:
            if pay_now == 15:
                print('Thank you for paying your ticket, you have 15 minutes to exit the garage.')
                self.currentTicket = True
                break
            elif pay_now < 15:
                pay_now = int(input('Invalid entry please pay for your parking. Please enter $15 to pay for your day parking. '))
            else:
                break



    def leaveGarage(self):
        pay_status = int(input('Please enter $15 to pay for your day parking '))
        
        while True:
            if pay_status == 15:
                print('Thank you for paying your ticket, you have 15 minutes to exit the garage.')
                self.currentTicket = False
                break
            elif pay_now < 15:
                pay_now = int(input('Invalid entry please pay for your parking. Please enter $15 to pay for your day parking. '))

        self.tickets += 1
        self.parkingSpaces += 1
        print(f'There are {self.parkingSpaces} available.')
 
Oop = ParkingGarage() 
Oop.runner()





