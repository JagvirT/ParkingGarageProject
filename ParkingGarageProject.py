class Parking_Garage():
    def __init__(self, name):
        self.name = name
        self.available_ticket = ['111', '112', '113', '114', '115', '116', '117', '118', '119', '120']
        self.current_ticket = {}
        self.ticket_amount = 10
        self.parking_spaces = 10
#     - takeTicket
#    - This should decrease the amount of tickets available by 1
#    - This should decrease the amount of parkingSpaces available by 1
    

#  - Display an input that waits for an amount from the user and store it in a variable
#    - If the payment variable is not empty then (meaning the ticket has been paid) ->  display a message to the user that their ticket has been paid and they have 15mins to leave
#    - This should update the "currentTicket" dictionary key "paid" to True
    
    def for_parking(self):
        self.ticket_amount -= 1
        self.parking_spaces -= 1
        print(self.available_ticket)
        user_ticket_number = input('What is your ticket number? ')
        amount = input('Do you want to pay now or later? (Now/Later)').lower()
        if user_ticket_number in self.available_ticket and amount == 'now':
            self.available_ticket.remove(user_ticket_number)
            self.current_ticket[user_ticket_number] = "true"
        elif amount == 'later':
            self.available_ticket.remove(user_ticket_number)
            self.current_ticket[user_ticket_number] = 'false'
        else:
            print('Try again. please pay parking in order to exit')
            pass
        # else:
        #     print('Unknown ticket number input, please enter a valid ticket number:')
        # amount = input('Please pay $20 for parking: (true or false)').lower()
        # if amount == 'true':
        #     print('Thank you for paying! You have 15 minutes to exit the parking garage.')
        #     self.current_ticket[user_ticket_number] = amount
        # elif amount == 'false':
        #     self.current_ticket[user_ticket_number] = amount
        # else:
        #     print('Try again. please pay parking in order to exit')
        #     pass
        print(self.current_ticket)
            

#     -leaveGarage
#    - If the ticket has been paid, display a message of "Thank You, have a nice day"
#    - If the ticket has not been paid, display an input prompt for payment
#       - Once paid, display message "Thank you, have a nice day!"
#    - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
#    - Update tickets list to increase by 1 (meaning add to the tickets list)
    
    def leave_garage(self):
        user_ticket_number = input('What is your ticket number?')
        for key, value in self.current_ticket.items():
            if key == user_ticket_number and value == 'true':
                print ('Thank You, have a nice day')
                #del self.current_ticket[user_ticket_number] 
                self.parking_spaces += 1
                self.ticket_amount += 1
                break
            elif key == user_ticket_number and value == 'false':
                print(f'Please pay ticket number: {user_ticket_number}')
                user_input = input('Please pay $20 for parking: (yes/no)' ).lower()
                if user_input == 'yes':
                    self.current_ticket[user_ticket_number]= 'true'
                    self.parking_spaces += 1
                    self.ticket_amount += 1
                    print ('Thank You, have a nice day')
                    break
                else:
                    print('Please see management ticket need to be paid in person now')
                    self.parking_spaces += 1
                    self.ticket_amount += 1
                    break
            

   

        
        
        
        # for value in self.current_ticket.value():
        #     if value == 'true':
        #         print('Thank You, have a nice day')
        #     elif value == 'false':



        pass

    def show_garage_space(self):
        if self.available_ticket == {}:
            print("Parking Garage Full")
        print(f'---------- Current Space in {self.name} Parking Garage')
        print(f'Parking Space = {self.parking_spaces}')
        print(f'Ticket Amount = {self.ticket_amount}')
        print(f'Space Available{self.available_ticket}')
        
       
    def runner(self):
        while True:
            user_choice = input("what do you want to do? (take ticket/pay ticket/available spots?" ).lower()
            if user_choice == "take ticket":
                self.for_parking()
            elif user_choice == "pay ticket":
                self.leave_garage()
            elif user_choice == "available spots":
                self.show_garage_space()
                print('thank you for parking')
                
            else:
                print("Invalid Option")



car = Parking_Garage('South Beach')
# car.take_ticket()
#car.for_parking()
# car.leave_garage()
# car.show_garage_space()
car.runner()



































