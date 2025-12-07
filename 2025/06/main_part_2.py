"""
Your puzzle answer was 10951882745757.

Both parts of this puzzle are complete! They provide two gold stars: **
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from utils.read_file import read_file
from utils.test_solution import test_solution

from math import prod


def calc_value(num_group, sym):
    if sym == "+":
        val = sum(num_group)
    else:
        val = prod(num_group)
    print(num_group, sym, val)
    return val


@test_solution(name="DAY 06 PART 2", runs=100)
def main():
    print("\n### DAY 06 PART 2 ###")

    content = read_file(os.path.join(os.path.dirname(__file__), "input.txt"))
    if not content:
        return

    total_sum = 0
    lines = content.strip().split("\n")
    numbers = lines[:-1]
    symbols = iter(lines[-1].split())

    num_group = []
    for col in zip(*numbers):
        str_num = "".join(col).strip()

        if not str_num:
            total_sum += calc_value(num_group, next(symbols))
            num_group = []
        else:
            num_group.append(int(str_num))
    if num_group:
        total_sum += calc_value(num_group, next(symbols))

    print(
        f"\n# SOLUTION: the grand total found by adding together all of the answers is: {total_sum}\n"
    )


if __name__ == "__main__":
    main()
