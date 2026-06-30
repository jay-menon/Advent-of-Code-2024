# This code is part of the Advent of Code 2024 challenge.
# Day 6: Guard Gallivant

# ///////// CLEANING PUZZLE INPUT /////////
with open("d6_input.txt") as raw_input:
    raw_map = raw_input.readlines()
strip_map = [i.strip("\n") for i in raw_map]
print(strip_map)