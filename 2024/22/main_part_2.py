"""
Your puzzle answer was 1710.

Both parts of this puzzle are complete! They provide two gold stars: **
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from utils.read_file import read_file
from utils.test_solution import test_solution


@test_solution(name="DAY 22 PART 2", runs=10)
def main():
    print("\n### DAY 22 PART 2 ###")

    content = read_file(os.path.join(os.path.dirname(__file__), "input.txt")).strip()
    if not content:
        return

    secret_numbers = [*map(int, content.split("\n"))]
    visited = {}

    num_elements = len(secret_numbers)
    prices = {}

    def mix(value, secret_number):
        return value ^ secret_number

    def prune(secret_number):
        return secret_number % 16777216

    def step(secret_number):
        old_secret_number = secret_number
        secret_number = prune(mix(secret_number * 64, secret_number))
        secret_number = prune(mix(secret_number // 32, secret_number))
        secret_number = prune(mix(secret_number * 2048, secret_number))
        visited[old_secret_number] = secret_number
        return secret_number

    def new_secret_number(secret_number, reps, idx):
        secret_number = step(secret_number)

        old_price = secret_number % 10
        sequence = []
        for j in range(1, reps):
            if secret_number in visited:
                secret_number = visited[secret_number]
            else:
                secret_number = step(secret_number)

            price = secret_number % 10
            delta = price - old_price

            sequence.append(delta)
            if j > 4:
                sequence = sequence[1:]
            else:
                continue

            key = tuple(sequence)
            if key not in prices:
                prices[key] = [-1] * num_elements

            if prices[key][idx] == -1:
                prices[key][idx] = price

            old_price = price

        return secret_number

    for i in range(num_elements):
        new_secret_number(secret_numbers[i], 2000, i)

    total_bananas = max(
        [sum([num for num in prices[key] if num != -1]) for key in prices]
    )

    print(f"\n# SOLUTION: the most bananas I can get is {total_bananas}\n")


if __name__ == "__main__":
    main()
