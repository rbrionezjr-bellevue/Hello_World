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

class CashRegister:
    #  Define a class variable somewhere for a available fruits and their prices?
    items_in_cart = 0

    def __int__(self, price):
        self.price = price

    def add_item(self, price):
        cart = []
        CashRegister.items_in_cart += 1  # This should increment each time an item is added with a price


welcome_message = "Welcome to the Fruit Cart!"


def main():
    price = 0
    cart = []
    print(welcome_message.upper())
    answer = input("Would you like to add items to your cart? Yes or No: ")
    answer = answer.lower()
    if answer == "yes":
        while True:
            item = input("Please enter a fruit: ")
            cart.append(item)
            if item == "stop":
                break
            print(cart)
    else:
        print("Thanks for stopping by!")
    pass


if __name__ == "__main__":
    main()