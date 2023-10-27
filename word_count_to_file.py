# DSC 510
# Week 9
# Programming Assignment 9.1 Week 9
# Author Ruben Brionez Jr
# 10/24/2023

# Change Log
# Change :1
# Changes Made: Created Program
# Date of Change: 10/24/2023
# Author: Ruben Brionez Jr
# Change Approved by: Ruben Brionez Jr
# Date Moved to Production: 10/29/2023

import string


def add_word(words, counts):  # loops over the dictionary and adds the amount of times a word shows up
    for word in words:
        if word not in counts:  # This ensures that a word only showing up once is counted
            counts[word] = 1
        else:
            counts[word] += 1  # This increments words that appear more than once


def process_line(line, counts):  # This processes each line if the text file, the for loop is in "main"
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))  # This line removes punctuation
    line = line.lower()  # This line converts all capital letters to lowercase
    words = line.split()  # This splits the words in the lines to be counted
    add_word(words, counts)  # This line calls the function to calculate the times a word appears


def process_file(counts, new_file):  # This line is intended to create a more readable output from the dictionary
    len_pairs = []  # Created an empty list
    for key, val in list(counts.items()):  # This loop places the key:value pair in a list in order to get a total
        len_pairs.append((val, key))  # adds the key,value par to the empty list
        total = len(len_pairs)  # totals the key/value paris in the list (This would be the total
    with open(new_file, 'w') as new_hand:
        width = 15
        filler = " "
        new_hand.write(f"Length of the dictionary is: {total}\n")
        column1 = "Word"
        column2 = "Count"
        new_hand.write(f"{column1:{filler}<{width}} {column2}\n")
        new_hand.write("------------------------\n")
        len_pairs.sort(reverse=True)
        for key, val in len_pairs:
            new_hand.write(f"{val:{filler}<{width}} {key:02}\n")


def main():
    try:
        file_name = input("Enter the file name: ")
        new_file = input("Please enter a name for the new file to write to: ")
        with open(file_name, 'r') as file_hand:  # Opens desired file
            with open(new_file, 'w') as new_hand:
                counts = dict()  # creates an Empty dictionary
                for line in file_hand:
                    process_line(line, counts)
            print(len(counts))
        process_file(counts, new_file)
    except FileNotFoundError:
        print("File cannot be opened\nPlease be sure the file path is correct!")


if __name__ == "__main__":
    main()