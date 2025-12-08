"""
Your puzzle answer was 112230.

The first half of this puzzle is complete! It provides one gold star: *
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from utils.read_file import read_file
from utils.test_solution import test_solution

import math
import heapq


@test_solution(name="DAY 08 PART 1", runs=10)
def main():
    print("\n### DAY 08 PART 1 ###")

    content = read_file(os.path.join(os.path.dirname(__file__), "input.txt"))
    if not content:
        return

    points = [(*map(int, line.split(",")),) for line in content.strip().split("\n")]

    max_connections = 1000
    distances = []
    for i, p1 in enumerate(points):
        for p2 in points[i + 1 :]:
            distance = math.dist(p2, p1)
            if len(distances) < max_connections:
                heapq.heappush(distances, (-distance, p1, p2))
            else:
                if distance < -distances[0][0]:
                    heapq.heapreplace(distances, (-distance, p1, p2))
    distances = sorted([(-d, p1, p2) for d, p1, p2 in distances], key=lambda x: x[0])[
        :max_connections
    ]

    connections = {}
    idx_group = 0
    groups = {}
    for _, p1, p2 in distances:
        conn1 = connections.get(p1)
        conn2 = connections.get(p2)
        
        if conn1 is None and conn2 is None:
            connections[p1] = idx_group
            connections[p2] = idx_group
            groups[idx_group] = [p1, p2]
            idx_group += 1
        elif conn1 is None:
            connections[p1] = conn2
            groups[conn2].append(p1)
        elif conn2 is None:
            connections[p2] = conn1
            groups[conn1].append(p2)
        elif conn1 != conn2:
            if len(groups[conn1]) < len(groups[conn2]):
                conn1, conn2 = conn2, conn1
                
            for point in groups[conn2]:
                connections[point] = conn1
                
            groups[conn1].extend(groups[conn2])
            del groups[conn2]

    size_big_3 = math.prod(sorted(map(len, groups.values()), reverse=True)[:3])
    
    print(
        f"\n# SOLUTION: the sizes of the three largest circuits multiply together is: {size_big_3}\n"
    )


if __name__ == "__main__":
    main()
