
'''
Your puzzle answer was 7,4,2,5,1,4,6,0,4.

The first half of this puzzle is complete! It provides one gold star: *
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file
from utils.test_solution import test_solution

@test_solution(name="DAY 17 PART 1", runs=100)
def main():
    print("\n### DAY 17 PART 1 ###")

    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt"))
    if not content: return

    [registers, operands] = content.split("\n\n")
    [ra, rb, rc] = [int(line.split(": ")[1]) for line in registers.strip().split("\n")]
    ra = 164278764924605
    print([ra, rb, rc])

    operands = operands.split(": ")[1].split(",")
    operands = [[operands[i], int(operands[i + 1])] for i in range(0, len(operands), 2)]
    print(operands)

    def get_combo(operand):
        if operand <= 3:
            return operand
        elif operand == 4:
            return ra
        elif operand == 5:
            return rb
        elif operand == 6:
            return rc
        elif operand == 7:
            raise NotImplementedError

    output = ""
    i = 0
    while i < len(operands):
        [opcode, operand] = operands[i]

        if opcode == "0":
            combo = get_combo(operand)
            ra = ra // 2**combo
        if opcode == "1":
            rb = rb ^ operand
        if opcode == "2":
            combo = get_combo(operand)
            rb = combo % 8 & 0b111
        if opcode == "3":
            if ra != 0:
                i = operand // 2
                continue
        if opcode == "4":
            rb = rb ^ rc
        if opcode == "5":
            combo = get_combo(operand)
            output += str(combo % 8) + ","
        if opcode == "6":
            combo = get_combo(operand)
            rb = ra // 2**combo
        if opcode == "7":
            combo = get_combo(operand)
            rc = ra // 2**combo

        i += 1

    output = output[:-1]
    print(f"\n# SOLUTION: program output commas separated: {output}\n")

if __name__ == "__main__":
    main()