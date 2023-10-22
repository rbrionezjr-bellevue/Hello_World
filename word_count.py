# DSC 510
# Week 8
# Programming Assignment 8.1 Week 8
# Author Ruben Brionez Jr
# 10/19/2023

# Change Log
# Change :1
# Changes Made: Created Program
# Date of Change: 10/19/2023
# Author: Ruben Brionez Jr
# Change Approved by: Ruben Brionez Jr
# Date Moved to Production: 10/22/2023

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


def pretty_print(counts):  # This line is intended to create a more readable output
    longest = 0
    lst = list()
    for key, val in list(counts.items()):
        lst.append((val, key))
        total = len(lst)
    print(f"Length of the dictionary is: {total}")
    print("Word     Count")
    print("--------------")
    lst.sort(reverse=True)
    for key, val in lst:
        print(f"{val}{key :^ }")


def main():
    try:
        gba_file = open('gettysburg.txt', 'r')
        counts = dict()
        for line in gba_file:
            process_line(line, counts)
        pretty_print(counts)

    except:
        print("File cannot be opened:", gba_file)
        exit()


if __name__ == "__main__":
    main()