"""
Your puzzle answer was 17087.

The first half of this puzzle is complete! It provides one gold star: *
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from utils.read_file import read_file
from utils.test_solution import test_solution


@test_solution(name="DAY 03 PART 1", runs=1000)
def main():
    print("\n### DAY 03 PART 1 ###")

    content = read_file(os.path.join(os.path.dirname(__file__), "input.txt"))
    if not content:
        return

    total_joltage = 0
    c = 0

    banks = content.strip().split("\n")
    for bank in banks:
        print(f"\nBank: {bank}")
        left = "0"
        right = "0"

        size = len(bank)
        #for i in range(size-1):
        for i in range(size-2, -1, -1):
            l = bank[i]
            
            #if l <= left: continue
            if l < left: continue

            right = "0"
            for j in range(i + 1, size):
                r = bank[j]

                if r >= right:
                    left = l
                    right = r

        print(f"L: {left} + R: {right}")
        total_joltage += int(left + right)

    print(f"\n# SOLUTION: the total output joltage is: {total_joltage}\n")


if __name__ == "__main__":
    main()
