# Adrienne's Code Start
class parkingGarage():
    def __init__(self, tickets=10, parkingSpaces=10, currentTicket='not paid'):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket

def takeTicket(self):
       
    tic_booth = int(input('Please press "1" to take ticket.'))
    while True:
        if tic_booth == int(1):
            self.tickets -= 1
            self.parkingSpaces -= 1
            break # ????
            # self.currentTicket += 1???
            # print('Parking is $5/hour')

        # I feel like there should be an elif here...below
        elif tic_booth == int(1):
            self.ticket == 0 & self.parkSpaces == 0
            print('Sorry the parking garage is FULL.')
            break # ????
        else:
            print('Please reverse and exit the parking garage.')


def payForParking(self):
    pay_for_ticket = input('Your total is $25. Hit "Yes" to pay now or "No" to pay later.').lower()
    while True:   # readME says use true dictionary
        if pay_for_ticket == 'yes':
            self.currentTicket = ('Paid')
            print('Thank you, your ticket is now paid and you will have 15 minutes to exit the parking garage.')
        elif pay_for_ticket == 'no':
            self.currentTicket = ('Not paid')
            print('Please pay when exiting the parking garage.')
        else:
            self.currentTicket = ('Not paid')
            print('Please pay before leaving the parking garage.')

    # park_cost = int(input(''))
    # if park_cost <= 1:
    #     print('Please pay $5')

    # elif park_cost > 1:
    #     print('Please pay ')

    # pc_var = park_cost
    
                  

def leaveGarage(self):
    while True:
        if self.currentTicket == 'paid':
            print('Thank you, have a nice day!')
            self.tickets += 1
            self.parkingSpaces += 1
            break
        elif self.currentTicket == 'Not paid':
           pay_now = input('Please hit "Pay now" to pay for parking ticket')
        if pay_now == True:
            print('Thank you, have a nice day!')
            self.tickets += 1
            self.parkingSpaces += 1
        else:
            print('You must pay before EXITING!')


def runner(self):
    while True:
        choose = input('What would you like to do? (take, pay or leave)').lower()
        if choose == 'take':
            self.takeTicket()
        
        elif choose == 'pay':
            self.payforParking()

        elif choose == 'leave':
            break

        else:
            print('Thank you, have a nice day!')


oop = parkingGarage()
oop.runner()



# # Kevin's Code Start
# # class kev_navigator(): ??

#     def takeTicket(self):
#         # self.tickets = []
        
#     def payForParking(self):
        

#     def leaveGarage(self):
      

#     def payment(self):
      

# # Kevin's Code End

# Oop = parkingGarage('tickets', 'parkingSpaces', 'currentTicket')
# Oop.runner()


# Danny's Code Start

# Danny's Code End
