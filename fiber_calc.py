# DSC 510
# Week 2
# Programming Assignment Week 2
# Author: Ruben Brionez Jr
# 09/09/2023
# Labor cost calculator for fiber install

# Change Log
# Change :1
# Changes Made: Created Program
# Date of Change: 09/09/2023
# Author: Ruben Brionez Jr
# Change Approved by: Ruben Brionez Jr
# Date Moved to Production: 09/09/2023

try:
    print("****Welcome to the Calculator****")
    company = input("Please enter the company name:\n")  # This line requests a company name be entered
    feet_install = (float(input("Please enter the footage for the cable.\n")))  # This line requests an input footage
    # and converts to a float
    cost = round((feet_install * 0.87), 2)  # This line multiplies the footage by 0.87 and
    # then rounds to two decimal places
    print("**************************************************")  # Line seperator
    print(f"The Company name entered was '{company}'\nThe total footage entered was {feet_install} FT\n"
          f"The price per foot is $0.87\nThe total cost is ${cost}")
    print("**************************************************")  # Line seperator
    print("Thank you!")
except Exception:
    print("Please be sure to enter numbers only for the footage.\nPlease run the calculator again!")  # This line should
    # capture any errors at the input level that will allow the user to re-run the program and be sure
    # the correct values are entered
