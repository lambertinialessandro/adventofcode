"""
Your puzzle answer was 1370.

The first half of this puzzle is complete! It provides one gold star: *
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from utils.read_file import read_file
from utils.test_solution import test_solution

@test_solution(name="DAY 04 PART 1", runs=100)
def main():
    print("\n### DAY 04 PART 1 ###")

    content = read_file(os.path.join(os.path.dirname(__file__), "input.txt"))
    if not content:
        return

    accessible_rolls = 0

    grid = content.strip().split("\n")
    rows = len(grid)
    cols = len(grid[0])
    print(rows, cols)

    for c in range(0, cols):
        for r in range(0, rows):
            if c == 0:
                if r == 0:
                    r1 = ""
                    r2 = grid[r][c:c+2]
                    r3 = grid[r+1][c:c+2]
                elif r == rows-1:
                    r3 = ""
                else:
                    r3 = grid[r+1][c:c+2]
            elif c == cols - 1:
                if r == 0:
                    r1 = ""
                    r2 = grid[r][c-1:c+1]
                    r3 = grid[r+1][c-1:c+1]
                elif r == rows-1:
                    r3 = ""
                else:
                    r3 = grid[r+1][c-1:c+1]
            else:
                if r == 0:
                    r1 = ""
                    r2 = grid[r][c-1:c+2]
                    r3 = grid[r+1][c-1:c+2]
                elif r == rows-1:
                    r3 = ""
                else:
                    r3 = grid[r+1][c-1:c+2]
                
            if grid[r][c] == "@":
                area_3_3 = r1 + r2 + r3
                # 5 = 4 adjacents + itself
                if area_3_3.count("@") < 5:
                    accessible_rolls += 1
            r1 = r2
            r2 = r3

    print(f"\n# SOLUTION: number of rolls of paper that can be accessed by a forklift: {accessible_rolls} {accessible_rolls == 1370}\n")


if __name__ == "__main__":
    main()
