"""
Your puzzle answer was 567.

The first half of this puzzle is complete! It provides one gold star: *
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from utils.read_file import read_file
from utils.test_solution import test_solution

import re


@test_solution(name="DAY 12 PART 1", runs=100)
def main():
    print("\n### DAY 12 PART 1 ###")

    content = read_file(os.path.join(os.path.dirname(__file__), "input.txt"))
    if not content:
        return

    blocks = content.split("\n\n")

    figures = []
    for block in blocks[:-1]:
        match = re.match(r"\d+:\n([.#]+)\n([.#]+)\n([.#]+)", block)
        figures.append((match.group(1) + match.group(2) + match.group(3)).count("#"))

    regions = []
    for line in blocks[-1].split("\n"):
        match = re.match(r"(\d+)x(\d+):\s([\s\d]+)", line)
        if match:
            regions.append(
                [int(match.group(1)) * int(match.group(2)), match.group(3).split(" ")]
            )

    possible_fits = 0
    for region in regions:
        count_size = 0
        count_occ = 0
        for piece, figure in zip(map(int, region[1]), figures):
            count_size += piece * 9
            count_occ += piece * figure

        if count_size <= region[0] or count_size - count_occ <= 9:
            possible_fits += 1

    print(f"\n# SOLUTION: the regions that can fit all of the presents are: {possible_fits}\n")


if __name__ == "__main__":
    main()
