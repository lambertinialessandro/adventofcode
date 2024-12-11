
'''
Your puzzle answer was 313.

The first half of this puzzle is complete! It provides one gold star: *
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file
from utils.test_solution import test_solution

@test_solution(name="DAY 08 PART 1", runs=100)
def main():
    print("\n### DAY 08 PART 1 ###")

    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt"))
    if not content: return

    env = [[*line] for line in content.split("\n")]
    nr, nc = len(env), len(env[0])
    chars = set(content)
    chars.remove("\n")
    chars.remove(".")


    antinodes = set()
    for char in chars:
        positions = [[r, c] for r, line in enumerate(env) for c, cell in enumerate(line) if cell == char]
        solutions = set()

        for i, pos1 in enumerate(positions):
            for j, pos2 in enumerate(positions):
                if i == j: continue

                [r1, c1] = pos1
                [r2, c2] = pos2

                dr, dc = abs(r1 - r2), abs(c1 - c2)

                if r1 == r2:
                    solutions.add(tuple(r1, min(c1, c2) - dc))
                    solutions.add(tuple(r1, max(c1, c2) + dc))
                elif c1 == c2:
                    solutions.add(tuple(min(r1, r2) - dr, c1))
                    solutions.add(tuple(min(r1, r2) + dr, c1))
                else:
                    if r1 > r2:
                        r1, c1, r2, c2 = r2, c2, r1, c1
                    
                    if c1 < c2:
                        solutions.add(tuple([r1 - dr, c1 - dc]))
                        solutions.add(tuple([r2 + dr, c2 + dc]))
                    else:
                        solutions.add(tuple([r1 - dr, c1 + dc]))
                        solutions.add(tuple([r2 + dr, c2 - dc]))
        
        for [r, c] in solutions:
            if r >= 0 and r < nr and c >= 0 and c < nc:
                antinodes.add(tuple([r, c]))

    print("\nExample: ")
    print(chars)
    for char in chars:
        positions = [[r, c] for r, line in enumerate(env) for c, cell in enumerate(line) if cell == char]
        print(f"{char}: {positions}")
    
    print(f"\n# SOLUTION: number of unique locations containing an antinode: {len(antinodes)} \n")

if __name__ == "__main__":
    main()