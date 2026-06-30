# This code is part of the Advent of Code 2024 challenge.
# Day 6: Guard Gallivant

# ///////// CLEANING PUZZLE INPUT /////////
with open("d6_input.txt") as raw_input:
    raw_map = raw_input.readlines()

horz_map = [i.strip("\n") for i in raw_map]
vert_map = []
for col_idx in range(0, len(horz_map[0])):
    new_str = ""
    for row_idx in range(0,len(horz_map)):
        new_str += horz_map[row_idx][col_idx]
    vert_map.append(new_str)

# ////////////////// PART 1 //////////////////
# Function finds knight's initial pos on the map
def init_pos(map):
    line_idx = 0
    for line in map:
        if line.count("^") == 1:
            return [line.index("^"), line_idx]
        line_idx += 1
    return "No initial pos found"
# Function takes knight's current position and outputs final pos, final ori(after 90deg) and range of the path taken
# If knight moves off map, function returns "Complete"
def knight_tracker(pos, ori, horz_map, vert_map):
    if ori == 0:
        path = vert_map[pos[0]][:pos[1]]
        if path.count("#") == 0:
            return "Complete", 1, [[pos[0], pos[0]], [pos[1], 0]]
        else:
            return [pos[0], pos[1]-path[::-1].index("#")], 1, [[pos[0], pos[0]], [pos[1], pos[1]-path[::-1].index("#")]]
    elif ori == 2:
        path = vert_map[pos[0]][pos[1]:]
        if path.count("#") == 0:
            return "Complete", 3, [[pos[0], pos[0]], [pos[1], len(vert_map[0])-1]] 
        else:
            return [pos[0], pos[1]+path.index("#")-1], 3, [[pos[0], pos[0]], [pos[1], pos[1]+path.index("#")-1]]
    elif ori == 1:
        path = horz_map[pos[1]][pos[0]:]
        if path.count("#") == 0:
            return "Complete", 2, [[pos[0], len(horz_map[0])-1], [pos[1], pos[1]]]
        else:
            return [pos[0]+path.index("#")-1, pos[1]], 2, [[pos[0], pos[0]+path.index("#")-1], [pos[1], pos[1]]]
    elif ori == 3:
        path = horz_map[pos[1]][:pos[0]]
        if path.count("#") == 0:
            return "Complete", 0, [[pos[0], 0], [pos[1], pos[1]]]
        else:
            return [pos[0]-path[::-1].index("#"), pos[1]], 0, [[pos[0], pos[0]-path[::-1].index("#")], [pos[1], pos[1]]]
# Function takes a range of positions and ouputs each individual position visited as a list
def range_to_pos(t_range):
    pos_list = []
    if t_range[0][0] == t_range[0][1]:
        for i in range(min(t_range[1]), max(t_range[1])+1):
            pos_list.append([t_range[0][0],i])
    else:
        for i in range(min(t_range[0]), max(t_range[0])+1):
            pos_list.append([i, t_range[1][0]])
    return pos_list
# Function only adds new positions visited to the old position list
def consol_lists(old_pos_vis, pos_list):
    new_pos_list = list(old_pos_vis)
    for pos in pos_list:
        if pos not in old_pos_vis:
            new_pos_list.append(pos)
    return new_pos_list

curr_pos = init_pos(horz_map)
curr_ori = 0
curr_pos_list = []
while curr_pos != "Complete":
    [curr_pos, curr_ori, path_range] = knight_tracker(curr_pos, curr_ori, horz_map, vert_map)
    pos_list = range_to_pos(path_range)
    curr_pos_list = consol_lists(curr_pos_list, pos_list)
print(len(curr_pos_list))

