
'''
Your puzzle answer was 87596249540359.

Both parts of this puzzle are complete! They provide two gold stars: **
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file
from utils.test_solution import test_solution

import re

@test_solution(name="DAY 13 PART 2", runs=100)
def main():
    print("\n### DAY 13 PART 2 ###")

    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt"))
    if not content: return

    buttons_a = re.findall("A: X\+(\d+), Y\+(\d+)", content)
    buttons_b = re.findall("B: X\+(\d+), Y\+(\d+)", content)
    prizes = re.findall("Prize: X=(\d+), Y=(\d+)", content)

    total_prizes = 0
    for button_a, button_b, prize in [*zip(buttons_a, buttons_b, prizes)]:
        [bax, bay] = [*map(int, button_a)]
        [bbx, bby] = [*map(int, button_b)]
        [px, py] = [prize + 10000000000000 for prize in map(int, prize)]

        # x b_a_x + y b_b_x = p_x
        # x b_a_y + y b_b_y = p_y
        y = (py*bax - px*bay)/(bby*bax - bbx*bay)
        x = (px - y*bbx)/bax

        if x % 1 == 0 and y % 1 == 0:
            total_prizes += 3*x + y
        
    print(f"\n# SOLUTION: tokens spend to win all possible prizes: {int(total_prizes)}\n")

if __name__ == "__main__":
    main()