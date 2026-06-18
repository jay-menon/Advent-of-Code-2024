# This code is part of the Advent of Code 2024 challenge.
# Day 4: Ceres Search

# ///////// CLEANING PUZZLE INPUT /////////
with open("d4_input.txt") as raw_input:
    raw_wordsearch = raw_input.readlines()
    horz_nr_list = [i.strip("\n") for i in raw_wordsearch]
horz_r_list = [i[::-1] for i in horz_nr_list]

# ////////////////// PART 1 //////////////////
# Make lists of the rows/columns rev/non-rev
vert_nr_list = [None] * len(horz_nr_list)
for row in range(0, len(horz_nr_list)):
    curr_row = [i[row] for i in horz_nr_list]
    vert_nr_list[row] = "".join(curr_row)
vert_r_list = [i[::-1] for i in vert_nr_list]

# Verified the Wordsearch is SQUARE
print("Square Wordsearch: " + str(len(horz_nr_list) == len(vert_nr_list)))

# Make lists or diagonals rev/non-rev
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

# Collate all lists and count xmas in all of them
test_list = horz_r_list + horz_nr_list + vert_nr_list + vert_r_list + diag_TR_nr_list + diag_TR_r_list + diag_TL_nr_list + diag_TL_r_list
xmas_count = 0
for i in test_list:
    xmas_count += i.count("XMAS")
print("PART 1 /// XMAS Count: " + str(xmas_count))

# ////////////////// PART 2 //////////////////
# Finds position of As in all MAS or SAM in diagonal list
def mas_finder(diag_list):
    diag_pos_list = []
    for i in range(0,len(diag_list)):
        curr_str = diag_list[i]
        while curr_str.count("MAS") != 0 or curr_str.count("SAM") != 0:
            if curr_str.count("MAS") != 0:
                a_idx = curr_str.index("MAS") + 1
            elif curr_str.count("SAM") != 0:
                a_idx = curr_str.index("SAM") + 1
            diag_pos_list.append([i, a_idx])
            curr_str = curr_str[:a_idx] + "*" + curr_str[a_idx+1:]
    return diag_pos_list
# Converts position in diagonal list to position in horizontal list
def diag_to_horz_idx(diag_pos, len_horz):
    if diag_pos[0] <= len_horz-1:
        horz_pos = [diag_pos[0]-diag_pos[1], diag_pos[1]]
    else:
        horz_pos = [len_horz-1-diag_pos[1], (diag_pos[1]) - (len_horz-1) + diag_pos[0]]
    return horz_pos
# Checks if the diagonal MAS/SAM forms a cross against the horizontal list
def xmas_verifier(horz_pos, horz_list):
    test_str = horz_list[horz_pos[0]-1][horz_pos[1]-1] + "A" + horz_list[horz_pos[0]+1][horz_pos[1]+1]
    if test_str == "SAM" or test_str == "MAS":
        result = 1
    else:
        result = 0
    return result

cross_mas_count = 0
diag_pos_list = mas_finder(diag_TR_nr_list)
for pos in diag_pos_list:
    horz_pos = diag_to_horz_idx(pos, len(horz_nr_list))
    cross_mas_count += xmas_verifier(horz_pos,horz_nr_list)
print("PART 2 /// Cross MAS Count: " + str(cross_mas_count))



# test_horz= matrix = [
#     ['a', 'b', 'c', 'd', 'e'],
#     ['f', 'g', 'h', 'i', 'j'],
#     ['k', 'l', 'm', 'n', 'o'],
#     ['p', 'q', 'r', 's', 't'],
#     ['u', 'v', 'w', 'x', 'y']
# ]
# test_diag = [
#     'a',
#     'fb',
#     'kgc',
#     'plhd',
#     'uqmie',
#     'vrnj',
#     'wso',
#     'xt',
#     'y'
# ]

# test_idx = [6,1]
# print(test_diag[test_idx[0]][test_idx[1]])
# idx = diag_to_horz_idx(test_idx, 5)
# print(idx)
# print(test_horz[idx[0]][idx[1]])



