
'''
Your puzzle answer was 559667.

The first half of this puzzle is complete! It provides one gold star: *
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file
from utils.test_solution import test_solution

@test_solution(name="DAY 03 PART 1", runs=100)
def main():
    print("\n### DAY 03 PART 1 ###")

    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt"))
    if not content: return

    content = content.split("\n")

    sum_adjacent = 0
    for i, line in enumerate(content):
        j = 0
        while j < len(line):
            char = line[j]
            if char.isdigit():
                k = 0
                while j+k < len(line) and line[j+k].isdigit():
                    k += 1
                
                has_simbol_adj = False
                if i > 0:
                    for w in range(j-1, j+k+1):
                        if has_simbol_adj:
                            break

                        if w < 0 or w >= len(content[i-1]):
                            continue

                        if not content[i-1][w].isdigit() and content[i-1][w] != ".":
                            has_simbol_adj = True
                    
                if i < len(content) - 1:
                    for w in range(j-1, j+k+1):
                        if has_simbol_adj:
                            break

                        if w < 0 or w >= len(content[i+1]):
                            continue

                        if not content[i+1][w].isdigit() and content[i+1][w] != ".":
                            has_simbol_adj = True
                
                if not has_simbol_adj and j > 0:
                    if not content[i][j-1].isdigit() and content[i][j-1] != ".":
                        has_simbol_adj = True
                
                if not has_simbol_adj and j + k < len(line):
                    if not content[i][j+k].isdigit() and content[i][j+k] != ".":
                        has_simbol_adj = True

                if has_simbol_adj:
                    sum_adjacent += int(line[j:j+k])
                    print(f"Found adjacent: {line[j:j+k]}")
                    j += k
            j += 1
                



    print(f"\n# SOLUTION: sum of all of the part numbers in the engine schematic: {sum_adjacent}\n")

if __name__ == "__main__":
    main()
