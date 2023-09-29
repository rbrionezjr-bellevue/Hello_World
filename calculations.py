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


def perform_calculation(operation):
    print("Enter two number")
    x = int(input("First number: "))
    y = int(input("Second number: "))
    if operation == "+":
        result = x + y
    elif operation == "-":
        result = x - y
    elif operation == "*":
        result = x * y
    else:
        result = x/y
    return result


def calculate_average():
    input("How many numbers would you like to enter: ")


def main():
    try:
        print("Hello World!")
    except Exception:
        print("End of Main Function")
