"""
Your puzzle answer was 980.

The first half of this puzzle is complete! It provides one gold star: *
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from utils.read_file import read_file
from utils.test_solution import test_solution


@test_solution(name="DAY 01 PART 1", runs=100)
def main():
    print("\n### DAY 01 PART 1 ###")

    content = read_file(os.path.join(os.path.dirname(__file__), "input.txt"))
    if not content:
        return

    movements = content.split()
    position = 50
    count_zero = 0

    for move in movements:
        if move[0] == "L":
            position = (position - int(move[1:])) % 100
        else:
            position = (position + int(move[1:])) % 100

        if position == 0:
            count_zero += 1

    print(f"\n# SOLUTION: the actual password to open the door is: {count_zero}\n")


if __name__ == "__main__":
    main()
