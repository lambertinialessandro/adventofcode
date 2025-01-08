
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


    [gates_str, connections_str] = content.split("\n\n")

    gates = [gate.split(": ") for gate in gates_str.split("\n")]
    gates = {g: int(v) for g, v in gates}

    connections = {}
    for connection in connections_str.split("\n"):
        [operation, res_gate] = connection.split(" -> ")
        [op1, logic_op, op2] = operation.split(" ")

        print(op1)

        if op1 not in connections:
            connections[op1] = []
        connections[op1].append([op1, logic_op, op2, res_gate])
        if op2 not in connections:
            connections[op2] = []
        connections[op2].append([op1, logic_op, op2, res_gate])

    print(f"gates: {gates}")
    print(f"connections: {connections}")

    dep_gates = []
    opened = set()
    missing_one = {}
    missing_two = {}
    for gate in gates:
        for [op1, logic_op, op2, res_gate] in connections[gate]:
            is_op1_missing = op1 not in gates
            is_op2_missing = op2 not in gates
            print(f"\tpop: {[op1, logic_op, op2, res_gate]}, {is_op1_missing}, {is_op2_missing}")

            if is_op1_missing and is_op2_missing:
                if op1 not in dep_gates: dep_gates.append(op1)
                if op2 not in dep_gates: dep_gates.append(op2)
                if op1 not in missing_two:
                    missing_two[op1] = set()
                missing_two[op1].add(tuple([op2, tuple([op1, logic_op, op2, res_gate])]))
                if op2 not in missing_two:
                    missing_two[op2] = set()
                missing_two[op2].add(tuple([op1, tuple([op1, logic_op, op2, res_gate])]))
            elif is_op1_missing:
                if op1 not in dep_gates: dep_gates.append(op1)
                if op1 not in missing_one:
                    missing_one[op1] = set()
                missing_one[op1].add(tuple([op1, logic_op, op2, res_gate]))
            elif is_op2_missing:
                if op2 not in dep_gates: dep_gates.append(op2)
                if op2 not in missing_one:
                    missing_one[op2] = set()
                missing_one[op2].add(tuple([op1, logic_op, op2, res_gate]))
            else:
                opened.add(tuple([op1, logic_op, op2, res_gate]))
            
            if res_gate not in dep_gates:
                dep_gates.append(res_gate)
    
    i = 0
    while i < len(dep_gates):
        gate = dep_gates[i]
        if gate not in connections:
            i += 1
            continue
        for [op1, logic_op, op2, res_gate] in connections[gate]:
            is_op1_missing = op1 not in gates
            is_op2_missing = op2 not in gates

            if is_op1_missing and is_op2_missing:
                if op1 not in dep_gates: dep_gates.append(op1)
                if op2 not in dep_gates: dep_gates.append(op2)
                if op1 not in missing_two:
                    missing_two[op1] = set()
                missing_two[op1].add(tuple([op2, tuple([op1, logic_op, op2, res_gate])]))
                if op2 not in missing_two:
                    missing_two[op2] = set()
                missing_two[op2].add(tuple([op1, tuple([op1, logic_op, op2, res_gate])]))
            elif is_op1_missing:
                if op1 not in dep_gates: dep_gates.append(op1)
                if op1 not in missing_one:
                    missing_one[op1] = set()
                missing_one[op1].add(tuple([op1, logic_op, op2, res_gate]))
            elif is_op2_missing:
                if op2 not in dep_gates: dep_gates.append(op2)
                if op2 not in missing_one:
                    missing_one[op2] = set()
                missing_one[op2].add(tuple([op1, logic_op, op2, res_gate]))
            
            if res_gate not in dep_gates:
                dep_gates.append(res_gate)
        i += 1

    out_gates = sorted([gate for gate in dep_gates if gate.startswith("z")], reverse=True)
    print(f"dep_gates: {dep_gates}")
    print(f"opened: {opened}")
    print(f"missing_one: {missing_one}")
    print(f"missing_two: {missing_two}")


    while True:
        if len(opened) == 0:
            break

        [op1, logic_op, op2, res_gate] = opened.pop()
        print(f"\tpop: {[op1, logic_op, op2, res_gate]}")

        if Operation.AND() == logic_op:
            res = gates[op1] & gates[op2]
            pass
        elif Operation.OR() == logic_op:
            res = gates[op1] | gates[op2]
            pass
        elif Operation.XOR() == logic_op:
            res = gates[op1] ^ gates[op2]
            pass
        
        gates[res_gate] = res

        if res_gate in missing_two:
            for [locked_gates, locked_res_gate] in missing_two[res_gate]:
                if locked_gates in gates:
                    continue

                if locked_gates not in missing_one:
                    missing_one[locked_gates] = set()
                missing_one[locked_gates].add(locked_res_gate)
        
        if res_gate in missing_one:
            for unlocked_gate in missing_one[res_gate]:
                opened.add(unlocked_gate)


    print(f"dep_gates: {dep_gates}")
    print(f"opened: {opened}")
    print(f"missing_one: {missing_one}")
    print(f"missing_two: {missing_two}")

    print(f"gates: {gates}")

    for gate in sorted(gates):
        print(gate, gates[gate])
    
    print(out_gates)

    combined_gates = "".join([str(gates[gate]) for gate in out_gates])
    print(combined_gates, int(combined_gates, 2))
    
    print(f"\n# SOLUTION: __: {int(combined_gates, 2)}\n")

if __name__ == "__main__":
    main()