
'''
Your puzzle answer was 164278764924605.

Both parts of this puzzle are complete! They provide two gold stars: **
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file
from utils.test_solution import test_solution

@test_solution(name="DAY 17 PART 1", runs=100)
def main():
    print("\n### DAY 17 PART 2 ###")

    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt"))
    if not content: return

    [_, operands] = content.split("\n\n")

    original_operands = operands.split(": ")[1]
    operands = original_operands.split(",")
    operands = [int(operands[i]) for i in range(0, len(operands))]

    i = 0
    init_ra = 0
    output = ""
    while True:
        tmp_rb = init_ra % 8 ^ 1
        rb = tmp_rb ^ 5 ^ (init_ra // 2**(tmp_rb))
        curr_out = rb%8

        if i == 0:
            _output = f"{curr_out}"
        else:
            _output = f"{curr_out},{output}"

        if original_operands.endswith(_output):
            print(init_ra, i, _output)
            if i >= len(operands)-1:
                break
            
            output = _output
            i += 1
            init_ra *= 8
        else:
            init_ra += 1

    solutions = {}
    def recursive_f(ra):
        if ra in solutions:
            return solutions[ra]
        else:
            tmp_rb = ra % 8 & 0b111 ^ 1
            rb = tmp_rb ^ 5 ^ (ra // 2**(tmp_rb))
            curr_out = rb%8

            if ra // 8 != 0:
                [ret, out] = recursive_f(ra // 8)
                _output = f"{curr_out},{out}"
            else:
                ret, out = True, f"{curr_out}"
                _output = out

            if not ret:
                solutions[ra] = [False, out]
            else:
                if original_operands.endswith(out):
                    solutions[ra] = [True, _output]
                else:
                    solutions[ra] = [False, _output]
            return solutions[ra]
    while True:
        [_, output] = recursive_f(init_ra)

        if output == original_operands:
            print(output)
            break
        
        init_ra += 1
    
    print(f"\n# SOLUTION: __: {init_ra}\n")

if __name__ == "__main__":
    main()