
'''
Your puzzle answer was 1900.

Both parts of this puzzle are complete! They provide two gold stars: **
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file
from utils.test_solution import test_solution

YELLOW = '\033[33m'
RESET = '\033[0m'

@test_solution(name="DAY 04 PART 2", runs=100)
def main():
    print("\n### DAY 04 PART 2 ###")

    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt")).strip()
    if not content: return

    text = content.split("\n")

    exampleText = [text[i][:3] for i in range(3)]
    print("\nExample:")
    print(f"Text:")
    for line in exampleText:
        print(f"\t{line}")
    print("MAS with X shape:")
    print(f'\t{YELLOW}{exampleText[0][0]}{RESET}{text[0][1]}{YELLOW}{text[0][2]}{RESET}')
    print(f'\t{text[1][0]}{YELLOW}{text[1][1]}{RESET}{text[1][2]}')
    print(f'\t{YELLOW}{text[2][0]}{RESET}{text[2][1]}{YELLOW}{text[2][2]}{RESET}')

    countWords = 0
    for r in range(len(text) - 2):
        for c in range(len(text) - 2):
            mas1 = text[r][c] + text[r+1][c+1] + text[r+2][c+2]
            mas2 = text[r][c+2] + text[r+1][c+1] + text[r+2][c]
            if (mas1 == "MAS" or mas1 == "SAM") and (mas2 == "MAS" or mas2 == "SAM"):
                countWords += 1
    
    print(f"\n# SOLUTION: MAS with X shape found: {countWords}\n")

if __name__ == "__main__":
    main()