
'''
Your puzzle answer was 5733696195703.

The first half of this puzzle is complete! It provides one gold star: *
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file
from utils.test_solution import test_solution

from math import prod

@test_solution(name="DAY 06 PART 1", runs=100)
def main():
    print("\n### DAY 06 PART 1 ###")

    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt"))
    if not content: return
    
    total_sum = 0
    lines = [line.split() for line in content.strip().split("\n")]

    for *col, sym in zip(*lines):
        if sym == "+":
            total_sum += sum(map(int, col))
        else:
            total_sum += prod(map(int, col))

    print(f"\n# SOLUTION: the grand total found by adding together all of the answers is: {total_sum}\n")

if __name__ == "__main__":
    main()
