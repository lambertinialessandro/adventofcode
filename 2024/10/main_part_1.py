
'''
Your puzzle answer was 611.

The first half of this puzzle is complete! It provides one gold star: *
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file

def main():
    print("\n### DAY 10 PART 1 ###")

    actions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt"))
    if not content: return

    env = [[*line] for line in content.split("\n")]
    nr, nc = len(env), len(env[0])

    startPos = [[r, c] for r, line in enumerate(env) for c, v in enumerate(line) if v == "0"]

    trailheads = []
    for pos in startPos:
        # exploring
        endPos = set()
        opened = [[pos, 0]]
        while len(opened) > 0:
            [[r, c], val] = opened.pop(len(opened) - 1)

            if val == 9:
                endPos.add(tuple([r, c]))

            for [ar, ac] in actions:
                nextR, nextC = r + ar, c + ac
                if nextR >= 0 and nextR < nr and nextC >= 0 and nextC < nc:
                    nextVal = int(env[nextR][nextC])
                    if val + 1 == nextVal:
                        #if nextVal == 9:
                        #    endPos.add(tuple([r, c]))
                        #else:
                            opened.append([[nextR, nextC], nextVal])
            
            #print(opened)
        trailheads.extend(endPos)


    #print(f"startPos: {startPos}\n")
    #print(f"endPos: {endPos}\n")
    #print(f"trailheads: {trailheads}\n")

    #for line in env: print("".join(line))
    
    print(f"\n# SOLUTION: sum of the scores of all trailheads: {len(trailheads)}\n")

if __name__ == "__main__":
    main()