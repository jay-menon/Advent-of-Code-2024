# This code is part of the Advent of Code 2024 challenge.
# Day 2: Red-Nosed Reports

# ///////// CLEANING PUZZLE INPUT /////////
with open("d2_input.txt") as raw_input:
    raw_levels = raw_input.readlines()
split_levels = [i.split("\n") for i in raw_levels]
str_input = [i[0].split(" ") for i in split_levels]
int_input = [[int(j) for j in i] for i in str_input]

# ////////////////// PART 1 //////////////////
# Rule 1: Ascending/descending only rule // Rule 2: Gradual change rule
def rule1(report):
    level_copy = list(report)
    level_copy.sort()
    if report == level_copy or report == list(reversed(level_copy)):
        return True
    return False
def rule2(report):
    prev_level = report[0]
    for i in report[1:]:
        curr_level = i
        diff = abs(prev_level - curr_level)
        if diff < 1 or diff > 3:
            return False
        prev_level = i
    return True

# Checks if rules for safety are met for each report in input
safe_count = 0
unsafe_reports = []
for i in int_input:
    if rule1(i) is True and rule2(i) is True:
        safe_count += 1
    else:
        unsafe_reports.append(i)
print("PART 1 /// Freq. of Safe Reports: " + str(safe_count))

# ////////////////// PART 2 //////////////////

# Returns 1 if the dampener made the unsafe report safe, else, returns 0
def dampener(unsafe_report):
    def rule1(report):
        level_copy = list(report)
        level_copy.sort()
        if report == level_copy or report == list(reversed(level_copy)):
            return True
        return False
    def rule2(report):
        prev_level = report[0]
        for i in report[1:]:
            curr_level = i
            diff = abs(prev_level - curr_level)
            if diff < 1 or diff > 3:
                return False
            prev_level = i
        return True
    # Take out all levels individually and check if rules now met
    for i in range(0,len(unsafe_report)):
        copy = list(unsafe_report)
        copy.pop(i)
        if rule1(copy) is True and rule2(copy) is True:
            return 1
    return 0

# Check how many of the unsafe reports have now become safe
for i in unsafe_reports:
    safe_count += dampener(i)
print("PART 2 /// New Freq. of Safe Reports: " + str(safe_count))