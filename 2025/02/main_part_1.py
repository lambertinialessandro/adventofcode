"""
Your puzzle answer was 8576933996.

The first half of this puzzle is complete! It provides one gold star: *
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from utils.read_file import read_file
from utils.test_solution import test_solution


@test_solution(name="DAY 02 PART 1", runs=100)
def main():
    print("\n### DAY 02 PART 1 ###")

    content = read_file(os.path.join(os.path.dirname(__file__), "input.txt"))
    if not content:
        return

    id_rangess = content.strip().split(",")
    print(f"number of ids: {len(id_rangess)}")
    sum_repeated = 0

    for id_range in id_rangess:
        start, end = [int(x) for x in id_range.split("-")]
        print("\nSTART", id_range, start, end)

        number = start
        while number <= end:
            number_s = str(number)
            size = len(number_s)
            
            # is 1-9
            if size == 1:
                number = 11
                continue

            # odd length
            if size % 2 != 0:
                number = 10 ** size
                continue

            # is 10-99
            if size == 2:
                if number_s[0] == number_s[1]:
                    print(f"repeated: {number}")
                    sum_repeated += number
                    number += 11
                else:
                    number += (11 - (number % 11))
            
            # even length
            else:
                size_2 = size // 2
                left = number_s[:size_2]
                right = number_s[size_2:]
                if left == right:
                    print(f"repeated: {number}")
                    sum_repeated += number
                    number += 10**size_2 + 1
                else:
                    next_number = int(left) - int(right)
                    if next_number > 0:
                        number += next_number
                    else:
                        next_number = 10**size_2 - int(right) + int(left) + 1
                        number += next_number
                
        print(f"\nEND number {number}")

    print(f"\n# SOLUTION: all the invalid IDs add up to: {sum_repeated}\n")


if __name__ == "__main__":
    main()
