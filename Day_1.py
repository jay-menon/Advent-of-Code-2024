# This code is part of the Advent of Code 2024 challenge.
# Day 1: Historian Hysteria

# ///////// CLEANING PUZZLE INPUT /////////
with open("d1_input.txt") as raw_input:
    raw_ranges = raw_input.readlines()
stripped_input = [i.strip("\n") for i in raw_ranges]
clean_input = [i.split("   ") for i in stripped_input]
int_input = [[int(i[0]), int(i[1])] for i in clean_input]
# print(int_input)

# ////////////////// PART 1 //////////////////
# Sort each list by order of their distances
lst1 = sorted([i[0] for i in int_input])
lst2 = sorted([i[1] for i in int_input])
comb_list = zip(lst1, lst2)
# Sum the abs. difference between the same ranked distances in each list
sum = 0
for i in comb_list:
    sum += abs(i[0]-i[1])
print("PART 1 /// Sum of Differences in Distances: " + str(sum))