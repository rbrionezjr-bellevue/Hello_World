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

# Change Log
# Change :2
# Changes Made: Implemented an if loop to account for bulk discount pricing
# Date of Change: 09/13/2023
# Author: Ruben Brionez Jr
# Change Approved by: Ruben Brionez Jr
# Date Moved to Production: 09/17/2023

try:
    print("****Welcome to the Calculator****")
    company = input("Please enter the company name:\n")  # This line requests a company name be entered
    feet_install = (int(input("Please enter the footage for the cable.\nPlease round to the nearest foot\n")))  # This
    # line requests an input footage and converts to an int
    if feet_install > 500:  # This starts the IF loop for bulk pricing discounts
        price = 0.50
    elif feet_install > 250:
        price = 0.70
    elif feet_install > 100:
        price = 0.80
    else:
        price = 0.87
    cost = (round((feet_install * price), 2))

    print("**************************************************")  # Line seperator
    print(f"The Company name entered was '{company}'\nThe total footage entered was {feet_install} FT\n"
          f"The price per foot is ${price:.2f}\nThe total cost is ${cost:.2f}")
    print("**************************************************")  # Line seperator
    print("Thank you!")
except Exception:
    print("Please be sure to enter numbers only for the footage.\nPlease run the calculator again!")  # This line should
    # capture any errors at the input level that will allow the user to re-run the program and be sure
    # the correct values are entered
