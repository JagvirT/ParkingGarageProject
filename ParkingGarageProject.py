class Parking_Garage():
    def __init__(self, name, pay_for_parking): 
        self.name = name
        self.pay_for_parking = pay_for_parking
        self.current_ticket = {}
        self.ticket_amount = 50
        self.parking_spaces = 50
        
#     - takeTicket
#    - This should decrease the amount of tickets available by 1
#    - This should decrease the amount of parkingSpaces available by 1
    
    def take_ticket(self): 
        self.ticket_amount -= 1
        self.parking_spaces -= 1
        pass

#  - Display an input that waits for an amount from the user and store it in a variable
#    - If the payment variable is not empty then (meaning the ticket has been paid) ->  display a message to the user that their ticket has been paid and they have 15mins to leave
#    - This should update the "currentTicket" dictionary key "paid" to True
    
    def for_parking(self):
        user_ticket_number = input('What is your ticket number?')
        amount = input('Please pay $20 for parking: (true or false)').lower()
        if amount == 'true':
            print('Thank you for paying! You have 15 minutes to exit the parking garage.')
            self.current_ticket[user_ticket_number] = amount
        else:
            print('Try again. please pay parking in order to exit')
        print(self.current_ticket)
        pass

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
                self.parking_spaces += 1
                self.ticket_amount += 1
            else:
                amount = input('Please pay $20 for parking: (true or false)').lower()

        
        
        
        # for value in self.current_ticket.value():
        #     if value == 'true':
        #         print('Thank You, have a nice day')
        #     elif value == 'false':



        pass



    
car = Parking_Garage('Kevon', ' ' )
car.for_parking()
car.leave_garage()




































#     def add_to_cart(self):
#         name = input('What are you adding to the cart? ').title()
#         number = input('What is the quantity? ')
#         self.depth_chart[name] = number
#         self.items_in_cart += 1
#         print(f'A quantity of {number} {name} was added to {self.name} cart.')

#     def remove_from_cart(self):
#         name = input('What item would you like to remove? ').title()
#         if name in self.depth_chart:
#             print(f'{name} was removed from {self.name} cart.')
#             del self.depth_chart[name] 
#             self.items_in_cart -= 1
#         else:
#             print('Item does not exist in cart.')

#     def show_cart(self):
#         print(f'---------- Current Items in {self.name} cart in {self.city} ----------')
#         print(f'Number of items: {self.items_in_cart}')
#         for k,v in self.depth_chart.items():
#             print(k,v)

#     def runner(self):
#         while True:
#             user_choice = input('What do you want to do? (add,remove,show,quit) ').lower()
#             if user_choice == 'add':
#                 self.add_to_cart()
#             elif user_choice == 'remove':
#                 self.remove_from_cart()
#             elif user_choice == 'show':
#                 self.show_cart()
#             elif user_choice == 'quit':
#                 self.show_cart()
#                 print(f'Thank for shopping {self.name}')
#                 break
#             else:
#                 print('Invalid option, please try again...')

                
            

# walmart = Store('Kevon','Fort Lauderdale')
# walmart.add_to_cart()
# # walmart.show_cart()
# # walmart.runner()