
'''
Your puzzle answer was 82868252.

Both parts of this puzzle are complete! They provide two gold stars: **
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file

import re

def main():
    print("\n### DAY 03 PART 2 ###")

    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt"))
    if not content: return

    print("\nExample:")
    print(f"Instruction: {content[100:200]}...")
    print(f"Matches: {re.findall("mul\(([0-9]{1,3}),([0-9]{1,3})\)|(do\(\))|(don\'t\(\))", content[100:200])}")
  
    uncorruptedMul = 0
    isEnabled = True
    matches = re.findall("mul\(([0-9]{1,3}),([0-9]{1,3})\)|(do\(\))|(don\'t\(\))", content)
        
    for m in matches:
        m = list(m)
        if isEnabled:
            if m[3]:
                # print("Disable")
                isEnabled = False
            elif m[2]:
                pass
            else:
                x, y = int(m[0]), int(m[1])
                # print(f"Multiply: {x} x {y}")
                uncorruptedMul += x * y
        else:
            if m[2]:
                # print("Enable")
                isEnabled = True
    
    print(f"\n# SOLUTION: Uncorrupted mul: {uncorruptedMul}\n")

if __name__ == "__main__":
    main()