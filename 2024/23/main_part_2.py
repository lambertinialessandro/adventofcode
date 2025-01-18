
'''
Your puzzle answer was ag,gh,hh,iv,jx,nq,oc,qm,rb,sm,vm,wu,zr.

Both parts of this puzzle are complete! They provide two gold stars: **
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file
from utils.test_solution import test_solution

@test_solution(name="DAY 23 PART 2", runs=100)
def main():
    print("\n### DAY 23 PART 2 ###")

    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt")).strip()
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

    for k in computers:
        computers[k] = sorted(list(computers[k]))
    
    three_connections = set()
    visited = []
    def recursive_f(curr_conns, curr_k):
        solutions = []

        
        if curr_k in visited:
            return curr_conns
        for next_k in computers[curr_k]:
            for conn in curr_conns[:-1]:
                if next_k not in computers[conn]:
                    break
            else:
                solutions.extend(recursive_f([*curr_conns, next_k], next_k))
        
        visited.append(curr_k)
        return [curr_conns] if len(solutions) == 0 else [max(solutions, key=lambda x: len(x))]

    passwords = set(tuple(sorted(recursive_f([k], k)[0])) for k in sorted(list(computers)))
    
    print(f"\n# SOLUTION: password to get into the LAN party: {','.join(max(passwords, key=lambda x: len(x)))}\n")

if __name__ == "__main__":
    main()