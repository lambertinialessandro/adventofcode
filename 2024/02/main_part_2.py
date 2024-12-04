
'''
Your puzzle answer was 604.

Both parts of this puzzle are complete! They provide two gold stars: **
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file
from utils.math_f import sign

def checkDelta(delta):
    m, M = min(delta), max(delta)
    return (m >= -3 and M <= -1) or (m >= 1 and M <= 3)
    

def main():
    print("\n### DAY 02 PART 2 ###")

    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt"))
    if not content: return
    
    reports = [[int(num) for num in report.split(" ")] for report in content.split("\n")[:-1]]
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

        posE = []
        prec = delta[0]
        succ = delta[-1]
        for i in range(len(delta)):
            num = delta[i]
            if sign(prec) != sign(num):
                tempDelta = delta.copy()
                tempDelta.pop(i)
                if checkDelta(tempDelta):
                    dampenedCount += 1
                    break
                posE.append(i)

            if sign(succ) != sign(num):
                tempDelta = delta.copy()
                tempDelta.pop(i)
                if checkDelta(tempDelta):
                    dampenedCount += 1
                    break
                posE.append(i)

            prec = num
            if i < len(delta) - 1:
                succ = delta[i+1]
        if len(posE) > 0:
            continue

        for i in range(len(delta)):
            num = delta[i]
            if abs(num) >= 4 or num == 0:
                posE.append(i)
        posE = list(set(posE))

        if len(posE) != 1:
            continue
        
        if posE[0] == 0 or posE[0] == len(delta) - 1:
            dampenedCount += 1
            continue
        if abs(delta[posE[0] - 1] + delta[posE[0]]) < 4:
            dampenedCount += 1
            continue
    
    reportsCount += dampenedCount
    print(f"\n# SOLUTION: Report count: {reportsCount} (Dampened reports: {dampenedCount})\n")

if __name__ == "__main__":
    main()