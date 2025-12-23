"""
Your puzzle answer was ____.

Both parts of this puzzle are complete! They provide two gold stars: **
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from utils.read_file import read_file
from utils.test_solution import test_solution


@test_solution(name="DAY 09 PART 2", runs=100)
def main():
    print("\n### DAY 09 PART 2 ###")

    content = read_file(os.path.join(os.path.dirname(__file__), "input.txt"))
    if not content:
        return

    couples = [[*map(int, line.split(","))] for line in content.strip().split("\n")]
    vertical_lines = []
    horizontal_lines = []

    prev_x, prev_y = couples[-1]
    for x, y in couples:
        if x == prev_x:
            if y > prev_y:
                horizontal_lines.append((prev_x, prev_y, x, y))
            else:
                horizontal_lines.append((x, y, prev_x, prev_y))
        else:
            if x > prev_x:
                vertical_lines.append((prev_x, prev_y, x, y))
            else:
                vertical_lines.append((x, y, prev_x, prev_y))

        prev_x, prev_y = x, y

    area_groups = []
    for i, [x1, y1] in enumerate(couples):
        for [x2, y2] in couples[i + 1 :]:
            if y1 > y2:
                y_min, y_max = y2, y1
            else:
                y_min, y_max = y1, y2

            if x1 > x2:
                x_min, x_max = x2, x1
            else:
                x_min, x_max = x1, x2

            area_groups.append(
                (
                    (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1),
                    (x_min, y_min),
                    (x_max, y_max),
                )
            )

    area_groups = sorted(area_groups, reverse=True)

    max_area = 0
    for area, p1, p2 in area_groups[:]:
        has_error = False
        for line in horizontal_lines:
            if line[0] <= p1[0] or line[0] >= p2[0]:
                continue
            elif line[1] < p1[1] and line[3] <= p1[1]:
                continue
            elif line[1] >= p2[1]:
                continue

            has_error = True
            break

        if has_error:
            continue

        for line in vertical_lines:

            if line[1] <= p1[1] or line[1] >= p2[1]:
                continue
            elif line[0] < p1[0] and line[2] <= p1[0]:
                continue
            elif line[0] >= p2[0]:
                continue

            has_error = True
            break

        if not has_error:
            max_area = area
            print("Found: ", area, p1, p2)
            break

    print(f"\n# SOLUTION: the largest area of any rectangle you can make using only red and green tiles is: {max_area}\n")


if __name__ == "__main__":
    main()
