
'''
Your puzzle answer was 16,46.

Both parts of this puzzle are complete! They provide two gold stars: **
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

@test_solution(name="DAY 18 PART 2", runs=10)
def main():
    print("\n### DAY 18 PART 2 ###")

    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt")).strip()
    if not content: return
    
    dim_r, dim_c = 71, 71 # 71, 71 # 7, 7
    er, ec = dim_r - 1, dim_c - 1
    moves = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    walls = [[*map(int, line.split(","))] for line in content.split("\n")]
    env = [[Tile.EMPTY() for _ in range(dim_r)] for _ in range(dim_c)]

    for [c, r] in walls[:1024]:
        env[r][c] = Tile.WALL()

    new_tile_pos = 1023
    while(True):
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
                    n_cost = h + 10 * math.sqrt((er-npr)**2 + (ec-npc)**2)
                    heapq.heappush(opened, tuple([n_cost, h+1, npr, npc]))
    
        if score == -1:
            break
        
        new_tile_pos += 1
        [c, r] = walls[new_tile_pos]
        env[r][c] = Tile.WALL()
        # TODO: evaluate the path only if the obstacle is in the current path
        # TODO: evaluate the path only from that position

    coordinates = f"{walls[new_tile_pos][0]},{walls[new_tile_pos][1]}"
    
    print(f"\n# SOLUTION: coordinates of the first byte that will prevent the exit: {coordinates}\n")

if __name__ == "__main__":
    main()