
'''
Your puzzle answer was 564.

The first half of this puzzle is complete! It provides one gold star: *
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file
from utils.test_solution import test_solution

@test_solution(name="DAY 02 PART 1", runs=100)
def main():
    print("\n### DAY 02 PART 1 ###")

    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt"))
    if not content: return
    
    reports = [[*map(int, report.split(" "))] for report in content.split("\n")]
    deltas = [[succ - curr for curr, succ in zip(report[:-1], report[1:])]for report in reports]
    deltas_min_max = [[min(delta), max(delta)] for delta in deltas]

    print("\nExample:")
    print(f"Reports: {reports[:4]}")
    print(f"Deltas: {deltas[:4]}")
    print(f"Min/Max delta: {deltas_min_max[:4]}")

    reportsCount = sum([1 for m, M in deltas_min_max if (m >= -3 and M <= -1) or (m >= 1 and M <= 3)])
    print(f"\n# SOLUTION: Report count: {reportsCount}\n")

if __name__ == "__main__":
    main()