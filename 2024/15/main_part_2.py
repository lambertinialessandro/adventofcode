
'''
Your puzzle answer was 1471826.

Both parts of this puzzle are complete! They provide two gold stars: **
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
    BOX1 = "["
    BOX2 = "]"
    ROBOT = "@"

def check_box_moved_h(env, pr, pc, dc):
    npc = pc
    while True:
        npc = npc + dc
        if env[pr][npc] == Tile.WALL():
            return [False, 0]
        if env[pr][npc] == Tile.EMPTY():
            return [True, npc]

def check_box_moved_v(env, pr, pc, dr, tile):
    cpr, cpc = pr, pc
    if tile == Tile.BOX2():
        cpc = cpc - 1
    
    if env[cpr+dr][cpc] == Tile.WALL() or env[cpr+dr][cpc+1] == Tile.WALL():
        return False
    if env[cpr+dr][cpc] == Tile.EMPTY() and env[cpr+dr][cpc+1] == Tile.EMPTY():
        return True
    
    if env[cpr+dr][cpc] == Tile.BOX1():
        return check_box_moved_v(env, cpr+dr, cpc, dr, Tile.BOX1())
    
    left_check = True
    if env[cpr+dr][cpc] == Tile.BOX2():
        left_check = check_box_moved_v(env, cpr+dr, cpc, dr, Tile.BOX2())

    right_check = True
    if env[cpr+dr][cpc+1] == Tile.BOX1():
        right_check = check_box_moved_v(env, cpr+dr, cpc+1, dr, Tile.BOX1())
    
    return left_check and right_check
    
def move_box_v(env, pr, pc, dr, tile):
    cpr, cpc = pr, pc
    if tile == Tile.BOX2():
        cpc = cpc - 1
    
    if env[cpr+dr][cpc] == Tile.BOX1():
        move_box_v(env, cpr+dr, cpc, dr, Tile.BOX1())
    elif env[cpr+dr][cpc] == Tile.BOX2():
        move_box_v(env, cpr+dr, cpc, dr, Tile.BOX2())
    if env[cpr+dr][cpc+1] == Tile.BOX1():
        move_box_v(env, cpr+dr, cpc+1, dr, Tile.BOX1())
    
    env[cpr+dr][cpc] = Tile.BOX1()
    env[cpr+dr][cpc+1] = Tile.BOX2()
    env[cpr][cpc] = Tile.EMPTY()
    env[cpr][cpc+1] = Tile.EMPTY()
    

    

            

@test_solution(name="DAY 15 PART 2", runs=100)
def main():
    print("\n### DAY 15 PART 2 ###")

    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt"))
    if not content: return

    moves = {"^": [-1, 0], ">": [0, 1], "v": [1, 0], "<": [0, -1]}

    [env_str, actions] = content.split("\n\n")
    env = []
    for line_str in env_str.split("\n"):
        line = []
        for char in line_str:
            if char == Tile.BOX():
                line.append(Tile.BOX1())
                line.append(Tile.BOX2())
            elif char == Tile.EMPTY():
                line.append(Tile.EMPTY())
                line.append(Tile.EMPTY())
            elif char == Tile.WALL():
                line.append(Tile.WALL())
                line.append(Tile.WALL())
            elif char == Tile.ROBOT():
                line.append(Tile.ROBOT())
                line.append(Tile.EMPTY())
        env.append(line)
    actions = actions.replace("\n", "")

    for line in env:
        print("".join(line))

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
            """ if n_tile == Tile.BOX():

                [can_be_moved, pbr, pbc] = check_box_moved(env, pr, pc, dr, dc)
                if can_be_moved:
                    env[pbr][pbc] = Tile.BOX()
                    env[pr][pc] = Tile.EMPTY()
                    env[npr][npc] = Tile.ROBOT()
                    pr, pc = npr, npc """
            
            if n_tile == Tile.BOX1() or n_tile == Tile.BOX2():
                if dr == 0:
                    [can_be_moved, pbc] = check_box_moved_h(env, npr, npc, dc)
                    if can_be_moved:
                        if dc > 0:
                            first_box = Tile.BOX1()
                            second_box = Tile.BOX2()
                        else:
                            first_box = Tile.BOX2()
                            second_box = Tile.BOX1()
                        for i in range(pbc-dc, npc, -dc*2):
                            env[npr][i] = first_box
                            env[npr][i+dc] = second_box
                        pc = npc
                        env[npr][npc-dc] = Tile.EMPTY()
                        env[npr][npc] = Tile.ROBOT()
                else:
                    if check_box_moved_v(env, npr, npc, dr, n_tile):
                        move_box_v(env, npr, npc, dr, n_tile)
                        env[pr][pc] = Tile.EMPTY()
                        env[npr][npc] = Tile.ROBOT()
                        pr, pc = npr, npc

    for line in env:
        print("".join(line))

    sum_gps_coordinates = 0
    for i, line in enumerate(env, 0):
        for j, char in enumerate(line, 0):
            if char == Tile.BOX1():
                sum_gps_coordinates += i * 100 + j
    
    
    print(f"\n# SOLUTION: sum of all boxes' GPS coordinates: {sum_gps_coordinates}\n")

if __name__ == "__main__":
    main()