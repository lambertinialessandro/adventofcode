"""
Your puzzle answer was 517315308154944.

Both parts of this puzzle are complete! They provide two gold stars: **
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from utils.read_file import read_file
from utils.test_solution import test_solution

from collections import defaultdict


@test_solution(name="DAY 11 PART 2", runs=100)
def main():
    print("\n### DAY 11 PART 2 ###")

    content = read_file(os.path.join(os.path.dirname(__file__), "input.txt"))
    if not content:
        return

    connections = defaultdict(list)
    for line in content.strip().split("\n"):
        device, outputs = line.split(": ")
        connections[device] = outputs.split(" ")
    # print(connections)

    depth = 0
    nodes_depth = {"svr": 0, "dac": 0, "fft": 0, "out": 0}
    queue = [["svr"]]

    while len(queue) > 0:
        devices = queue.pop()
        next_lvl = set()

        for device in devices:
            conns = connections[device]

            if "dac" in conns:
                nodes_depth["dac"] = depth + 1
            elif "fft" in conns:
                nodes_depth["fft"] = depth + 1
            elif "out" in conns:
                nodes_depth["out"] = depth + 1
            next_lvl.update(set(conns))

        depth += 1
        if len(next_lvl) > 0:
            queue.append(next_lvl)

    nodes_visit_order = sorted(
        [[k, v] for k, v in nodes_depth.items()], key=lambda x: x[1]
    )
    print("nodes", nodes_visit_order)

    count_paths = 1

    visited = {}

    def recursive_exploration(device, depth, target_device, target_depth):

        if device in visited.keys():
            return visited[device]

        if device == target_device:
            visited[device] = 1
            return 1

        if depth >= target_depth:
            return 0

        local_count_paths = 0
        conn = connections[device]
        for d in conn:
            local_count_paths += recursive_exploration(
                d, depth + 1, target_device, target_depth
            )

        visited[device] = local_count_paths
        return local_count_paths

    prev = nodes_visit_order[0]
    for curr in nodes_visit_order[1:]:
        visited = {}
        curr_count_paths = recursive_exploration(prev[0], prev[1], curr[0], curr[1])
        print(f"from {prev} to {curr} -> {curr_count_paths}")
        count_paths = count_paths * curr_count_paths
        prev = curr

    print(
        f"\n# SOLUTION: number of different paths that lead from svr to both dac and fft and finish to out: {count_paths}\n"
    )


if __name__ == "__main__":
    main()
