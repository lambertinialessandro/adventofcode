
'''
Your puzzle answer was 3255.

The first half of this puzzle is complete! It provides one gold star: *
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file
from utils.enum import SmartEnum
from utils.test_solution import test_solution

@test_solution(name="DAY 25 PART 1", runs=100)
def main():
    print("\n### DAY 25 PART 1 ###")

    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt"))
    if not content: return

    locks = []
    keys = []
    for schematic_str in content.split("\n\n"):

        schematic = schematic_str.split("\n")
        if schematic_str.startswith("#"):
            lock = []
            for c in range(5):
                count = 0
                while schematic[count][c] == "#":
                    count += 1
                lock.append(count - 1)
            locks.append(lock)
        else:
            key = []
            for c in range(5):
                count = 6
                while schematic[count][c] == "#":
                    count -= 1
                key.append(5 - count)
            keys.append(key)
    
    #print(locks)
    #print(keys)

    count_matching_pairs = 0
    for key in keys:
        for lock in locks:
            for i in range(5):
                if lock[i] + key[i] > 5:
                    break
            else:
                count_matching_pairs += 1

    print(f"\n# SOLUTION: number of unique lock/key pairs: {count_matching_pairs}\n")

if __name__ == "__main__":
    main()