
'''
Your puzzle answer was 217443.

The first half of this puzzle is complete! It provides one gold star: *
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file
from utils.test_solution import test_solution

@test_solution(name="DAY 11 PART 1", runs=100)
def main():
    print("\n### DAY 11 PART 1 ###")

    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt"))
    if not content: return

    stones = [*map(int, content.strip().split(" "))]
    countStones = 0
    print(f"stones: {stones}")

    for stone in stones:
        opened = [[stone, 0]]
        while len(opened) > 0:
            [currStone, idx] = opened.pop()
            for i in range(idx, 25):
                strStone = str(currStone)
                lenStrStone = len(strStone)
                if currStone == 0:
                    currStone = 1
                elif lenStrStone % 2 == 0:
                    currStone = int(strStone[:lenStrStone//2])
                    opened.append([int(strStone[lenStrStone//2:]), i+1])
                else:
                    currStone *= 2024
            countStones += 1
    
    print(f"\n# SOLUTION: number of stones after 25 blinks: {countStones}\n")

if __name__ == "__main__":
    main()