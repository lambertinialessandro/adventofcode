
'''
Your puzzle answer was 21558.

The first half of this puzzle is complete! It provides one gold star: *
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file
from utils.test_solution import test_solution

import re

@test_solution(name="DAY 04 PART 1", runs=100)
def main():
    print("\n### DAY 04 PART 1 ###")

    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt"))
    if not content: return

    points = 0
    for winning, numbers in re.findall(r"([\d\s]+)\|([\d\s]+)\n", content):
        winning = list(map(int, winning.split()))
        numbers = list(map(int, numbers.split()))
        count_w_n = sum([w_n in numbers for w_n in winning])
        if count_w_n != 0:
            points += 2**(count_w_n-1)
    
    print(f"\n# SOLUTION: {points}\n")

if __name__ == "__main__":
    main()