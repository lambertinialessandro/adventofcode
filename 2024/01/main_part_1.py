
'''
Your puzzle answer was 1834060.

The first half of this puzzle is complete! It provides one gold star: *
'''
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file
from utils.test_solution import test_solution

@test_solution(name="DAY 01 PART 1", runs=100)
def main():
    print("\n### DAY 01 PART 1 ###")

    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt")).strip()
    if not content: return
    
    pairs = [pair.split("   ") for pair in content.split("\n")]
    list_a, list_b = zip(*pairs)
    list_a = sorted(map(int, list_a))
    list_b = sorted(map(int, list_b))

    print("\nExample:")
    print(f"List A: {list_a[:10]}")
    print(f"List B: {list_b[:10]}")
    print(f"Distances: {[abs(a - b) for a, b in zip(list_a[:10], list_b[:10])]}")
    print(f"Total distance: {sum(abs(a - b) for a, b in zip(list_a, list_b))}")

    total_distance = sum(abs(a - b) for a, b in zip(list_a, list_b))
    print(f"\n# SOLUTION: Total distance: {total_distance}\n")

if __name__ == "__main__":
    main()