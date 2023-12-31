# DSC 510
# Week 4
# Programming Assignment Week 3
# Author: Ruben Brionez Jr
# 09/17/2023
# Labor cost calculator for fiber install with bulk discount

# Change Log
# Change :1
# Changes Made: Created Program
# Date of Change: 09/09/2023
# Author: Ruben Brionez Jr
# Change Approved by: Ruben Brionez Jr
# Date Moved to Production: 09/09/2023

# Change Log
# Change :2
# Changes Made: Implemented an if conditional to account for bulk discount pricing
# Date of Change: 09/13/2023
# Author: Ruben Brionez Jr
# Change Approved by: Ruben Brionez Jr
# Date Moved to Production: 09/17/2023

# Change Log
# Change :3
# Changes Made: Added bulk discount statement
# Date of Change: 09/14/2023
# Author: Ruben Brionez Jr
# Change Approved by: Ruben Brionez Jr
# Date Moved to Production: 09/17/2023

# Change Log
# Change :4
# Changes Made: Added a function to calculate the cost
# Date of Change: 09/19/2023
# Author: Ruben Brionez Jr
# Change Approved by: Ruben Brionez Jr
# Date Moved to Production: 09/24/2023

# Change Log
# Change :5
# Changes Made: defined a main function that calculates cost and is currently only called when run from main program
# Date of Change: 09/22/2023
# Author: Ruben Brionez Jr
# Change Approved by: Ruben Brionez Jr
# Date Moved to Production: 09/24/2023
def calc(feet, price):  # This defines a function that takes two parameter and multiplies them
    total_cost = round(feet * price, 2)  # Round the result to two decimal places
    return total_cost  # This line returns the value of multiplied parameter and stores it


def main():
    try:
        print("****Welcome to the Calculator****")
        company = input("Please enter the company name:\n")  # This line requests a company name be entered
        feet_install = (int(input("Please enter the footage for the cable.\nPlease round to the nearest foot\n")))
        # The above line requests an input footage and converts to an int
        if feet_install > 500:  # This starts the IF conditional statement for bulk pricing discounts
            price = 0.50
        elif feet_install > 250:
            price = 0.70
        elif feet_install > 100:
            price = 0.80
        else:
            price = 0.87

        print("_______________________________________________________")  # Line seperator
        print(f"The Company name entered was '{company}'\nThe total footage entered was {feet_install} FT\n"
              f"The price per foot is ${price:.2f}\nThe total cost is ${calc(feet_install, price):.2f}")  # This is an F
        # string that prints the customer a receipt with needed information, price and cost formatted
        # to 2 decimal places
        if price != 0.87:  # This conditional statement add a printed message
            # to let the customer know they received a discount
            print(f"You received a bulk discount of ${0.87 - price:.2f} per foot".upper())  # Prints discount per foot
        else:
            pass  # This allows the program to pass the else statement without an error
        print("_______________________________________________________")  # Line seperator
        print("Thank you!".upper())  # Thank you message to uppercase
    except Exception:
        print("Please be sure to enter numbers only for the footage.\nBe sure to round to the nearest foot.\n"
              "Please run the calculator again!")  # This line should
        # capture any errors at the input level that will allow the user to re-run the program and be sure
        # the correct values are entered


if __name__ == "__main__":
    main()
