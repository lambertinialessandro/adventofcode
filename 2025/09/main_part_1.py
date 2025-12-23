"""
Your puzzle answer was 4781377701.

The first half of this puzzle is complete! It provides one gold star: *
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from utils.read_file import read_file
from utils.test_solution import test_solution

import math


@test_solution(name="DAY 09 PART 1", runs=100)
def main():
    print("\n### DAY 09 PART 1 ###")

    content = read_file(os.path.join(os.path.dirname(__file__), "input.txt"))
    if not content:
        return

    couples = [[*map(int, line.split(","))] for line in content.strip().split("\n")]

    max_area = 0
    for i, [x1, y1] in enumerate(couples):
        for [x2, y2] in couples[i + 1 :]:
            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            if area > max_area:
                max_area = area

    print(f"\n# SOLUTION: the largest area of any rectangle you can make is: {max_area}\n")


if __name__ == "__main__":
    main()
