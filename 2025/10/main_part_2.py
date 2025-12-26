"""
Your puzzle answer was 20172.

Both parts of this puzzle are complete! They provide two gold stars: **
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from utils.read_file import read_file
from utils.test_solution import test_solution

import re
from scipy.optimize import linprog


@test_solution(name="DAY 10 PART 2", runs=100)
def main():
    print("\n### DAY 10 PART 2 ###")

    content = read_file(os.path.join(os.path.dirname(__file__), "input.txt"))
    if not content:
        return

    pattern = re.compile(
        r"\[(?P<lights>.*?)\]|\((?P<buttons>.*?)\)|\{(?P<joltage>.*?)\}"
    )

    button_presses = 0
    for line in content.strip().split("\n"):
        matches = pattern.finditer(line)
        buttons = []

        for m in matches:
            if m.group("lights"):
                pass
            elif m.group("buttons"):
                buttons.append([*map(int, m.group("buttons").split(","))])
            elif m.group("joltage"):
                joltage = [*map(int, m.group("joltage").split(","))]

        c = [1 for _ in range(len(buttons))]
        A = [
            [1 if i in button else 0 for button in buttons] for i in range(len(joltage))
        ]
        B = joltage
        bounds = (0, None)

        res = linprog(c, A_eq=A, b_eq=B, bounds=bounds, integrality=1)
        button_presses += int(res.fun)

    print(
        f"\n# SOLUTION: the fewest button presses required to correctly configure the joltage level counters is: {button_presses}\n"
    )


if __name__ == "__main__":
    main()
