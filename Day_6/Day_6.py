# This code is part of the Advent of Code 2024 challenge.
# Day 6: Guard Gallivant

# ///////// CLEANING PUZZLE INPUT /////////
with open("d6_input.txt") as raw_input:
    raw_map = raw_input.readlines()

horz_map = [i.strip("\n") for i in raw_map]

horz_map = [
    "....#.....",
    ".........#",
    "..........",
    "..#.......",
    ".......#..",
    "..........",
    ".#..^.....",
    "........#.",
    "#.........",
    "......#..."
]

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

def new_path_count(test_range, range_list):
    overlap_count = 0
    if test_range[0][0] == test_range[0][1]:
        range_len = abs(test_range[1][0]-test_range[1][1])+1
        for old_range in range_list:
            if old_range[0][0] != old_range[0][1] and test_range[0][0] >= min(old_range[0][0],old_range[0][1]) and test_range[0][0] <= max(old_range[0][0],old_range[0][1]):
                if old_range[1][0] >= min(test_range[1][0],test_range[1][1]) and old_range[1][0] <= max(test_range[1][0],test_range[1][1]):
                    overlap_count += 1
    else:
        range_len = abs(test_range[0][0]-test_range[0][1])+1
        for old_range in range_list:
            if old_range[1][0] != old_range[1][1] and test_range[1][0] >= min(old_range[1][0],old_range[1][1]) and test_range[1][0] <= max(old_range[1][0],old_range[1][1]):
                if old_range[0][0] >= min(test_range[1][0],test_range[1][1]) and old_range[0][0] <= max(test_range[1][0],test_range[1][1]):
                    overlap_count += 1
    return range_len - overlap_count

# Testing
initial_pos = init_pos(horz_map)
#print(knight_tracker(init_pos, 0, horz_map, vert_map))

ground_covered = 0
curr_pos = initial_pos
curr_ori = 0
path_range_list = []
while curr_pos != "Complete":
    [curr_pos, curr_ori, path_range] = knight_tracker(curr_pos, curr_ori, horz_map, vert_map)
    print(curr_pos)
    ground_covered += new_path_count(path_range, path_range_list)
    path_range_list.append(path_range)
print(ground_covered)

