
'''
Your puzzle answer was 4811940.

The first half of this puzzle is complete! It provides one gold star: *
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file
from utils.test_solution import test_solution

import re
import math

@test_solution(name="DAY 06 PART 1", runs=100)
def main():
    print("\n### DAY 06 PART 1 ###")

    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt")).strip()
    if not content: return

    Ts, Ys = [[int(number) for number in re.findall("\d+", line)] for line in content.split("\n")]
    print(Ts, Ys)

    prod_solutions = 1
    for T, y in zip(Ts, Ys):
        print(f"T: {T}, y: {y}")

        delta = T**2-4*y
        print(f"delta: {delta}")

        x1_r, x2_r = (T - math.sqrt(delta)) / 2, (T + math.sqrt(delta)) / 2
        x1, x2 = math.floor(x1_r) + 1, math.ceil(x2_r)
        print(f"x1: {x1_r}, x2: {x2_r}")
        print(f"x1: {x1}, x2: {x2}, diff: {x2 - x1}")

        prod_solutions *= x2 - x1

    print(f"\n# SOLUTION: total times multiplied: {prod_solutions}\n")

if __name__ == "__main__":
    main()
