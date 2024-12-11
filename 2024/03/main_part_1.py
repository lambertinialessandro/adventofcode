
'''
Your puzzle answer was 170778545.

The first half of this puzzle is complete! It provides one gold star: *
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file
from utils.test_solution import test_solution

import re

@test_solution(name="DAY 03 PART 1", runs=100)
def main():
    print("\n### DAY 03 PART 1 ###")

    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt"))
    if not content: return

    print("\nExample:")
    print(f"Instruction: {content[:100]}...")
    print(f"Muls: {re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", content[:100])}")
    print(f"Muls x and y: {re.findall("mul\(([0-9]{1,3}),([0-9]{1,3})\)", content[:100])}")
    print(f"Results mul: {[int(x) * int(y) for x, y in re.findall("mul\(([0-9]{1,3}),([0-9]{1,3})\)", content[:100])]}")

    uncorruptedMul = sum([int(x) * int(y) for x, y in re.findall("mul\(([0-9]{1,3}),([0-9]{1,3})\)", content)])
    
    print(f"\n# SOLUTION: Uncorrupted mul: {uncorruptedMul}\n")

if __name__ == "__main__":
    main()