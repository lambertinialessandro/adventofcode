
'''
Your puzzle answer was 99448.

The first half of this puzzle is complete! It provides one gold star: *
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file
from utils.enum import SmartEnum
from utils.test_solution import test_solution

import heapq

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

#@test_solution(name="DAY 16 PART 1", runs=10)
def main():
    print("\n### DAY 16 PART 1 ###")

    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt"))
    if not content: return
    possible_directions = {direction: [d for d in Direction if d != (direction - 2)] for direction in Direction}
    moves = {Direction.NORTH: [-1, 0], Direction.EST: [0, 1], Direction.SOUTH: [1, 0], Direction.WEST: [0, -1]}

    env = [[*line] for line in content.split("\n")]
    sr = sc = er = ec = -1
    for i, line in enumerate(env):
        if "S" in line:
            sr, sc = i, line.index("S")
        if "E" in line:
            er, ec = i, line.index("E")
        if sr != -1 and er != -1:
            break

    score = -1
    visited = {}
    opened = [tuple([0, sr, sc, Direction.EST])]
    heapq.heapify(opened)
    while True:
        if len(opened) == 0:
            break

        [cost, pr, pc, pd] = heapq.heappop(opened)
        visited[tuple([pr, pc])] = cost
        if pr == er and pc == ec:
            score = cost
            break

        for direction in possible_directions[pd]:
            [dr, dc] = moves[direction]
            npr, npc = pr + dr, pc + dc

            if env[npr][npc] != Tile.WALL():
                n_cost = cost + 1 + 1000 * min(1, abs(pd() - direction()))
                if tuple([npr, npc]) not in visited or visited[tuple([npr, npc])] > n_cost:
                    heapq.heappush(opened, tuple([n_cost, npr, npc, direction]))

    zero_env = [[0] * len(line) for line in env]

    for i, line in enumerate(env):
        for j, char in enumerate(line):
            if char == "#":
                zero_env[i][j] = -1

    for k, v in visited.items():
        [r, c] = k

        if zero_env[r][c] == 0:
            zero_env[r][c] = v
        else:
            zero_env[r][c] = min(zero_env[r][c], v)
    
    import matplotlib.pyplot as plt
    import numpy as np
    zero_env_array = np.array(zero_env)

    plt.imshow(zero_env_array, cmap='viridis', origin='upper', interpolation='none')
    plt.colorbar(label='Value')
    plt.title('Heatmap of Zero Environment')

    plt.scatter(sc, sr, color='red', s=100, edgecolors='black', label='Start (S)')
    plt.scatter(ec, er, color='red', s=100, edgecolors='black', label='End (E)')

    plt.xticks([])
    plt.yticks([])
    plt.show()
    
    print(f"\n# SOLUTION: __: {score}\n")

if __name__ == "__main__":
    main()