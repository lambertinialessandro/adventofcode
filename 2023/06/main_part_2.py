
'''
Your puzzle answer was 30077773.

Both parts of this puzzle are complete! They provide two gold stars: **
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file
from utils.test_solution import test_solution

import re
import math

@test_solution(name="DAY 06 PART 2", runs=100)
def main():
    print("\n### DAY 06 PART 2 ###")

    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt")).strip()
    if not content: return

    Ts, Ys = [[int(number) for number in re.findall("\d+", line)] for line in content.split("\n")]
    print(Ts, Ys)

    T = int("".join(map(str, Ts)))
    y = int("".join(map(str, Ys)))
    print(f"T: {T}, y: {Ys}")

    delta = T**2-4*y
    print(f"delta: {delta}")

    x1_r, x2_r = (T - math.sqrt(delta)) / 2, (T + math.sqrt(delta)) / 2
    x1, x2 = math.floor(x1_r) + 1, math.ceil(x2_r)
    print(f"x1: {x1_r}, x2: {x2_r}")
    print(f"x1: {x1}, x2: {x2}, diff: {x2 - x1}")

    print(f"\n# SOLUTION: total ways to beat the record: {x2 - x1}\n")


if __name__ == "__main__":
    main()
