"""
Your puzzle answer was 523.

The first half of this puzzle is complete! It provides one gold star: *
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from utils.read_file import read_file
from utils.test_solution import test_solution

from collections import defaultdict


@test_solution(name="DAY 11 PART 1", runs=100)
def main():
    print("\n### DAY 11 PART 1 ###")

    content = read_file(os.path.join(os.path.dirname(__file__), "input.txt"))
    if not content:
        return

    connections = defaultdict(list)
    for line in content.strip().split("\n"):
        device, outputs = line.split(": ")
        connections[device] = outputs.split(" ")

    queue = [[output, ["you"]] for output in connections["you"]]

    count_paths = 0
    while len(queue) > 0:
        device, path = queue.pop()

        if device == "out":
            count_paths += 1

        for output in connections[device]:
            queue.append([output, [*path, device]])

    print(f"\n# SOLUTION: number of different paths that lead from you to out: {count_paths}\n")


if __name__ == "__main__":
    main()
