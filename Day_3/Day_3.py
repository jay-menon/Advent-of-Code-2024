# This code is part of the Advent of Code 2024 challenge.
# Day 3: Mull It Over

# ///////// CLEANING PUZZLE INPUT /////////
with open("d3_input.txt") as raw_input:
    raw_code_list = raw_input.readlines()
# Note that raw_code_list is a 6 item list of large blocks of code

# ////////////////// PART 1 //////////////////
# Parses code for m and when found, will check for correct mul formatting
# Also removes all code before+including m to shorten next search
def mul_finder(code):
    # Finds m and removes all before m, including the m
    # Including m so same m doesn't get picked up on next parse
    m_idx = code.index("m")
    trunc_code = code[m_idx+1:]
    # Testing formatting of the potential mul
    com_idx = trunc_code.index(",")
    brack_idx = trunc_code.index(")")
    if trunc_code[0:3] == "ul(" and com_idx < brack_idx:
        test_list = trunc_code[3:brack_idx].split(",")
        if len(test_list) == 2 and test_list[0].isdigit() and test_list[1].isdigit():
            return [[int(test_list[0]), int(test_list[1])], trunc_code]
    return [False, trunc_code]

sum = 0
for code in raw_code_list:
    curr_code = code
    for m in range(0,curr_code.count("m")):
        result = mul_finder(curr_code)
        if result[0] is not False:
            sum += result[0][0] * result[0][1]
        curr_code = result[1]

print("PART 1 /// Sum of Correctly Formatted Factors: " + str(sum))

# Overall strategy
# Take big input and use index to find an m
    # At that index, do a check to see if it's mul formatted correctly
    # If it is, do the multiplication and add to sum, if it isn't, ignore
    # Regardless of the outcome, remove all text before and including that m for the next parse
    # Repeat