# DSC 510
# Week 5
# Programming Assignment 5.1
# Author Ruben Brionez
# 09/27/2023

# Change Log
# Change :1
# Changes Made: Created Program
# Date of Change: 09/28/2023
# Author: Ruben Brionez Jr
# Change Approved by: Ruben Brionez Jr
# Date Moved to Production: 10/01/2023


def perform_calculation():
    print("Enter two number")
    num1 = int(input("First number: "))
    num2 = int(input("Second number: "))
    print(f"Your first number was {num1} and your second number was {num2}")


def calculate_average():
    x = int(input("How many numbers would you like to enter: "))
    while x > 0:
        input("Please enter a number: ")
        x = x - 1
    #  test = [1, 2, 3, 4]
    #  for num in test:
        #  print(num)


def main():
    try:
        #  perform_calculation()
        calculate_average()
    except Exception:
        print("End of Main Function")


if __name__ == "__main__":
    main()