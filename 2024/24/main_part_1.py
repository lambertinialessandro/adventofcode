
'''
Your puzzle answer was 69201640933606.

The first half of this puzzle is complete! It provides one gold star: *
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file
from utils.enum import SmartEnum
from utils.test_solution import test_solution

class Operation(SmartEnum):
    AND = "AND"
    OR = "OR"
    XOR = "XOR"

@test_solution(name="DAY 24 PART 1", runs=100)
def main():
    print("\n### DAY 24 PART 1 ###")

    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt")).strip()
    if not content: return

    gates_str, connections_str = content.split("\n\n")
    gates = [gate.split(": ") for gate in gates_str.split("\n")]
    gates = {g: int(v) for g, v in gates}

    connections = {}
    opened = []
    for connection in connections_str.split("\n"):
        operation, res_gate = connection.split(" -> ")
        op1, logic_op, op2 = operation.split(" ")

        connections[res_gate] = [op1, logic_op, op2]
        
        opened.append(res_gate)
    out_gates = sorted([gate for gate in opened if gate.startswith("z")], reverse=True)
    
    while len(opened) != 0:
        gate = opened.pop()
        
        if gate not in gates:
            [op1, logic_op, op2] = connections[gate]
            
            if op1 in gates and op2 in gates:
                if Operation.AND() == logic_op:
                    res = gates[op1] & gates[op2]
                elif Operation.OR() == logic_op:
                    res = gates[op1] | gates[op2]
                elif Operation.XOR() == logic_op:
                    res = gates[op1] ^ gates[op2]
                
                gates[gate] = res
            else:
                opened.append(gate)
                opened.append(op1)
                opened.append(op2)

    combined_gates = "".join([str(gates[gate]) for gate in out_gates])
    decimal_result = int(combined_gates, 2)

    print(f"\n# SOLUTION: decimal number output on the wires starting with z: {decimal_result}\n")

if __name__ == "__main__":
    main()