# DSC 510
# Week 5
# Programming Assignment 5.1
# Author Ruben Brionez
# 09/27/2023

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


perform_calculation("+")
