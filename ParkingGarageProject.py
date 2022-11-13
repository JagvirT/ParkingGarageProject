class Parking_Garage():
    def __init__(self, name, pay_for_parking): 
        self.name = name
        self.pay_for_parking = pay_for_parking
        self.current_ticket = {}
        self.ticket_ammount = 50
        self.parking_spaces = 50
        

    def for_parking(self):
        name = input('Do you wish to purchase a parking ticket?: (true or false)')
        amount = input('Please pay $5 for 15 minutes of parking: ')
        print('Thank you for paying! Please proceed to parking spot for 15 minutes.')
        self.current_ticket[amount] = name
        print(self.current_ticket)
        pass

    def take_ticket(): 
        pass

    def leave_garage():
        pass



    
car = Parking_Garage('Kevon', ' ' )
car.for_parking()



































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