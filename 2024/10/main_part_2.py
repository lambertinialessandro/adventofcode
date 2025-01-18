
'''
Your puzzle answer was 1380.

Both parts of this puzzle are complete! They provide two gold stars: **
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file
from utils.test_solution import test_solution

@test_solution(name="DAY 10 PART 2", runs=100)
def main():
    print("\n### DAY 10 PART 2 ###")
    
    actions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt")).strip()
    if not content: return

    env = [[*line] for line in content.split("\n")]
    nr, nc = len(env), len(env[0])

    startPos = [[r, c] for r, line in enumerate(env) for c, v in enumerate(line) if v == "0"]

    trailheads = []
    for pos in startPos:
        endPos = []
        opened = [[pos, 0]]
        while opened:
            [[r, c], val] = opened.pop()

            if val == 9:
                endPos.append(tuple([r, c]))

            for [ar, ac] in actions:
                nextR, nextC = r + ar, c + ac
                if nextR >= 0 and nextR < nr and nextC >= 0 and nextC < nc:
                    nextVal = int(env[nextR][nextC])
                    if val + 1 == nextVal:
                        opened.append([[nextR, nextC], nextVal])
            
        trailheads.extend(endPos)
    
    print(f"\n# SOLUTION: sum of the ratings of all trailheads: {len(trailheads)}\n")

if __name__ == "__main__":
    main()