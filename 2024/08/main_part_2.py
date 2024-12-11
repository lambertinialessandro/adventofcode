
'''
Your puzzle answer was 1064.

Both parts of this puzzle are complete! They provide two gold stars: **
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file
from utils.test_solution import test_solution

def isSolutionCorrect(solution, nr, nc):
    [r, c] = solution
    return r >= 0 and r < nr and c >= 0 and c < nc

@test_solution(name="DAY 08 PART 2", runs=100)
def main():
    print("\n### DAY 08 PART 2 ###")

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
                    newSolution = tuple(r1, min(c1, c2))
                    while isSolutionCorrect(newSolution, nr, nc):
                        solutions.add(newSolution)
                        newSolution = tuple(r1, newSolution[1] - dc)
                    newSolution = tuple(r1, max(c1, c2))
                    while isSolutionCorrect(newSolution, nr, nc):
                        solutions.add(newSolution)
                        newSolution = tuple(r1, newSolution[1] + dc)
                elif c1 == c2:
                    newSolution = tuple(min(r1, r2), c1)
                    while isSolutionCorrect(newSolution, nr, nc):
                        solutions.add(newSolution)
                        newSolution = tuple(newSolution[0] - dr, c1)
                    newSolution = tuple(min(r1, r2), c1)
                    while isSolutionCorrect(newSolution, nr, nc):
                        solutions.add(newSolution)
                        newSolution = tuple(newSolution[0] + dr, c1)
                else:
                    if r1 > r2:
                        r1, c1, r2, c2 = r2, c2, r1, c1
                    
                    if c1 < c2:
                        newSolution = tuple([r1, c1])
                        while isSolutionCorrect(newSolution, nr, nc):
                            solutions.add(newSolution)
                            newSolution = tuple([newSolution[0] - dr, newSolution[1] - dc])
                        newSolution = tuple([r2, c2])
                        while isSolutionCorrect(newSolution, nr, nc):
                            solutions.add(newSolution)
                            newSolution = tuple([newSolution[0] + dr, newSolution[1] + dc])
                    else:
                        newSolution = tuple([r1, c1])
                        while isSolutionCorrect(newSolution, nr, nc):
                            solutions.add(newSolution)
                            newSolution = tuple([newSolution[0] - dr, newSolution[1] + dc])
                        newSolution = tuple([r2, c2])
                        while isSolutionCorrect(newSolution, nr, nc):
                            solutions.add(newSolution)
                            newSolution = tuple([newSolution[0] + dr, newSolution[1] - dc])
        
        for [r, c] in solutions:
            if r >= 0 and r < nr and c >= 0 and c < nc:
                antinodes.add(tuple([r, c]))

    print("\nExample: ")

    print(chars)
    for char in chars:
        positions = [[r, c] for r, line in enumerate(env) for c, cell in enumerate(line) if cell == char]
        print(f"{char}: {positions}")

    #for [r, c] in antinodes: env[r][c] = "#"
    #for line in env: print(line)
    
    print(f"\n# SOLUTION: number of unique locations containing an antinode: {len(antinodes)} \n")

if __name__ == "__main__":
    main()