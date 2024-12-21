
'''
Your puzzle answer was 1471826.

The first half of this puzzle is complete! It provides one gold star: *
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file
from utils.enum import SmartEnum
from utils.test_solution import test_solution

class Tile(SmartEnum):
    EMPTY = "."
    WALL = "#"
    BOX = "O"
    ROBOT = "@"

def check_box_moved(env, pr, pc, dr, dc):
    npr, npc = pr, pc
    while True:
        npr, npc = npr + dr, npc + dc
        if env[npr][npc] == Tile.WALL():
            return [False, 0, 0]
        if env[npr][npc] == Tile.EMPTY():
            return [True, npr, npc]

@test_solution(name="DAY 15 PART 1", runs=100)
def main():
    print("\n### DAY 15 PART 1 ###")

    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt"))
    if not content: return

    moves = {"^": [-1, 0], ">": [0, 1], "v": [1, 0], "<": [0, -1]}

    [env, actions] = content.split("\n\n")
    env = [[*line] for line in env.split("\n")]
    actions = actions.replace("\n", "")

    pr, pc = 0, 0
    for i, line in enumerate(env):
        for j, char in enumerate(line):
            if char == Tile.ROBOT():
                pr, pc = i, j
                break
    
    for action in actions:
        [dr, dc] = moves[action]
        npr, npc = pr + dr, pc + dc
        if env[npr][npc] != Tile.WALL(): #0 <= npr < nr and 0 <= npc < nc:
            n_tile = env[npr][npc]

            if n_tile == Tile.EMPTY():
                env[pr][pc] = Tile.EMPTY()
                env[npr][npc] = Tile.ROBOT()
                pr, pc = npr, npc
            if n_tile == Tile.BOX():

                [can_be_moved, pbr, pbc] = check_box_moved(env, pr, pc, dr, dc)
                if can_be_moved:
                    env[pbr][pbc] = Tile.BOX()
                    env[pr][pc] = Tile.EMPTY()
                    env[npr][npc] = Tile.ROBOT()
                    pr, pc = npr, npc

    sum_gps_coordinates = 0
    for i, line in enumerate(env, 0):
        for j, char in enumerate(line, 0):
            if char == Tile.BOX():
                sum_gps_coordinates += i * 100 + j
    
    
    print(f"\n# SOLUTION: __: {sum_gps_coordinates}\n")

if __name__ == "__main__":
    main()