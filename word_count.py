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


def add_word(file):
    counts = dict()
    for line in file:
        words = line.split()
        for word in words:
            if word not in counts:
                counts[word] = 1
            else:
                counts[word] = +1
    print(counts)


def process_line(file):
    counts = dict()
    for line in file:
        line = line.rstrip()
        line = line.translate(line.maketrans("","", string.punctuation))
        line = line.lower()
        words = line.split()
        print(words)


def pretty_print():
    pass


def main():
    try:
        gba_file = open('gettysburg.txt', 'r')
        for line in gba_file:
            process_line(gba_file)
    except Exception:
        print("What happened...?")


if __name__ == "__main__":
    main()