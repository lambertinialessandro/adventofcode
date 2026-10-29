"""
Your puzzle answer was 975376.

Both parts of this puzzle are complete! They provide two gold stars: **
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from utils.read_file import read_file
from utils.enum import SmartEnum
from utils.test_solution import test_solution

import heapq
from collections import defaultdict


class Tile(SmartEnum):
    EMPTY = "."
    WALL = "#"
    START = "S"
    END = "E"


class Direction(SmartEnum):
    NORTH = 0
    EST = 1
    SOUTH = 2
    WEST = 3


threshold = 100
cheat_dist = 20
possible_directions = {direction: [d for d in Direction if d != (direction - 2)] for direction in Direction}
moves = {Direction.NORTH: [-1, 0], Direction.EST: [0, 1], Direction.SOUTH: [1, 0], Direction.WEST: [0, -1]}

@test_solution(name="DAY 20 PART 2", runs=10)
def main():
    print("\n### DAY 20 PART 2 ###")

    content = read_file(os.path.join(os.path.dirname(__file__), "input.txt"))
    if not content:
        return

    env = [[*line] for line in content.strip().split("\n")]
    sr = sc = er = ec = -1
    for i, line in enumerate(env):
        if "S" in line:
            sr, sc = i, line.index("S")
        if "E" in line:
            er, ec = i, line.index("E")
        if sr != -1 and er != -1:
            break

    visited = {}
    opened = [(0, sr, sc, Direction.EST)]
    heapq.heapify(opened)
    while len(opened) != 0:
        [cost, pr, pc, pd] = heapq.heappop(opened)
        visited[(pr, pc)] = cost
        
        if pr == er and pc == ec:
            continue

        for direction in possible_directions[pd]:
            [dr, dc] = moves[direction]
            npr, npc = pr + dr, pc + dc

            if env[npr][npc] != Tile.WALL():
                n_cost = cost + 1
                if (npr, npc) not in visited:
                    heapq.heappush(opened, (n_cost, npr, npc, direction))


    total_valid_cheats = 0
    path_cells = list(visited.keys())
    for i in range(len(path_cells)):
        pr, pc = path_cells[i]
        pd = visited[(pr, pc)]
        
        for dr in range(-cheat_dist, cheat_dist + 1):
            for dc in range(-cheat_dist, cheat_dist + 1):
                distance = abs(dr) + abs(dc)
                
                if 2 <= distance <= cheat_dist:
                    npr, npc = pr + dr, pc + dc
                    
                    if (npr, npc) in visited:
                        dest_dist = visited[(npr, npc)]
                        
                        if dest_dist > pd:
                            skipped_cost = dest_dist - pd - distance
                            if skipped_cost >= threshold:
                                total_valid_cheats += 1
    
    print(f"\n# SOLUTION: number of cheats that save at least {threshold} picoseconds: {total_valid_cheats}")


if __name__ == "__main__":
    main()
