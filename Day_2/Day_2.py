# This code is part of the Advent of Code 2024 challenge.
# Day 2: Red-Nosed Reports

# ///////// CLEANING PUZZLE INPUT /////////
with open("d2_input.txt") as raw_input:
    raw_levels = raw_input.readlines()
split_levels = [i.split("\n") for i in raw_levels]
str_input = [i[0].split(" ") for i in split_levels]
int_input = [[int(j) for j in i] for i in str_input]
print(int_input)

# ////////////////// PART 1 //////////////////
