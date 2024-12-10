
'''
Your puzzle answer was _____.

Both parts of this puzzle are complete! They provide two gold stars: **

12839601725877
14181189129690

13637405805052 too low
'''


import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file

def main():
    print("\n### DAY 07 PART 2 ###")

    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt"))
    if not content: return

    operations = []
    for line in content.split("\n")[:-1]:
        [tot, nums] = line.split(":")
        operations.append([int(tot), [*map(int, nums[1:].split(" "))]])

    totalSum = 0
    for tot, nums in operations:
        solutions = []
        opened = [[nums[0], f"{nums[0]}", nums[1:]]]
        #print(opened)
        while len(opened) > 0:
            [t, ops, ns] = opened.pop(len(opened)- 1)
            if len(ns) == 0:
                if t == tot:
                    solutions.append([t, ops])
                continue

            opened.append([t + ns[0], f"{ops}+{ns[0]}", ns[1:]])
            opened.append([t * ns[0], f"{ops}*{ns[0]}", ns[1:]])
            opened.append([int(str(t)+str(ns[0])), f"{ops}||{ns[0]}", ns[1:]])

            #print(opened)
        #print()
        if len(solutions) > 0:
            totalSum += tot
    
    print(solutions)
    
    print(f"\n# SOLUTION: __: {totalSum}\n")

if __name__ == "__main__":
    main()
