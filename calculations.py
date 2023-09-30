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
    lst = []
    n = int(input("Enter How many number to be averaged: "))
    for i in range(0, n):
        num = int(input("Please enter a number: "))
        lst.append(num)
    print(f"The numbers you entered were {lst}!")
    total = 0
    for num in lst:
        total = total + num
    print(f"The sum of the numbers entered is {total}")
    average = total / n
    print(f"The average of the numbers entered is {average}")


def main():
    try:
        #  perform_calculation()
        answer = input("Would you like to begin? Yes or No\n ")
        while answer != "No":
            calculate_average()
            answer = input("Would you like to continue? Yes or No\n ")

    except Exception:
        print("End of Main Function")


if __name__ == "__main__":
    main()