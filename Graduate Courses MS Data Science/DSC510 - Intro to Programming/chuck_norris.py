# DSC 510
# Week 10
# Programming Assignment 10.1 Week 10
# Author Ruben Brionez Jr
# 11/05/2023

# Change Log
# Change :1
# Changes Made: Created Program
# Date of Change: 11/03/2023
# Author: Ruben Brionez Jr
# Change Approved by: Ruben Brionez Jr
# Date Moved to Production: 11/05/2023

import requests
from urllib.error import HTTPError


def categories():  # This function uses the API to generate the available categories
    available_category = "https://api.chucknorris.io/jokes/categories"  # Uses the api to retrieve available categories
    response = requests.get(available_category)
    api_data = response.json()
    api_dictionary = {key: value for key, value in enumerate(api_data, 1)}  # This line adds a numeric key to the
    # retrieved categories
    for key, value in api_dictionary.items():
        print(key, value)  # This line prints the key and value (number and category)
    return api_dictionary  # This line returns the dictionary for use in main


def joke(value):  # This function uses the API to generate a joke based on user input
    selected_category = f"https://api.chucknorris.io/jokes/random?category={value}"  # This line Uses the api to
    # retrieve a joke from the selected category
    response = requests.get(selected_category)
    joke_data = response.json()
    joke_phrase = joke_data.get("value")  # This line uses retrieves that value from the parsed json (a dictionary)
    print(joke_phrase)


def main():
    try:
        print("Welcome to the Chuck Norris Joke Generator!")
        while True:  # The while loop allows the user to run the program multiple times if they choose
            answer = input("Would you like a Chuck Norris Joke? Yes or No: ")
            answer = answer.lower()
            if answer == "yes":
                choices = categories()  # This line creates a variable from the returned dictionary in order to allow
                # the user to select a category based on the number/key from the dictionary.
                key = int(input("Please enter the number for the category: "))
                if key in range(1, 16):  # This if statement is a check to verify that the entered key is
                    # associated with a value/category
                    value = choices.get(key)
                    print(f"You have selected the {value} category, enjoy this {value} Chuck Norris joke!")
                    print("--------------------------------------------------------------------------------")  # Line
                    # for separation
                    joke(value)  # Calls the joke function
                    print("--------------------------------------------------------------------------------")  # Line
                    # for separation
                else:
                    print("Make sure you entered a number that corresponds to a category!")
            elif answer == "no":
                print("MAYBE NEXT TIME!")
                break
            else:
                print("Be sure to type 'Yes' or 'No'")
    except HTTPError as err:  # This error exception should catch a 404 if the webpage is not available
        if err.code == 404:
            print("The webpage may not be available or has moved, verify in browser")
        else:
            raise


if __name__ == "__main__":
    main()
