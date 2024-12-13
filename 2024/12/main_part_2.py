
'''
Your puzzle answer was 818286.

Both parts of this puzzle are complete! They provide two gold stars: **
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file
from utils.test_solution import test_solution

@test_solution(name="DAY 12 PART 2", runs=100)
def main():
    print("\n### DAY 12 PART 2 ###")

    neighbors = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt"))
    if not content: return

    field = [[*line] for line in content.split("\n")]
    nr, nc = len(field), len(field[0])
    #print(field)

    garden_plots = []
    visited = [["." for _ in range(nc) ] for _ in range(nr)]
    for r in range(nr):
        for c in range(nc):
            if visited[r][c] == ".":
                opened = [[r, c]]
                plant = field[r][c]
                garden_plots.append([0, set()])
                while opened:
                    [o_r, o_c] = opened.pop(0)
                    visited[o_r][o_c] = "x"
                    garden_plots[-1][0] += 1
                    for [dr, dc] in neighbors:
                        dr, dc = o_r + dr, o_c + dc
                        if 0 <= dr < nr and 0 <= dc < nc and field[dr][dc] == plant:
                            if visited[dr][dc] == ".":
                                visited[dr][dc] = "-"
                                opened.append([dr, dc])
                        else:
                            garden_plots[-1][1].add(tuple([o_r, o_c]))



    #for line in visited: print("".join(line))
    #print(f"garden_plots: {garden_plots}")

    area_edges = []
    for [area, garden_plot] in garden_plots:
        a_plot = list(garden_plot)[0]
        #print(a_plot)
        plant = field[a_plot[0]][a_plot[1]]
        [rows, cols] = map(set, [*zip(*garden_plot)])
        #print(f"garden_plot: {garden_plot}", rows, cols)
        
        area_edges.append([area, 0])
        for row in rows:
            [_, pcs] = [*zip(*sorted([plot for plot in garden_plot if plot[0] == row], key=lambda p: p[1]))]

            #print(f"row: {row}", pcs)
            countEdges = 0
            isNew = [True, True]
            prevC = pcs[0]
            for pc in pcs:
                if pc != prevC + 1:
                    isNew = [True, True]
                else:
                    if row-1 >= 0 and field[row-1][pc] == plant:
                        isNew[0] = True
                    if row+1 < nr and field[row+1][pc] == plant:
                        isNew[1] = True
                
                if isNew[0] and (row-1 < 0 or field[row-1][pc] != plant):
                    countEdges += 1
                    isNew[0] = False
                if isNew[1] and (row+1 >= nr or field[row+1][pc] != plant):
                    countEdges += 1
                    isNew[1] = False
                prevC = pc

            area_edges[-1][1] += countEdges
        
        for col in cols:
            [prs, _] = [*zip(*sorted([plot for plot in garden_plot if plot[1] == col], key=lambda p: p[0]))]

            #print(f"col: {col}", prs)
            countEdges = 0
            isNew = [True, True]
            prevR = prs[0]
            for pr in prs:
                if pr != prevR + 1:
                    isNew = [True, True]
                else:
                    if col-1 >= 0 and field[pr][col-1] == plant:
                        isNew[0] = True
                    if col+1 < nc and field[pr][col+1] == plant:
                        isNew[1] = True
                
                if isNew[0] and (col-1 < 0 or field[pr][col-1] != plant):
                    countEdges += 1
                    isNew[0] = False
                if isNew[1] and (col+1 >= nr or field[pr][col+1] != plant):
                    countEdges += 1
                    isNew[1] = False
                prevR = pr

            area_edges[-1][1] += countEdges


        
        for col in cols:
            pass
        
        
        #break

    #print(f"\edges: {area_edges}")
    
    total_cost = sum([a * e for [a, e] in area_edges])
    print(f"\n# SOLUTION: total price of fencing all regions: {total_cost}\n")

if __name__ == "__main__":
    main()