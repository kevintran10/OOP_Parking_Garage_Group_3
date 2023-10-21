# Adrienne's Code Start
class parkingGarage():
    def __init__(self, tickets=5, parkingSpaces=5, currentTicket=False):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket

    
    def runner(self):
        while True:
            choose = input('What would you like to do? (take ticket, pay, leave) ').lower()

            if choose == 'take':
                self.takeTicket()

            elif choose == 'pay':
                self.payForParking()

            elif choose == 'leave':
                break
            else:
                print('Have a nice day!')

    
    def takeTicket(self):
        tic_booth = int(input('Please press "1" to take ticket. '))
        if (tic_booth in self.tickets):
                self.tickets -= 1
                self.parkingSpaces -= 1
                self.currentTicket[tic_booth] = tic_booth
                print('Parking is $5/hour')


    def payForParking(self):
        pay_now = int(input('How may hours would you like to park? '))
        pay_later = input()
        # park_hours = int(input(''))
        if pay_now == True:
            print('Please pay $5')


            elif park_hours > 1:
            print('Please pay ')
            pass
        


    def leaveGarage(self):
        if park_cost == 5:
            print('Thank you for paying your ticket, have a nice day!')
        elif
            self.currentTicket == 0:
            print('Please pay parking ticket.')
        else:
            print('Thank you, have a nice day!')
            self.tickets += 1
            self.parkingSpaces += 1
            self.currentTicket[tic_booth] = tic_booth







Oop = parkingGarage('tickets', 'parkingSpaces', 'currentTicket')
Oop.runner()

