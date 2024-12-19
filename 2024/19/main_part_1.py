
'''
Your puzzle answer was 285.

The first half of this puzzle is complete! It provides one gold star: *
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file
from utils.test_solution import test_solution

@test_solution(name="DAY 19 PART 1", runs=100)
def main():
    print("\n### DAY 19 PART 1 ###")

    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt"))
    if not content: return

    [towels, patterns] = content.split("\n\n")
    towels = towels.split(", ")
    patterns = patterns.split("\n")

    def recursive_f(towels, pattern, i):
        if i == len(pattern):
            return True

        for towel in towels:
            if pattern[i:].startswith(towel) and recursive_f(towels, pattern, i+len(towel)):
                return True
        return False

    correct_towels = sum([1 for pattern in patterns if recursive_f(towels, pattern, 0)])
    
    print(f"\n# SOLUTION: total designs possible: {correct_towels}\n")

if __name__ == "__main__":
    main()