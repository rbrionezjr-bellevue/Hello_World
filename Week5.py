# DSC 510
# Week 5
# Programming Assignment 5.1
# Author Ruben Brionez
# 09/27/2023

def perform_calculation(choice):  # This function takes an operation parameter and then requests
    #  two number to perform the operation
    print("Enter two number please")
    num1 = int(input("First number: "))
    num2 = int(input("Second number: "))
    print(f"Your first number was {num1} and your second number was {num2}")
    if choice == "+":
        val = num1 + num2
    elif choice == "-":
        val = num1 - num2
    elif choice == "*":
        val = num1 * num2
    elif choice == "/":
        val = num1 * num2
    else:
        print("You have not selected a correct operation\nPlease try again!")
    print(f"The operation selected was {choice} and the value of the two numbers is {val}")
    return val


def calculate_average():  # This function takes as many numbers entered by the user
    # and generates an average of the entered numbers
    lst = []  # This is an empty list to store input
    n = int(input("Enter How many numbers to be averaged: "))
    for i in range(0, n):  # This for loop iterates over the input statement
        # based on the number entered and fills the list
        num = int(input("Please enter a number: "))
        lst.append(num)  # This is what adds the entered numbers into the list
    print(f"The numbers you entered were {lst}!")
    total = 0
    for num in lst:  # This for loop iterates over the list created by the user and sums the numbers
        total = total + num
    print(f"The sum of the numbers entered is {total}")
    average = total / n
    round(average, 2)
    print(f"The average of the numbers entered is {average:.2f}")  # This is formatted to
    # show average at 2 decimal places


def main():  # This is the main function program that used to call the previously defined functions
    try:
        while True:  # While the answer is True the user can continue to run the program
            answer = input("Would you like to run the calculation program? Yes or No\n")
            answer = answer.upper()
            if answer == "YES":
                print("Please select from the following operations: +, -, *, /")
                choice = input("Please select the operation: ")
                perform_calculation(choice)

            elif answer == "NO":
                answer = input("Would you like to run the average program? Yes or No\n")
                answer = answer.upper()
                if answer == "YES":
                    calculate_average()
                else:
                    break
            else:
                print("Please be sure you've entered a correct value")
                print("Try again!")
                break
            print("--------------------------------------------------")
    except Exception:
        print("Please be sure you've entered a correct value")  # This line only prints when the user has not
        # entered a correct value when prompted
    print("You have existed the program, please run again!")


if __name__ == "__main__":
    main()