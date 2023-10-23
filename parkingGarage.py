class ParkingGarage():
    def __init__(self, tickets = 150, parkingSpaces = 150, currentTicket=False):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket


    def runner(self):
        while True:
            choose = input('What would you like to do? Show availability, take ticket, pay ticket, leave garage or quit.: ').lower()
            if choose == 'quit':
                print('Have a nice day! Please exit the garage to the left. ')
                break
            elif choose == 'show':
                self.showSpaces()
            elif choose == 'take':
                self.takeTicket() 
            elif choose == 'pay':
                self.payForParking()
            elif choose == 'leave':
                self.leaveGarage()
            else:
                print('Invalid entry, please make another choice.')

    
    def showSpaces(self):
        open_spaces = int(input('Press 1 to see how may open spaces.: '))

        while True:
            if open_spaces == 1:
                print(f'There are {self.parkingSpaces} spaces open')
                break
            if open_spaces != 1:
                open_spaces = int(input('Invalid entry please enter 1 to see available spaces.: '))


    def takeTicket(self):
        tic_booth = int(input('Please press 2 to take ticket.: '))
       
        while True:
            if tic_booth == 2:
                print(f'Please pull forward to park.')
                self.tickets -= 1
                self.parkingSpaces -= 1
                print(f'There are {self.parkingSpaces} open spaces left.')  
                break  
            if tic_booth > 2:
                tic_booth = int(input('Invalid entry, please press 1 to take ticket.: '))

    
    def payForParking(self):
        pay_now = int(input('Please enter 15 to pay for your day parking ticket.: '))
       
        while True:
            if pay_now == 15:
                print("Thank you for paying your ticket, you have 15 minutes to exit the garage. Select 'leave' to leave garage.")
                self.currentTicket = True
                break
            elif pay_now < 15:
                pay_now = int(input('Invalid entry please pay for your parking. Please enter 15 to pay for your day parking.: '))
           

    def leaveGarage(self):
        pay_status = int(input('Please enter 3 to leave, if parking is not paid, enter 15 to pay for your day parking.: '))
        
        while True:
            if pay_status == 3:
                print('Thank you have a nice day!')
                self.currentTicket == True
                self.tickets += 1
                self.parkingSpaces += 1
                print(f'There are {self.parkingSpaces} available spaces.')
                break
            elif self.currentTicket == False:
                break
            elif pay_status == 15:
                self.currentTicket == False
                print('Please enter 15 to pay for your parking ticket.: ')
                break
    
Oop = ParkingGarage() 
Oop.runner()





