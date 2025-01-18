
'''
Your puzzle answer was 7492.

Both parts of this puzzle are complete! They provide two gold stars: **
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file
from utils.test_solution import test_solution

import re

@test_solution(name="DAY 14 PART 1", runs=10)
def main():
    print("\n### DAY 14 PART 2 ###")

    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt"))
    if not content: return
    nx, ny = 101, 103

    robots = [[*map(int, robot)] for robot in re.findall(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", content)]

    for k in range(2, 10**6):
        overlaps = 0
        env = [["."] * nx for _ in range(ny)]

        for robot in robots:
            [px, py, vx, vy] = map(int, robot)
            px = (px + vx * k) % nx
            py = (py + vy * k) % ny

            if env[py][px] == "#":
                overlaps += 1
            env[py][px] = "#"

        if overlaps == 0:
            break
    
    print(f"\n# SOLUTION: fewest number of seconds: {k}\n")

if __name__ == "__main__":
    main()