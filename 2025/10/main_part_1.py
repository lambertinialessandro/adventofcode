"""
Your puzzle answer was 530.

The first half of this puzzle is complete! It provides one gold star: *
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from utils.read_file import read_file
from utils.test_solution import test_solution

import re


def explore_solution(lights, buttons, prev_comb, pos, depth):
    for i, comb in enumerate(buttons[pos + 1 :]):

        if depth > 1:
            if explore_solution(
                lights, buttons, prev_comb ^ comb, pos + i + 1, depth - 1
            ):
                return True
        else:
            if prev_comb ^ comb == lights:
                return True

    return False


@test_solution(name="DAY 10 PART 1", runs=100)
def main():
    print("\n### DAY 10 PART 1 ###")

    content = read_file(os.path.join(os.path.dirname(__file__), "input.txt"))
    if not content:
        return

    pattern = re.compile(r"\[(?P<lights>.*?)\]|\((?P<buttons>.*?)\)")
    button_presses = 0

    for line in content.strip().split("\n")[:]:
        matches = pattern.finditer(line)
        buttons = []
        l_size = 0

        for m in matches:
            if m.group("lights"):
                lights = m.group("lights").replace(".", "0").replace("#", "1")
                l_size = len(lights)
            elif m.group("buttons"):
                code = ""
                for i in range(l_size):
                    code += "1" if str(i) in m.group("buttons") else "0"
                buttons.append(int(code, 2))

        lights = int(lights, 2)

        size = 1
        found = False
        while size < 8 and not found:
            for i, comb in enumerate(buttons):

                if size > 1:
                    found = explore_solution(lights, buttons, comb, i, size - 1)
                else:
                    found = comb == lights

                if found:
                    button_presses += size
                    break
            size += 1

    print(
        f"\n# SOLUTION: the fewest button presses required to correctly configure the indicator lights is: {button_presses}\n"
    )


if __name__ == "__main__":
    main()
