
'''
Your puzzle answer was 169019504359949.

Both parts of this puzzle are complete! They provide two gold stars: **
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file
from utils.test_solution import test_solution

def find_battery(bank, depth, pos):
    battery = "0"
    other_batteries = ""
    
    for i in range(len(bank)-depth, pos-1, -1):
        b = bank[i]
        
        if b < battery: continue
        
        if depth > 1:
            other_batteries = find_battery(bank, depth-1, i+1)
            battery = b
        else:
            if b > battery:
                battery = b
    
    return battery+other_batteries

@test_solution(name="DAY 03 PART 2", runs=10)
def main():
    print("\n### DAY 03 PART 2 ###")

    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt"))
    if not content: return
    
    total_joltage = 0

    banks = content.strip().split("\n")
    for bank in banks:
        print(f"\nBank: {bank}")
        
        batteries = find_battery(bank, 12, 0)
        print(f"Batteries: {batteries}")
        
        total_joltage += int(batteries)

    print(f"\n# SOLUTION: the new total output joltage is: {total_joltage}\n")

if __name__ == "__main__":
    main()
