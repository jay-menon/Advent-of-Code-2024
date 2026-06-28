# This code is part of the Advent of Code 2024 challenge.
# Day 5: Print Queue

# ///////// CLEANING PUZZLE INPUT /////////
with open("d5_input.txt") as raw_input:
    raw_page_order = raw_input.readlines()
    strip_page_order = [i.strip("\n") for i in raw_page_order]
split_idx = strip_page_order.index("")
order_list = strip_page_order[:split_idx]
update_list = strip_page_order[split_idx+1:]
