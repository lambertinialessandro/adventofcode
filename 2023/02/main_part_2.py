
'''
Your puzzle answer was 74804.

Both parts of this puzzle are complete! They provide two gold stars: **
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file
from utils.test_solution import test_solution

import re
    
@test_solution(name="DAY 02 PART 2", runs=100)
def main():
    print("\n### DAY 02 PART 2 ###")

    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt"))
    if not content: return
    
    # match = Game #number, a list of #number #color until ;
    games = re.findall(r"Game (\d+): ([\d\s\w,;]+)\n", content)

    print(f"Games: {games}")

    sum_possible_games = 0
    for game in games:
        [game_id, rounds] = game
        rounds = rounds.split("; ")
        
        max_cubes = {"red": 0, "green": 0, "blue": 0}
        for game_round in rounds:
            cubes = game_round.split(", ")
            for cube in cubes:
                [number, color] = cube.split(" ")
                if max_cubes[color] < int(number):
                    max_cubes[color] = int(number)
        else:
            print(max_cubes)
            mult = 1
            for color in max_cubes:
                mult *= max_cubes[color]
            sum_possible_games += mult


    print(f"\n# SOLUTION: {sum_possible_games}\n")

if __name__ == "__main__":
    main()