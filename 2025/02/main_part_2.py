
'''
Your puzzle answer was 25663320831.

Both parts of this puzzle are complete! They provide two gold stars: **
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file
from utils.test_solution import test_solution

@test_solution(name="DAY 02 PART 2", runs=10)
def main():
    print("\n### DAY 02 PART 2 ###")

    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt"))
    if not content: return
    
    id_rangess = content.strip().split(",")
    print(f"number of ids: {len(id_rangess)}")
    sum_repeated = 0

    for id_range in id_rangess:
        start, end = [int(x) for x in id_range.split("-")]
        print("\nSTART", id_range, start, end)
        
        number = start
        while number <= end:
            number_s = str(number)
            size = len(number_s)
            
            # is 1-9
            if size == 1:
                number = 11
                continue

            # odd length
            if size % 2 != 0:
                for i in range(1, size//2+1, 2):
                    if size % i != 0:
                        continue
                    
                    patt = number_s[:i]
                    if number_s.count(patt) == size//i:
                        print(f"repeated: {number}")
                        sum_repeated += number
                        break
                
                number += 1 # TODO: optimize
                continue
            
            # is 10-99
            if size == 2:
                if number_s[0] == number_s[1]:
                    print(f"repeated: {number}")
                    sum_repeated += number
                    number += 11
                    continue
                else:
                    number += (11 - (number % 11))
                    continue
                
            # even length
            else:
                for i in range(1, size//2+1, 1):
                    if size % i != 0:
                        continue
                    
                    patt = number_s[:i]
                    if number_s.count(patt) == size//i:
                        print(f"repeated: {number}")
                        sum_repeated += number
                        break
                
                number += 1 # TODO: optimize
                continue

            
        print(f"\nEND number {number}")
    
    print(f"\n# SOLUTION: all the invalid IDs add up to: {sum_repeated}\n")

if __name__ == "__main__":
    main()
    