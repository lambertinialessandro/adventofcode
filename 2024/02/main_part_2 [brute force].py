
'''
Your puzzle answer was 604.

Both parts of this puzzle are complete! They provide two gold stars: **
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file

def checkDelta(delta):
    m, M = min(delta), max(delta)
    return (m >= -3 and M <= -1) or (m >= 1 and M <= 3)

def evaluateNewReport(report, i):
    tempReport = report.copy()
    tempReport.pop(i)
    delta = [succ - curr for curr, succ in zip(tempReport[:-1], tempReport[1:])]

    return checkDelta(delta)

def main():
    print("\n### DAY 02 PART 2 [BRUTE FORCE] ###")

    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt"))
    if not content: return
    
    reports = [[int(num) for num in report.split(" ")] for report in content.split("\n")]
    deltas = [[succ - curr for curr, succ in zip(report[:-1], report[1:])]for report in reports]

    print("\nExample:")
    print(f"Reports: {reports[:4]}")
    print(f"Deltas: {deltas[:4]}")

    reportsCount = 0
    dampenedCount = 0
    for report in reports:
        delta = [succ - curr for curr, succ in zip(report[:-1], report[1:])]

        if checkDelta(delta):
            reportsCount += 1
            continue

        for i in range(len(report)):
            if evaluateNewReport(report, i):
                dampenedCount += 1
                break
            
    
    reportsCount += dampenedCount
    print(f"\n# SOLUTION: Report count: {reportsCount} (Dampened reports: {dampenedCount})\n")

if __name__ == "__main__":
    main()