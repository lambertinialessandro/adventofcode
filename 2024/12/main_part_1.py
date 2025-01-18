
'''
Your puzzle answer was 1370100.

The first half of this puzzle is complete! It provides one gold star: *
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file
from utils.test_solution import test_solution

@test_solution(name="DAY 12 PART 1", runs=100)
def main():
    print("\n### DAY 12 PART 1 ###")

    neighbors = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt")).strip()
    if not content: return

    field = [[*line] for line in content.split("\n")]
    nr, nc = len(field), len(field[0])

    garden_plots = []
    visited = [["." for _ in range(nc) ] for _ in range(nr)]
    for r in range(nr):
        for c in range(nc):
            if visited[r][c] == ".":
                opened = [[r, c]]
                plant = field[r][c]
                garden_plots.append([0, 0])
                while opened:
                    [o_r, o_c] = opened.pop(0)
                    garden_plots[-1][0] += 1
                    visited[o_r][o_c] = "x"
                    for [dr, dc] in neighbors:
                        dr, dc = o_r + dr, o_c + dc
                        if 0 <= dr < nr and 0 <= dc < nc and field[dr][dc] == plant:
                            if visited[dr][dc] == ".":
                                visited[dr][dc] = "-"
                                opened.append([dr, dc])
                        else:
                            garden_plots[-1][1] += 1
    
    total_cost = sum([n * c for [n, c] in garden_plots])
    print(f"\n# SOLUTION: total price of fencing all regions: {total_cost}\n")

if __name__ == "__main__":
    main()