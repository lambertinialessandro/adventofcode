"""
Your puzzle answer was dhq,hbs,jcp,kfp,pdg,z18,z22,z27.

Both parts of this puzzle are complete! They provide two gold stars: **
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from utils.read_file import read_file
from utils.enum import SmartEnum
from utils.test_solution import test_solution


class Operation(SmartEnum):
    AND = "AND"
    OR = "OR"
    XOR = "XOR"

@test_solution(name="DAY 24 PART 2", runs=100)
def main():
    print("\n### DAY 24 PART 2 ###")

    content = read_file(os.path.join(os.path.dirname(__file__), "input.txt")).strip()
    if not content:
        return

    _, connections_str = content.split("\n\n")

    connections = []
    for connection in connections_str.split("\n"):
        operation, res_gate = connection.split(" -> ")
        op1, logic_op, op2 = operation.split(" ")

        connections.append((op1, logic_op, op2, res_gate))

    out_gates = sorted(
        [res_gate for _, _, _, res_gate in connections if res_gate.startswith("z")],
        reverse=True,
    )
    max_z = out_gates[0]

    wrong = set()

    for op1, logic_op, op2, res_gate in connections:
        operands = [op1, op2]
        is_input = any(i.startswith(("x", "y")) for i in operands)
        is_first = "x00" in operands or "y00" in operands

        # Rule 1: Every z_i output (except the final overflow bit) MUST be driven by an XOR gate
        if res_gate.startswith("z") and res_gate != max_z:
            if logic_op != Operation.XOR():
                wrong.add(res_gate)

        # Rule 2: XOR gates that do NOT take x/y inputs MUST drive a z_i output
        if (
            logic_op == Operation.XOR()
            and not is_input
            and not res_gate.startswith("z")
        ):
            wrong.add(res_gate)

        # Rule 3: Primary XOR gates (x_i XOR y_i, except bit 0) MUST feed into a secondary XOR gate
        if logic_op == Operation.XOR() and is_input and not is_first:
            for n_op1, n_logic_op, n_op2, _ in connections:
                if n_logic_op == Operation.XOR() and (
                    res_gate == n_op1 or res_gate == n_op2
                ):
                    break
            else:
                wrong.add(res_gate)

        # Rule 4: AND gates (except bit 0) MUST feed into an OR gate
        if logic_op == Operation.AND() and not is_first:
            for n_op1, n_logic_op, n_op2, _ in connections:
                if n_logic_op == Operation.OR() and (
                    res_gate == n_op1 or res_gate == n_op2
                ):
                    break
            else:
                wrong.add(res_gate)

    swapped_wires = ",".join(sorted(wrong))
    print(f"\n# SOLUTION: the eight wires involved in a swap are: {swapped_wires}\n")


if __name__ == "__main__":
    main()
