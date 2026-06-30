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
        if rule[0] in str_update and rule[1] in str_update:
            rel_rule_list.append(rule)
    return rel_rule_list
# Function tests if an inputted rule has been followed in an inputted update
def rule_tester(str_rule, str_update):
    if str_update.index(str_rule[0]) < str_update.index(str_rule[1]):
        return True
    return False

sum = 0
upd_to_fix_list = []
for update in str_upd_list:
    rule_broken = False
    rel_rules = rule_finder(str_rule_list, update)
    for rule in rel_rules:
        if rule_tester(rule, update) is False:
            rule_broken = True
            upd_to_fix_list.append(update)
            break
    if rule_broken is False:
        sum += int(update[int((len(update)-1)/2)])
print("Sum of Ordered Update Middle Nums: " + str(sum))

# ////////////////// PART 2 //////////////////
# Takes in an update and a set of rules, outputs the furthest left number
def left_num(update, rule_list):
    for update_num in update:
        not_furth_left = False
        for rule in rule_list:
            if rule[1] == update_num:
                not_furth_left = True
                break
        if not_furth_left is False:
            return update_num
# Takes in a number, rules list and update, outputs all rule list and update without that number
def rule_strip(num, update, rules):
    new_rules = []
    for rule in rules:
        if num not in rule:
            new_rules.append(rule)
    new_upd = list(update)
    new_upd.remove(num)
    return [new_upd, new_rules]
# Finds middle index item in an odd length list:
def mid_item(list_arg):
    if len(list_arg) % 2 == 1:
        return list_arg[int((len(list_arg)-1)/2)]
    else:
        return "List is even lengthed"

sum = 0
for update in upd_to_fix_list:
    rel_rules = rule_finder(str_rule_list, update)
    fixed_update = []
    [curr_update, curr_rules] = [update, rel_rules]

    while len(fixed_update) != len(update):
        leftmost = left_num(curr_update, curr_rules)
        fixed_update.append(leftmost)
        [curr_update, curr_rules] = rule_strip(leftmost, curr_update, curr_rules)

    mid_num = int(mid_item(fixed_update))
    sum += mid_num
print("Sum of Fixed Ordered Update Middle Nums: " + str(sum))