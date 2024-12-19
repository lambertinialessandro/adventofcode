
'''
Your puzzle answer was 636483903099279.

Both parts of this puzzle are complete! They provide two gold stars: **
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file
from utils.test_solution import test_solution

@test_solution(name="DAY 19 PART 1", runs=10)
def main():
    print("\n### DAY 19 PART 2 ###")

    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt"))
    if not content: return

    [towels, patterns] = content.split("\n\n")
    towels = towels.split(", ")
    patterns = patterns.split("\n")

    solutions = {}
    def recursive_f(towels, pattern, i):
        if i == len(pattern):
            return 1

        if pattern[i:] not in solutions:
            sum_possible_patterns = sum([recursive_f(towels, pattern, i+len(towel)) for towel in towels if pattern[i:].startswith(towel)])
            solutions[pattern[i:]] = sum_possible_patterns
        else:
            sum_possible_patterns = solutions[pattern[i:]]

        return sum_possible_patterns

    correct_towels = sum([recursive_f(towels, pattern, 0) for pattern in patterns])
    
    print(f"\n# SOLUTION: total number of possible designs with different arrangements: {correct_towels}\n")

if __name__ == "__main__":
    main()