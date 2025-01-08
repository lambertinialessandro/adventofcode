
'''
Your puzzle answer was 15006633487.

The first half of this puzzle is complete! It provides one gold star: *
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file
from utils.test_solution import test_solution

@test_solution(name="DAY 22 PART 1", runs=100)
def main():
    print("\n### DAY 22 PART 1 ###")

    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt")).strip()
    if not content: return

    secret_numbers = [*map(int, content.split("\n"))]

    def mix(value, secret_number):
        return value ^ secret_number
    def prune(secret_number):
        return secret_number % 16777216
    def new_secret_number(secret_number, reps):
        for _ in range(reps):
            secret_number = prune(mix(secret_number * 64, secret_number))
            secret_number = prune(mix(secret_number // 32, secret_number))
            secret_number = prune(mix(secret_number * 2048, secret_number))
        return secret_number

    sum_secret_numbers = sum([new_secret_number(secret_number, 2000) for secret_number in secret_numbers])
    
    print(f"\n# SOLUTION: __: {sum_secret_numbers}\n")

if __name__ == "__main__":
    main()