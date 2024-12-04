
'''
Your puzzle answer was 1834060.

The first half of this puzzle is complete! It provides one gold star: *
'''
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file

def main():
    print("\n### DAY 01 PART 1 ###")

    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt"))
    if not content: return
    
    pairs = [pair.split("   ") for pair in content.split("\n")]
    pairs.pop()
    listA, listB = [list(map(int, i)) for i in zip(*pairs)]
    listA.sort(), listB.sort()

    print("\nExample:")
    print(f"List A: {listA[0:10]}")
    print(f"List B: {listB[0:10]}")
    print(f"Distances: {[abs(a-b) for a, b in zip(listA[0:10], listB[0:10])]}")
    print(f"Total distance: {sum(abs(a-b) for a, b in zip(listA[0:10], listB[0:10]))}")
    
    totalDistance = sum(abs(a-b) for a, b in zip(listA, listB))
    print(f"\n# SOLUTION: Total distance: {totalDistance}\n")

if __name__ == "__main__":
    main()