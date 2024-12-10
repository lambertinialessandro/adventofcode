
'''
Your puzzle answer was 12839601725877.

The first half of this puzzle is complete! It provides one gold star: *
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file

def recursiveF(tot, nums, i, tmpTot):
    if i >= len(nums) or tmpTot > tot:
        return tmpTot == tot
    
    isCorrectS = recursiveF(tot, nums, i+1, tmpTot + int(nums[i]))
    if isCorrectS: return True
    return recursiveF(tot, nums, i+1, tmpTot * int(nums[i]))

def main():
    print("\n### DAY 07 PART 1 ###")

    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt"))
    if not content: return

    operations = []
    for line in content.split("\n"):
        [tot, nums] = line.split(":")
        operations.append([tot, nums[1:].split(" ")])

    totalSum = 0
    for tot, nums in operations:
        isCorrect = recursiveF(int(tot), nums, 1, int(nums[0]))
        totalSum += int(tot) if isCorrect else 0
    
    print(operations[:5])
    
    print(f"\n# SOLUTION: __: {totalSum}\n")

if __name__ == "__main__":
    main()