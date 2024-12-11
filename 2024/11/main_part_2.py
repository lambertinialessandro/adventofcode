
'''
Your puzzle answer was 257246536026785.

Both parts of this puzzle are complete! They provide two gold stars: **
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file
from utils.test_solution import test_solution

def solveRecursive(stepFound, stone, blinks):
    if (stone, blinks) in stepFound.keys():
        return stepFound[stone, blinks]
    if blinks == 0:
        stepFound[stone, blinks] = 1
        return 1
    
    strStone = str(stone)
    lenStrStone = len(strStone)
    if stone == 0:
        totSolutions = solveRecursive(stepFound, stone + 1, blinks - 1)
        stepFound[stone, blinks] = totSolutions
    elif lenStrStone % 2 == 0:
        totSolutions1 = solveRecursive(stepFound, int(strStone[:lenStrStone//2]), blinks - 1)
        totSolutions2 = solveRecursive(stepFound, int(strStone[lenStrStone//2:]), blinks - 1)

        totSolutions = totSolutions1 + totSolutions2
        stepFound[stone, blinks] = totSolutions
    else:
        totSolutions = solveRecursive(stepFound, stone * 2024, blinks - 1)
        stepFound[stone, blinks] = totSolutions
    return totSolutions
    


@test_solution(name=f"DAY 11 PART 2", runs=100)
def main():
    print("\n### DAY 11 PART 2 ###")

    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt"))
    if not content: return

    stones = [*map(int, content.strip().split(" "))]
    countStones = 0
    print(f"stones: {stones}")

    stepFound = {}
    blink = 75

    for stone in stones:
        countStones += solveRecursive(stepFound, stone, blink)

    #print(res)
    
    print(f"\n# SOLUTION: number of stones after 75 blinks: {countStones}\n")

if __name__ == "__main__":
    main()