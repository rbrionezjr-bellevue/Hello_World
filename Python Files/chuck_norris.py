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
import json
from urllib.error import HTTPError


def categories():
    available_category = "https://api.chucknorris.io/jokes/categories"
    response = requests.get(available_category)
    api_data = response.json()
    api_dictionary = {key: value for key, value in enumerate(api_data, 1)}
    for key, value in api_dictionary.items():
        print(key, value)
    return api_dictionary


def joke(value):
    selected_category = f"https://api.chucknorris.io/jokes/random?category={value}"
    response = requests.get(selected_category)
    joke_data = response.json()
    joke_phrase = joke_data.get("value")
    print(joke_phrase)


def main():
    try:
        print("Welcome to the Chuck Norris Joke Generator!")
        while True:
            answer = input("Would you like a Chuck Norris Joke? Yes or No: ")
            answer = answer.lower()
            if answer == "yes":
                choices = categories()
                key = int(input("Please enter the number for the category: "))
                if key in range(1, 16):
                    value = choices.get(key)
                    print(f"You have selected the {value} category, enjoy this {value} Chuck Norris joke!")
                    print("--------------------------------------------------------------------------------")
                    joke(value)
                    print("--------------------------------------------------------------------------------")
                else:
                    print("Make sure you entered a number that corresponds to a category!")
            elif answer == "no":
                print("MAYBE NEXT TIME!")
                break
            else:
                print("Be sure to type 'Yes' or 'No'")
    except HTTPError as err:
        if err.code == 404:
            print("The webpage may have been moved, verify in browser")
        else:
            raise


if __name__ == "__main__":
    main()
