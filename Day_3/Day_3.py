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

# Loops through each code in the code list, finding and checking formatting of each m
# Adds result of each correctly formatted m to sum
sum = 0
for code in raw_code_list:
    curr_code = code
    for m in range(0,curr_code.count("m")):
        result = mul_finder(curr_code)
        if result[0] is not False:
            sum += result[0][0] * result[0][1]
        curr_code = result[1]
print("PART 1 /// Sum of Correctly Formatted Factors: " + str(sum))

# ////////////////// PART 2 //////////////////
# Same as the first but modified for do() and dont()
# def mul_finder_2(code):

#     m_idx = code.index("m")
#     # Checks if do or dont activate before the current m
#     dont = False
#     if "don't()" in code[:m_idx]:
#         # This is the string before the m in reverse order
#         rev_precode = code[:m_idx][::-1]
#         if "do()" in code[:m_idx]:
#             do_idx = rev_precode.find(")(od")
#             dont_idx = rev_precode.find(")(t'nod")
#             if dont_idx < do_idx:
#                 dont = True
#         else:
#             dont = True

#     if dont is True:
#         # Removes all code between don't and next do
#         next_do_idx = code[m_idx:].find("do()")
#         trunc_code = code[m_idx+next_do_idx+4:]
#         return [False, trunc_code]
#     else:
#         # Finds m and removes all before m, including the m
#         # Including m so same m doesn't get picked up on next parse
#         trunc_code = code[m_idx+1:]
#         # Testing formatting of the potential mul
#         com_idx = trunc_code.index(",")
#         brack_idx = trunc_code.index(")")
#         if trunc_code[0:3] == "ul(" and com_idx < brack_idx:
#             test_list = trunc_code[3:brack_idx].split(",")
#             if len(test_list) == 2 and test_list[0].isdigit() and test_list[1].isdigit():
#                 return [[int(test_list[0]), int(test_list[1])], trunc_code[brack_idx:]]
#         return [False, trunc_code]

# sum = 0
# for code in raw_code_list:
#     curr_code = code
#     m_count = code.count("m")
#     while m_count != 0:
#         print(m_count)
#         result = mul_finder_2(curr_code)
#         if result[0] is not False:
#             #print(str(result[0][0]) + " " + str(result[0][1]))
#             sum += result[0][0] * result[0][1]
#         curr_code = result[1]
#         m_count = curr_code.count("m")
# print("PART 2 /// New Sum: " + str(sum))

def mulfinder2(code):
    sum = 0
    curr_code = code
    while curr_code.count("mul(") != 0:
        mul_idx = curr_code.index("mul(")
        # Testing formatting of the potential mul
        trunc_code = curr_code[mul_idx+4:]
        com_idx = trunc_code.index(",")
        brack_idx = trunc_code.index(")")
        if com_idx < brack_idx:
            test_list = trunc_code[:brack_idx].split(",")
            if len(test_list) == 2 and test_list[0].isdigit() and test_list[1].isdigit():
                sum += int(test_list[0]) * int(test_list[1])
        curr_code = trunc_code
    return sum

def dont_do_cutter(code):
    curr_code = code + "don't()"
    saved_code = ""
    while curr_code.count("don't()") != 0:
        dont_idx = curr_code.index("don't()")
        saved_code += curr_code[:dont_idx]
        if "do()" in curr_code[dont_idx:]:
            next_do_idx = curr_code[dont_idx:].index("do()")
            curr_code = curr_code[dont_idx+next_do_idx+4:]
        else:
            curr_code = ""
    return saved_code

overall_string = ""
for code in raw_code_list:
    overall_string += code
cut_code = dont_do_cutter(overall_string)
sum = mulfinder2(cut_code)
print("PART 2 /// New Sum: " + str(sum))

# test = "AAAAAAAAdon't()BBBBBBBBBBBdo()don't()do()CCCdon't()EEEdon't()FFdo()GG"
# print(dont_do_cutter(test))