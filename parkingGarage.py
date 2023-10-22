# Adrienne's Code Start
class parkingGarage():
    def __init__(self, tickets=5, parkingSpaces=5, currentTicket=False):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket

    
    def runner(self):
        while True:
            choose = input('What would you like to do? (take ticket, pay, leave, quit) ').lower()
            if choose == 'quit':
                print('Have a nice day! Please exit the garage to the ;eft leave. ')
                break
            if choose == 'take':
                self.takeTicket() 
            if choose == 'pay':
                self.payForParking()
            if choose == 'leave':
                self.leaveGarage()
            else:
                print('Invalid entry, please make a choice.')
               

    
    def takeTicket(self):
        tic_booth = int(input('Please press "1" to take ticket. '))
        if (tic_booth in self.tickets):
                self.tickets -= 1
                self.parkingSpaces -= 1
                self.currentTicket[tic_booth] = tic_booth
                print('Parking is $5/hour')


    def payForParking(self):
        pay_now = int(input('Please enter $15 to pay for your day parking '))
       
        while True:
            if pay_now == 15:
                print('Thank you for paying your ticket, you have 15 minuets to exit the garage.')
                self.currentTicket = True
                break
            elif pay_now < 15:
                pay_now = int(input('Invalid entry please pay for your parking. Please enter $15 to pay for your day parking. '))
        


   







Oop = parkingGarage()
Oop.runner()

