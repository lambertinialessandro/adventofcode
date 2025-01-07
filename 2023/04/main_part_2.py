
'''
Your puzzle answer was 10425665.

Both parts of this puzzle are complete! They provide two gold stars: **
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file
from utils.test_solution import test_solution

import re

@test_solution(name="DAY 04 PART 2", runs=100)
def main():
    print("\n### DAY 04 PART 2 ###")

    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt"))
    if not content: return

    total_scratchcards = 0
    scratchcards_winned = [1]
    for winning, numbers in re.findall(r"([\d\s]+)\|([\d\s]+)\n", content):
        #print(f"scratchcards_winned: {scratchcards_winned}")

        num_scratchcards = 1
        if len(scratchcards_winned) != 0:
            num_scratchcards = scratchcards_winned.pop(0)

        winning = list(map(int, winning.split()))
        numbers = list(map(int, numbers.split()))
        count_w_n = sum([w_n in numbers for w_n in winning])
        #print(f"num_scratchcards: {num_scratchcards}, count_w_n: {count_w_n}")

        total_scratchcards += num_scratchcards

        for i in range(count_w_n):
            if len(scratchcards_winned) > i:
                scratchcards_winned[i] += 1 * num_scratchcards
            else:
                scratchcards_winned.append(1 + 1 * num_scratchcards)
    
    print(f"\n# SOLUTION: {total_scratchcards}\n")

if __name__ == "__main__":
    main()