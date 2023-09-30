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

# Change Log
# Change :2
# Changes Made: Defined two functions outside of main function
# Date of Change: 09/29/2023
# Author: Ruben Brionez Jr
# Change Approved by: Ruben Brionez Jr
# Date Moved to Production: 10/01/2023


def perform_calculation():  # This function takes an operation parameter and then requests
    # two number to perform the operation
    print("Enter two number")
    num1 = int(input("First number: "))
    num2 = int(input("Second number: "))
    print(f"Your first number was {num1} and your second number was {num2}")


def calculate_average():
    lst = []  # This is an empty list to store input
    n = int(input("Enter How many numbers to be averaged: "))
    for i in range(0, n):  # This for loop iterates over the input statement
        # based on the number entered and fills the list
        num = int(input("Please enter a number: "))
        lst.append(num)
    print(f"The numbers you entered were {lst}!")
    total = 0
    for num in lst:  # This for loop iterates over the list created by the user and sums the numbers
        total = total + num
    print(f"The sum of the numbers entered is {total}")
    average = round(total / n), 2
    print(f"The average of the numbers entered is {average:.2f}")


def main():
    try:
        #  perform_calculation()
        answer = input("Would you like to begin? Yes or No\n")
        while answer != "No" or "N":
            calculate_average()
            print("--------------------------------------------------")
            answer = input("Would you like to continue? Yes or No\n")

    except Exception:
        print("Please be sure to only enter numbers in the fields\nYou have existed the program, please run again")


if __name__ == "__main__":
    main()
