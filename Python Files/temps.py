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
        print("Welcome to the Temperature Tracker!")
        print("Please enter a data set of temperatures.\nWhen completed, please enter '*' to save your list.")  # This
        # line  denotes the sentinel value to be used to exit the loop
        print("Please only enter numbers!")
        print("_______________________________________________________")  # break line
        while True:
            temps = input("Please enter a temperature reading in Fahrenheit degrees: ")
            if temps == "":
                print("Please do not leave empty!")  # Catches an empty input value
            elif temps != "*":
                temperatures.append(temps)  # This adds the input value to the list
            else:
                break
        print(f"The temperatures entered were {temperatures}")  # This prints the temperatures
        # entered as required by the assignment guidelines.
        print(f"There were {len(temperatures)} entries in the list of temperatures")  # This prints how many
        # temperatures entered as required by the assignment guidelines
        print(f"The highest temperature entered was {max(temperatures)} degrees")  # This prints the max
        # temperatures entered as required by the assignment guidelines
        print(f"The lowest temperature entered was {min(temperatures)} degrees")  # This prints the min
        # temperatures entered as required by the assignment guidelines

    except ValueError:
        print("Oops!  That was not a valid number.  Try again...")


if __name__ == "__main__":
    main()
