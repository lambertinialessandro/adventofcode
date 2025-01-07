
'''
Your puzzle answer was 1200.

The first half of this puzzle is complete! It provides one gold star: *
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file
from utils.test_solution import test_solution

@test_solution(name="DAY 23 PART 1", runs=100)
def main():
    print("\n### DAY 23 PART 1 ###")

    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt"))
    if not content: return

    computers = {}

    def add_connection(name, other_name):
        if name not in computers:
            computers[name] = set()
        computers[name].add(other_name)

    for line in content.split("\n"):
        [name, other_name] = line.split("-")
        add_connection(name, other_name)
        add_connection(other_name, name)

    #print(computers)

    three_connections = set()
    for k1 in computers:
        hasT1 = k1.startswith("t")
        for k2 in computers[k1]:
            hasT2 = k2.startswith("t")
            for k3 in computers[k2]:
                hasT3 = k3.startswith("t")
                if k1 in computers[k3] and (hasT1 or hasT2 or hasT3):
                    three_connections.add(tuple(sorted([k1, k2, k3])))

    #print(sorted(three_connections))
    
    print(f"\n# SOLUTION: __: {len(three_connections)}\n")

if __name__ == "__main__":
    main()