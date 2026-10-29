
'''
Your puzzle answer was 118392478819140.

Both parts of this puzzle are complete! They provide two gold stars: **
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file
from utils.test_solution import test_solution

from functools import cache


numeric_btns = {
    "7": [0, 0], "8": [0, 1], "9": [0, 2],
    "4": [1, 0], "5": [1, 1], "6": [1, 2],
    "1": [2, 0], "2": [2, 1], "3": [2, 2],
                 "0": [3, 1], "A": [3, 2]
}
directional_btns = {
                 "^": [0, 1], "A": [0, 2],
    "<": [1, 0], "v": [1, 1], ">": [1, 2],
}


@cache
def compute_row(dr):
    if dr > 0:
        return "v" * dr
    return "^" * -dr

@cache
def compute_column(dc):
    if dc > 0:
        return ">" * dc
    return "<" * -dc


@cache
def compute_numeric(curr_code, next_code):
    [curr_r, curr_c] = numeric_btns[curr_code]
    [next_r, next_c] = numeric_btns[next_code]
    delta_r = next_r - curr_r
    delta_c = next_c - curr_c
    
    if curr_c == 0 and next_r == 3:
        return compute_column(delta_c) + compute_row(delta_r) + "A"
    if curr_r == 3 and next_c == 0:
        return compute_row(delta_r) + compute_column(delta_c) + "A"

    if delta_c < 0:
        return compute_column(delta_c) + compute_row(delta_r) + "A"
    else:
        return compute_row(delta_r) + compute_column(delta_c) + "A"
    
@cache
def compute_directional(curr_code, next_code):
    [curr_r, curr_c] = directional_btns[curr_code]
    [next_r, next_c] = directional_btns[next_code]
    delta_r = next_r - curr_r
    delta_c = next_c - curr_c
    
    if curr_r == 0 and next_c == 0:
        return compute_row(delta_r) + compute_column(delta_c) + "A"
    if curr_c == 0 and next_r == 0:
        return compute_column(delta_c) + compute_row(delta_r) + "A"
    
    if delta_c < 0:
        return compute_column(delta_c) + compute_row(delta_r) + "A"
    else:
        return compute_row(delta_r) + compute_column(delta_c) + "A"


@cache
def compute_robots(parent_seq, depth):
    char_count = 0
    code = "A"
    for single_code in parent_seq:
        
        if depth == 1:
            [curr_r, curr_c] = directional_btns[code]
            [next_r, next_c] = directional_btns[single_code]
            delta_r = next_r - curr_r
            delta_c = next_c - curr_c
            char_count += abs(delta_r) + abs(delta_c) + 1
        else:
            sequence = compute_directional(code, single_code)
            char_count += compute_robots(sequence, depth-1)
        
        code = single_code
    
    return char_count

@cache
def compute_door(parent_seq, number_of_robots):
    
    # Door
    code = "A"
    char_count = 0
    for single_code in parent_seq:
        
        # Robots
        sequence = compute_numeric(code, single_code)
        char_count += compute_robots(sequence, number_of_robots)

        code = single_code
            
    return char_count

@test_solution(name="DAY 21 PART 2", runs=100)
def main():
    print("\n### DAY 21 PART 2 ###")
    
    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt")).strip()
    if not content: return

    codes = content.split("\n")

    number_of_robots = 25
    complexity_sum = 0
    for code in codes:
        char_count = compute_door(code, number_of_robots)
        
        numeric_part = int(code[:-1])
        
        print(f"Code {code} = {char_count} * {numeric_part}")
        complexity_sum += char_count * numeric_part

    
    print(f"\n# SOLUTION: sum of complexities of all codes: {complexity_sum}\n")

if __name__ == "__main__":
    main()
