
'''
Your puzzle answer was 498.

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
    START = "S"
    END = "E"

class Direction(SmartEnum):
    NORTH = 0
    EST = 1
    SOUTH = 2
    WEST = 3

def find_seats(visited, predecessors, er, ec, score):
    seats = set()
    stack = [(er, ec, d) for d in Direction if visited.get((er, ec, d)) == score]
    seen_states = set(stack)

    while stack:
        r, c, d = stack.pop()
        seats.add((r, c))
        for pr, pc, pd in predecessors.get((r, c, d), set()):
            if (pr, pc, pd) not in seen_states:
                seen_states.add((pr, pc, pd))
                stack.append((pr, pc, pd))

    return seats

@test_solution(name="DAY 16 PART 2", runs=10)
def main():
    print("\n### DAY 16 PART 2 ###")
    
    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt"))
    if not content: return
    
    possible_directions = {direction: [d for d in Direction if d != (direction - 2)] for direction in Direction}
    moves = {Direction.NORTH: [-1, 0], Direction.EST: [0, 1], Direction.SOUTH: [1, 0], Direction.WEST: [0, -1]}

    env = [[*line] for line in content.split("\n")]
    sr = sc = er = ec = -1
    for i, line in enumerate(env):
        if sr == -1 and Tile.START() in line:
            sr, sc = i, line.index(Tile.START())
        if er == -1 and Tile.END() in line:
            er, ec = i, line.index(Tile.END())
        if sr != -1 and er != -1:
            break

    score = math.inf
    visited = {}
    opened = [(0, sr, sc, Direction.EST)]
    predecessors = {}
    heapq.heapify(opened)
    while opened:
        [cost, pr, pc, pd] = heapq.heappop(opened)
        if cost > score:
            break

        if pr == er and pc == ec:
            score = cost
            break
    
        for direction in possible_directions[pd]:
            [dr, dc] = moves[direction]
            npr, npc, npd = pr + dr, pc + dc, direction

            if env[npr][npc] != Tile.WALL():
                n_cost = cost + 1 + 1000 * (pd != npd)
                
                current_best = visited.get((npr, npc, npd), math.inf)
                if n_cost > current_best:
                    continue
                if n_cost < current_best:
                    visited[(npr, npc, npd)] = n_cost
                    predecessors[(npr, npc, npd)] = set()
                predecessors[(npr, npc, npd)].add((pr, pc, pd))
                heapq.heappush(opened, (n_cost, npr, npc, npd))

    seats = find_seats(visited, predecessors, er, ec, score)
    
    print(f"visited: {len(visited)}")
    print(f"\n# SOLUTION: __: {len(seats)}\n")
    
    if False:
        max_len = max(len(line) for line in env)
        zero_env_1 = [[0] * max_len for _ in env]
        zero_env_2 = [[0] * max_len for _ in env]

        # fill walls
        for i, line in enumerate(env):
            for j, char in enumerate(line):
                if char == "#":
                    zero_env_1[i][j] = -1
                    zero_env_2[i][j] = -1
        
        for [r, c] in seats:
            if zero_env_1[r][c] == 0:
                zero_env_1[r][c] = 1
        
        for k, v in visited.items():
            [r, c, _] = k

            if zero_env_2[r][c] == 0:
                zero_env_2[r][c] = v
            else:
                zero_env_2[r][c] = min(zero_env_2[r][c], v)
        
        import matplotlib.pyplot as plt
        import numpy as np

        zero_env_array_1 = np.array(zero_env_1)
        plt.figure(figsize=(8, 6))
        plt.imshow(zero_env_array_1, cmap='viridis', origin='upper', interpolation='none')
        plt.colorbar(label='Value')
        plt.title('Heatmap of Zero Environment')
        plt.scatter(sc, sr, color='red', s=100, edgecolors='black', label='Start (S)')
        plt.scatter(ec, er, color='red', s=100, edgecolors='black', label='End (E)')
        
        zero_env_array_2 = np.array(zero_env_2)
        plt.figure(figsize=(8, 6))
        plt.imshow(zero_env_array_2, cmap='viridis', origin='upper', interpolation='none')
        plt.colorbar(label='Value')
        plt.title('Heatmap of Non-Zero Environment')
        plt.scatter(sc, sr, color='red', s=100, edgecolors='black', label='Start (S)')
        plt.scatter(ec, er, color='red', s=100, edgecolors='black', label='End (E)')
        
        plt.show()
        
        

if __name__ == "__main__":
    main()