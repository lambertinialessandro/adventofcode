
'''
Your puzzle answer was 310.

The first half of this puzzle is complete! It provides one gold star: *
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file
from utils.enum import SmartEnum
from utils.test_solution import test_solution

import heapq
import math

class Tile(SmartEnum):
    EMPTY = "."
    WALL = "#"

@test_solution(name="DAY 18 PART 1", runs=100)
def main():
    print("\n### DAY 18 PART 1 ###")

    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt"))
    if not content: return
    
    dim_r, dim_c = 71, 71 # 71, 71 # 7, 7
    er, ec = dim_r - 1, dim_c - 1
    moves = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    walls = [[*map(int, line.split(","))] for line in content.split("\n")][:1024]
    env = [[Tile.EMPTY() for _ in range(dim_r)] for _ in range(dim_c)]

    for [c, r] in walls:
        env[r][c] = Tile.WALL()

    score = -1
    visited = {}
    opened = [tuple([0, 0, 0, 0])]
    heapq.heapify(opened)
    while True:
        if len(opened) == 0:
            break

        [cost, h, pr, pc] = heapq.heappop(opened)
        if tuple([pr, pc]) in visited: continue
        visited[tuple([pr, pc])] = cost
        if pr == er and pc == ec:
            score = h
            break

        for move in moves:
            [dr, dc] = move
            npr, npc = pr + dr, pc + dc

            if 0 <= npr < dim_r and 0 <= npc < dim_c and env[npr][npc] != Tile.WALL() and tuple([npr, npc]) not in visited:
                n_cost = h + 1 * math.sqrt((er-npr)**2 + (ec-npc)**2)
                heapq.heappush(opened, tuple([n_cost, h+1, npr, npc]))
    
    print(f"\n# SOLUTION: __: {score}\n")
    print(f"\n# SOLUTION: minimum number of steps: {score}\n")

if __name__ == "__main__":
    main()