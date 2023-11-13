# DSC 510
# Week 10
# Programming Assignment 10.1 Week 10
# Author Ruben Brionez Jr
# 11/12/2023

# Change Log
# Change :1
# Changes Made: Created Program
# Date of Change: 11/08/2023
# Author: Ruben Brionez Jr
# Change Approved by: Ruben Brionez Jr
# Date Moved to Production: 11/12/2023

# Change Log
# Change :2
# Changes Made: Updated Program and corrected the __init__ to correctly initialize the variables
# Date of Change: 11/12/2023
# Author: Ruben Brionez Jr
# Change Approved by: Ruben Brionez Jr
# Date Moved to Production: 11/12/2023

import locale
region = locale.getlocale()
locale.setlocale(locale.LC_MONETARY, region)


class CashRegister:

    def __init__(self, price, count=0, total=0):
        self.price = price
        self.total = total
        self.count = count
        self.cart = []

    def add_item(self, price):
        if len(self.cart) == 1:
            self.total = price
        else:
            self.total += price
        self.count = len(self.cart)
        # print(f"Your current total is {CashRegister.total}")
        # print(f"There are {len(CashRegister.item_price)} items in your cart")
        return self.total, self.count

    @property
    def get_total(self):
        return self.total

    @property
    def get_count(self):
        return self.count


message_header = "-------------------------"
welcome_message = "Welcome to the Fruit Cart!"
message_footer = "-------------------------"
fruits = ['apple', 'banana', 'pear', 'blueberry', 'strawberry', 'grape', 'peach', 'orange', 'tangerine', 'blackberry',
          'watermelon', 'cantaloupe', 'coconut', 'pineapple', 'pumpkin']


def main():
    cart = []
    total = 0
    count = 0
    register = CashRegister(cart, total, count)  # Creates instance of CashRegister Class in Main()
    print(message_header)
    print(welcome_message.upper())  # Prints a Welcome Message to the user
    print(message_footer)
    try:
        answer = input('Would you like to add items to your cart? Yes or No: ')
        answer = answer.lower()
        if answer == "yes":
            item = ""  # Sets item to empty string to begin the while loop
            while item.lower() != 'quit':
                item = input('Enter a fruit or enter "quit" to exit: ')
                if item.lower() not in fruits and item.lower() != 'quit':  # This line is meant to check that the input
                    # is in the list of available fruits and that the user has not entered 'quit'
                    print("That's not a fruit we have!")
                elif item.lower() in fruits:
                    register.cart.append(item.lower())  # Fills the cart which is an empty list class variable
                    while True:
                        price = float(input('Enter price: '))
                        if price < 0 or price > 3.00:
                            print("The price of our fruit is between 0.00 and 3.00")
                        else:
                            register.add_item(price)  # Calls the Class Method add_item and fills the parameter price
                            print(f'The current total is {locale.currency(register.get_total, grouping=True)}')
                            break
                else:
                    break
            # see comments at  Class Method for more details
            print(message_header)
            print(f"Your total is {locale.currency(register.get_total, grouping=True)}")  # Sets the output to be in
            # users local currency
            print(f"There were {register.get_count} items(s) in your cart")
            print(message_footer)
        else:
            print("Thanks for stopping by!")
    except ValueError:  # This ValueError exception will catch a sting entered into the price variable.
        print("Be sure you enter the correct value for 'price'!")


if __name__ == "__main__":
    main()
