
'''
Your puzzle answer was 56108.

The first half of this puzzle is complete! It provides one gold star: *
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file
from utils.test_solution import test_solution

import re

@test_solution(name="DAY 01 PART 1", runs=100)
def main():
    print("\n### DAY 01 PART 1 ###")

    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt")).strip()
    if not content: return

    numbers = ["".join(re.findall(r"^[A-Za-z]*?(\d)", line) + re.findall(r"(\d)[A-Za-z]*?$", line)) for line in content.split("\n")]

    sum_calibration = sum(map(int, numbers))
    
    print(f"\n# SOLUTION: sum of all of the calibration values: {sum_calibration}\n")

if __name__ == "__main__":
    main()