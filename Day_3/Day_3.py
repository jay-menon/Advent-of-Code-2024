# This code is part of the Advent of Code 2024 challenge.
# Day 3: Mull It Over

# ///////// CLEANING PUZZLE INPUT /////////
with open("d3_input.txt") as raw_input:
    raw_code_list = raw_input.readlines()
# Note that raw_code_list
print(len(raw_code_list))

# Overall strategy
# Take big input and use index to find an m
    # At that index, do a check to see if it's mul formatted correctly
    # If it is, do the multiplication and add to sum, if it isn't, ignore
    # Regardless of the outcome, remove all text before and including that m for the next parse
    # Repeat