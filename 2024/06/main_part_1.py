
'''
Your puzzle answer was 5242.

The first half of this puzzle is complete! It provides one gold star: *
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file
from utils.enum import SmartEnum
from utils.test_solution import test_solution


class Direction(SmartEnum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

class Tile(SmartEnum):
    EMPTY = '.'
    OBSTACLE = '#'
    VISITED = 'X'

@test_solution(name="DAY 06 PART 1", runs=100)
def main():
    print("\n### DAY 06 PART 1 ###")

    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt"))
    if not content: return

    labMap = [[char for char in line] for line in content.split("\n")]
    maxRow, maxCol = len(labMap), len(labMap[0])
    guardPosition = [[i, line.index('^')] for i, line in enumerate(labMap) if line.count('^') == 1][0]
    guardDirection = Direction.UP

    distinctPositions = 0
    isFinished = False
    while not isFinished:
        gRow, gCol = guardPosition

        if Direction.UP == guardDirection:
            for row in range(gRow, -1, -1):
                tile = labMap[row][gCol]
                if Tile.OBSTACLE == tile:
                    guardPosition = [row + 1, gCol]
                    guardDirection = Direction.RIGHT
                    break
                elif Tile.VISITED != tile:
                    labMap[row][gCol] = Tile.VISITED()
                    distinctPositions += 1
            else:
                isFinished = True
            
        elif Direction.RIGHT == guardDirection:
            for col in range(gCol, maxCol):
                tile = labMap[gRow][col]
                if Tile.OBSTACLE == tile:
                    guardPosition = [gRow, col - 1]
                    guardDirection = Direction.DOWN
                    break
                elif Tile.EMPTY == tile:
                    labMap[gRow][col] = Tile.VISITED()
                    distinctPositions += 1
            else:
                isFinished = True
            
        elif Direction.DOWN == guardDirection:
            for row in range(gRow, maxRow):
                tile = labMap[row][gCol]
                if Tile.OBSTACLE == tile:
                    guardPosition = [row - 1, gCol]
                    guardDirection = Direction.LEFT
                    break
                elif Tile.EMPTY == tile:
                    labMap[row][gCol] = Tile.VISITED()
                    distinctPositions += 1
            else:
                isFinished = True

        else: # direction.LEFT == guardDirection:
            for col in range(gCol, -1, -1):
                tile = labMap[gRow][col]
                if Tile.OBSTACLE == tile:
                    guardPosition = [gRow, col + 1]
                    guardDirection = Direction.UP
                    break
                elif Tile.EMPTY == tile:
                    labMap[gRow][col] = Tile.VISITED()
                    distinctPositions += 1
            else:
                isFinished = True

    print("\nGuard Path:")
    for line in labMap:
        print("".join(line))
    
    print(f"\n# SOLUTION: distinct positions visited: {distinctPositions}\n")

if __name__ == "__main__":
    main()