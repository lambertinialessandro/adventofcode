import os
import sys
import heapq
import math
from collections import defaultdict

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from utils.read_file import read_file
from utils.enum import SmartEnum
from utils.test_solution import test_solution


class Tile(SmartEnum):
    EMPTY = "."
    WALL = "#"
    START = "S"
    END = "E"


class Direction(SmartEnum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

def move_forward(r, c, d):
    if d == Direction.NORTH:
        return r - 1, c
    if d == Direction.SOUTH:
        return r + 1, c
    if d == Direction.EAST:
        return r, c + 1
    if d == Direction.WEST:
        return r, c - 1

# @test_solution(name="DAY 16 PART 2", runs=10)
def main():
    print("\n### DAY 16 PART 2 (final correct) ###")

    content = read_file(os.path.join(os.path.dirname(__file__), "input.txt"))
    if not content:
        return

    env = [[*line] for line in content.split("\n")]
    sr = sc = er = ec = -1
    for i, line in enumerate(env):
        if sr == -1 and Tile.START() in line:
            sr, sc = i, line.index(Tile.START())
        if er == -1 and Tile.END() in line:
            er, ec = i, line.index(Tile.END())
        if sr != -1 and er != -1:
            break

    # Dijkstra with turn cost, tracking all optimal predecessors
    score = math.inf
    opened = [(0, sr, sc, Direction.EAST)]
    
    visited = {(sr, sc, Direction.EAST): 0}
    predecessors = {}

    while opened:
        cost, r, c, d = heapq.heappop(opened)
        if cost > score: #visited.get((r, c, d)):
            break

        if (r, c) == (er, ec):
            score = min(score, cost)
            break

        # define combined moves: (nr, nc, nd, ncost)
        moves = []

        # move forward in current direction
        nr, nc = move_forward(r, c, d)
        if env[nr][nc] != Tile.WALL():
            moves.append((nr, nc, d, cost + 1))

        # rotate left + move
        nd = Direction((d.value - 1) % 4)
        nr, nc = move_forward(r, c, nd)
        if env[nr][nc] != Tile.WALL():
            moves.append((nr, nc, nd, cost + 1001))

        # rotate right + move
        nd = Direction((d.value + 1) % 4)
        nr, nc = move_forward(r, c, nd)
        if env[nr][nc] != Tile.WALL():
            moves.append((nr, nc, nd, cost + 1001))

        for nr, nc, nd, ncost in moves:
            current_best = visited.get((nr, nc, nd), math.inf)
            if ncost > current_best:
                continue
            if ncost < current_best:
                visited[(nr, nc, nd)] = ncost
                predecessors[(nr, nc, nd)] = set()
            predecessors[(nr, nc, nd)].add((r, c, d))
            heapq.heappush(opened, (ncost, nr, nc, nd))


    # --- Backtrack all optimal paths ---
    seats = set()
    stack = [(er, ec, d) for d in Direction if visited.get((er, ec, d)) == score]
    seen_states = set(stack)

    while stack:
        r, c, d = stack.pop()
        seats.add((r, c))
        for pr, pc, pd in predecessors.get((r, c, d), set()):
            if (pr, pc, pd) not in seen_states:
                seen_states.add((pr, pc, pd))
                stack.append((pr, pc, pd))

    print(f"\n# SOLUTION: {len(seats)} tiles are on at least one optimal path.\n")


if __name__ == "__main__":
    main()
