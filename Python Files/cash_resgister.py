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

class Fruit:
    def __int__(self, name, price):
        self.name = name
        self.price = price


class CashRegister:
    cart = []  # Rework this class!!!
    items_in_cart = 0

    def __int__(self, price, cart):
        self.price = price

    def add_item(self, price):
        print(len(CashRegister.cart))


welcome_message = "Welcome to the Fruit Cart!"


def main():
    print(welcome_message.upper())
    answer = input("Would you like to add items to your cart? Yes or No: ")
    answer = answer.lower()
    if answer == "yes":
        while True:
            item = input("Please enter a fruit: ")
            #  price = input("Please enter a price for the item: ") Rework
            #  price = int(price)  Rework
            CashRegister.cart.append(item)
            #  CashRegister.add_item(price)  Rework
            if item == "stop":
                break
            print(CashRegister.cart)
    else:
        print("Thanks for stopping by!")
    pass


if __name__ == "__main__":
    main()