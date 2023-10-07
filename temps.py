# DSC 510
# Week 6
# Programming Assignment Week 6
# Author Ruben Brionez Jr
# 10/08/2023

# Change#:1
# Change(s) Made: Created program
# Date of Change: 10/04/2023
# Author: Ruben Brionez Jr
# Change Approved by: Ruben Brionez Jr
# Date Moved to Production: 10/08/2023

temperatures = []  # This creates an empty list to store input values


def main():
    try:
        print("Please enter a data set of temperatures.\nWhen completed, please enter '*' to save your list.")
        print("_______________________________________________________")
        while True:
            temps = input("Please enter a temperature reading in Fahrenheit degrees: ")
            if temps == "*":
                print("That completes the data set!")
                break
            elif temps != "*":
                temperatures.append(temps)
                #  print(temperatures)
            else:
                print("Make sure you entered a correctly formatted temperature!")
                break
        print(f"There were {len(temperatures)} entries in the list of temperatures")
        print(f"The highest temperature entered was {max(temperatures)}")
        print(f"The lowest temperature entered was {min(temperatures)}")
    except ValueError:
        print("Oops!  That was not a valid number.  Try again...")


if __name__ == "__main__":
    main()
