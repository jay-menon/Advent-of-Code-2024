# This code is part of the Advent of Code 2024 challenge.
# Day 5: Print Queue

# ///////// CLEANING PUZZLE INPUT /////////
with open("d5_input.txt") as raw_input:
    raw_page_order = raw_input.readlines()
    strip_page_order = [i.strip("\n") for i in raw_page_order]
split_idx = strip_page_order.index("")
str_rule_list = [i.split("|") for i in strip_page_order[:split_idx]]
str_upd_list = [i.split(",") for i in strip_page_order[split_idx+1:]]

# ////////////////// PART 1 //////////////////
# Function finds all relevant rules for an inputted update
def rule_finder(str_rule_list, str_update):
    rel_rule_list = []
    for rule in str_rule_list:
        if str_update[0] in rule and str_update[1] in rule:
            rel_rule_list.append(rule)
    return rel_rule_list
# Function tests if an inputted rule has been followed in an inputted update
def rule_tester(str_rule, str_update):
    if str_update.index(str_rule[0]) < str_update.index(str_rule[1]):
        return True
    return False

# Function testing
test_srl = [["1", "2"], ["4", "5"]]
test_su = ["1","2","3"]
print(rule_tester(test_srl[0],test_su))