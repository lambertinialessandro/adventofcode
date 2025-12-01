"""
Your puzzle answer was 5961.

Both parts of this puzzle are complete! They provide two gold stars: **
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from utils.read_file import read_file
from utils.test_solution import test_solution


@test_solution(name="DAY 01 PART 2", runs=100)
def main():
    print("\n### DAY 01 PART 2 ###")

    content = read_file(os.path.join(os.path.dirname(__file__), "input.txt"))
    if not content:
        return

    movements = content.split()
    position = 50
    count_zero = 0

    for move in movements:
        if move[0] == "L":
            distance = position - int(move[1:])

            gap = distance if position != 0 else 100 - int(move[1:])
            if gap <= 0:
                gap = 100 - gap
        else:
            distance = position + int(move[1:])
            gap = distance

        position = distance % 100
        count_zero = count_zero + (gap // 100)

    print(f"\n# SOLUTION: the password to open the door is: {count_zero}\n")


if __name__ == "__main__":
    main()
