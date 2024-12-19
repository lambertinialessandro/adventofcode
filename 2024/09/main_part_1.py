
'''
Your puzzle answer was 6401092019345.

The first half of this puzzle is complete! It provides one gold star: *
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file
from utils.test_solution import test_solution

@test_solution(name="DAY 09 PART 1", runs=100)
def main():
    print("\n### DAY 09 PART 1 ###")

    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt"))
    if not content: return

    checksum = ""
    i = 0
    idI = 0
    j = len(content)-1
    idJ = j // 2
    vJ = int(content[j])
    countJ = 0
    while i < j and idI < idJ:
        v = int(content[i])
        if i % 2 == 1:
            if idJ == 13:
                print(i, j, idI, idJ)
            for _ in range(v):
                if countJ >= vJ:
                    vJ = 0
                    while vJ == 0:
                        j -= 2
                        vJ = int(content[j])
                        idJ -= 1
                    countJ = 0
                checksum += f" {idJ}"
                countJ += 1
            i += 1
        else:
            for _ in range(v):
                checksum += f" {idI}"
            idI += 1
            i += 1
    while countJ < vJ:
        checksum += f" {idJ}"
        countJ += 1
    
    sumChecksum = sum([i * int(_v) for i, _v in enumerate(filter(None, checksum.split(" ")))])
    print(f"\n# SOLUTION: filesystem checksum: {sumChecksum}\n")

if __name__ == "__main__":
    main()