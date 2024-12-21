
'''
Your puzzle answer was 208437768.

The first half of this puzzle is complete! It provides one gold star: *
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file
from utils.test_solution import test_solution

import re
import math

@test_solution(name="DAY 14 PART 1", runs=100)
def main():
    print("\n### DAY 14 PART 1 ###")

    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt"))
    if not content: return
    nx, ny = 101, 103
    midx, midy = nx//2, ny//2

    robots = re.findall(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", content)
    env = [["."] * nx for _ in range(ny)]
    quadrants = [0, 0, 0, 0]

    for robot in robots:
        [px, py, vx, vy] = map(int, robot)
        px = (px + vx * 7492) % nx
        py = (py + vy * 7492) % ny

        env[py][px] = "#"
        if px != midx and py != midy:
            quadrants[(0 if px < midx else 2) + (0 if py < midy else 1)] += 1

    for line in env: print("".join(map(str, line)))
    
    print(quadrants)
    safety_factor = math.prod(quadrants)
    print(f"\n# SOLUTION: __: {safety_factor}\n")

if __name__ == "__main__":
    main()