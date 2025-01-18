
'''
Your puzzle answer was 94426.

The first half of this puzzle is complete! It provides one gold star: *

+---+---+---+
| 7 | 8 | 9 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
    | 0 | A |
    +---+---+

    +---+---+
    | ^ | A |
+---+---+---+
| < | v | > |
+---+---+---+
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file
from utils.test_solution import test_solution

def compute_row(dr):
    if dr < 0:
        return "v" * -dr
    return "^" * dr
def compute_column(dc):
    if dc < 0:
        return ">" * -dc
    return "<" * dc

@test_solution(name="DAY 21 PART 1", runs=100)
def main():
    print("\n### DAY 21 PART 1 ###")

    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt")).strip()
    if not content: return

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

    codes = content.split("\n")

    complexity_sum = 0
    for code in codes:
        numeric_part = int(code[:-1])

        # Door
        [r, c] = numeric_btns["A"]
        char_count = 0
        door_code = ""
        for single_code in code:
            [nr, nc] = numeric_btns[single_code]
            dr, dc = r - nr, c - nc

            if r < 3:
                door_code += compute_column(dc) + compute_row(dr) + "A"
            else:
                door_code += compute_row(dr) + compute_column(dc) + "A"

            #char_count += abs(dr) + abs(dc) + 1
            r, c = nr, nc
        
        # Robots
        [r, c] = directional_btns["A"]
        robot_code = ""
        for single_code in door_code:
            [nr, nc] = directional_btns[single_code]
            dr, dc = r - nr, c - nc
            #print([r, c], [nr, nc], [dr, dc])

            if r < 1:
                robot_code += compute_row(dr) + compute_column(dc) + "A"
            else:
                robot_code += compute_column(dc) + compute_row(dr) + "A"

            #char_count += (abs(dr) + abs(dc) + 1) * 2
            r, c = nr, nc
        
        [r, c] = directional_btns["A"]
        human_code = ""
        for single_code in robot_code:
            [nr, nc] = directional_btns[single_code]
            dr, dc = r - nr, c - nc
            #print([r, c], [nr, nc])
            #print(single_code, [dr, dc])

            if r < 1:
                human_code += compute_row(dr) + compute_column(dc) + "A"
            else:
                human_code += compute_column(dc) + compute_row(dr) + "A"

            char_count += abs(dr) + abs(dc) + 1
            r, c = nr, nc

        print(code, char_count, numeric_part, char_count * numeric_part)
        print(f"door_code: {door_code}")
        print(f"robot_code: {robot_code}")
        print(f"human_code: {human_code}")
        
        complexity_sum += char_count * numeric_part

    
    print(f"\n# SOLUTION: sum of complexities of five codes: {complexity_sum}\n")

if __name__ == "__main__":
    main()