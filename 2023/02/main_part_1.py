
'''
Your puzzle answer was 2317.

The first half of this puzzle is complete! It provides one gold star: *
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file
from utils.test_solution import test_solution

import re

#@test_solution(name="DAY 02 PART 1", runs=100)
def main():
    print("\n### DAY 02 PART 1 ###")

    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt"))
    if not content: return
    
    # match = Game #number, a list of #number #color until ;
    games = re.findall(r"Game (\d+): ([\d\s\w,;]+)\n", content)

    print(f"Games: {games}")

    cubes_count = {"red": 12, "green": 13, "blue": 14}

    sum_possible_games = 0
    for game in games:
        [game_id, rounds] = game
        rounds = rounds.split("; ")
        
        for game_round in rounds:
            cubes = game_round.split(", ")

            for cube in cubes:
                [number, color] = cube.split(" ")
                if cubes_count[color] < int(number):
                    print(f"\nGame: {game_id}")
                    print(f"\tRound: {game_round}")
                    print(f"\t\tCube: {cube}")
                    print(f"\t\t\tCube {cube} is not possible")
                    break
            else:
                continue
            break
        else:
            sum_possible_games += int(game_id)


    print(f"\n# SOLUTION: {sum_possible_games}\n")

if __name__ == "__main__":
    main()