# This code is part of the Advent of Code 2024 challenge.
# Day 4: Ceres Search

# ///////// CLEANING PUZZLE INPUT /////////
with open("d4_input.txt") as raw_input:
    raw_wordsearch = raw_input.readlines()
    horz_nr_list = [i.strip("\n") for i in raw_wordsearch]
horz_r_list = [i[::-1] for i in horz_nr_list]

# ////////////////// PART 1 //////////////////
vert_nr_list = [None] * len(horz_nr_list)
for row in range(0, len(horz_nr_list)):
    curr_row = [i[row] for i in horz_nr_list]
    vert_nr_list[row] = "".join(curr_row)
vert_r_list = [i[::-1] for i in vert_nr_list]

# Verified the Wordsearch is SQUARE
print(len(horz_nr_list))
print(len(vert_nr_list))

def diag(list):
    new_list = []
    for i in range(0, len(list)):
        new_str = ""
        for j in range(0, i+1):
            a = j
            b = i - j
            new_str += list[b][a]
        new_list.append(new_str)

    for i in range(len(list), (len(list)*2)-1):
        new_str = ""
        for j in range(i-len(list)+1, len(list)):
            a = j
            b = i - j
            new_str += list[b][a]
        new_list.append(new_str)
    return new_list

diag_TR_nr_list = diag(horz_nr_list)
diag_TR_r_list  = [i[::-1] for i in diag_TR_nr_list]
diag_TL_nr_list = diag(horz_r_list)
diag_TL_r_list  = [i[::-1] for i in diag_TL_nr_list]

test_list = horz_r_list + horz_nr_list + vert_nr_list + vert_r_list + diag_TR_nr_list + diag_TR_r_list + diag_TL_nr_list + diag_TL_r_list
xmas_count = 0
for i in test_list:
    xmas_count += i.count("XMAS")
print("PART 1 /// XMAS Count: " + str(xmas_count))