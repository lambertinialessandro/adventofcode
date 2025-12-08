
'''
Your puzzle answer was ____.

Both parts of this puzzle are complete! They provide two gold stars: **
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file
from utils.test_solution import test_solution

import math

@test_solution(name="DAY 08 PART 2", runs=100)
def main():
    print("\n### DAY 08 PART 2 ###")

    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt"))
    if not content: return
    
    points = [(*map(int, line.split(",")),) for line in content.strip().split("\n")]
    
    distances = []
    for i, p1 in enumerate(points):
        for p2 in points[i+1:]:
            distance = math.dist(p2, p1)
            distances.append([distance, p1, p2])
    distances.sort(key=lambda x: x[0])
    
    connections = {}
    idx_group = 0
    groups = {}
    missing_points = points
    for _, p1, p2 in distances:
        if len(groups.keys()) == 1 and len(missing_points) == 0:
            break
        
        conn1 = connections.get(p1)
        conn2 = connections.get(p2)
        last_p1, last_p2 = p1, p2
        
        if conn1 is None and conn2 is None:
            connections[p1] = idx_group
            connections[p2] = idx_group
            groups[idx_group] = [p1, p2]
            missing_points.remove(p1)
            missing_points.remove(p2)
            idx_group += 1
        elif conn1 is None:
            connections[p1] = conn2
            groups[conn2].append(p1)
            missing_points.remove(p1)
        elif conn2 is None:
            connections[p2] = conn1
            groups[conn1].append(p2)
            missing_points.remove(p2)
        elif conn1 != conn2:
            if len(groups[conn1]) < len(groups[conn2]):
                conn1, conn2 = conn2, conn1
                
            for point in groups[conn2]:
                connections[point] = conn1
                
            groups[conn1].extend(groups[conn2])
            del groups[conn2]

    prod_last_x = last_p1[0] * last_p2[0]

    print(f"\n# SOLUTION: the moltiplication of the X coordinates of the last two junction boxes you need to connect is: {prod_last_x}\n")

if __name__ == "__main__":
    main()
