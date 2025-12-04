"""
@ Description:
    Start a problem for a specific year/day of the Advent of Code
    The AOC_SESSION environment variable must be set with the session cookie
    The USER_AGENT environment variable must be set
@ Parameters:
    year: Year of the Advent of Code
    day: Day of the Advent of Code
@ Return:
    Create 2 new files for the solution in the respective year/day folder
    

@ Example:
    create_solution 2015 01
"""

import os
import sys
import time
import re

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.read_file import read_file
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))

def create_solution(year, day):
    assert year.isdigit(), "Year must be a number"
    int_year = int(year)
    assert int_year >= 2015, "Doesn't exist a AoC before 2015"
    assert int_year <= time.localtime().tm_year, "Year must be less than or equal to the current year"


    assert day.isdigit(), "Day must be a number"
    int_day = int(day)
    assert 1 <= int_day <= 25, "Day must be between 1 and 25"
    if int_year == time.localtime().tm_year:
        assert time.localtime().tm_mon == 12, "It's not December yet"
        assert int_day <= time.localtime().tm_mday, "Day must be less than or equal to the current day"

    # Create the main_part_1.py file
    if not os.path.exists(os.path.join(os.path.dirname(__file__), "..", year, day, "main_part_1.py")):
        content = read_file(os.path.join(os.path.dirname(__file__),"template_main_part_1.txt"))
        content = re.sub(r"DAY ____ PART 1", f"DAY {day} PART 1", content)
        with open(os.path.join(os.path.dirname(__file__), "..", year, day, "main_part_1.py"), "w") as file:
            file.write(content)
        print("\033[92mFile main_part_1.py\033[0m created\n")
    else:
        print("\033[92mFile main_part_1.py\033[0m already exists\n")
    
    # Create the main_part_2.py file
    if not os.path.exists(os.path.join(os.path.dirname(__file__), "..", year, day, "main_part_2.py")):
        content = read_file(os.path.join(os.path.dirname(__file__),"template_main_part_2.txt"))
        content = re.sub(r"DAY ____ PART 2", f"DAY {day} PART 2", content)
        with open(os.path.join(os.path.dirname(__file__), "..", year, day, "main_part_2.py"), "w") as file:
            file.write(content)
        print("\033[92mFile main_part_2.py\033[0m created\n")
    else:
        print("\033[92mFile main_part_2.py\033[0m already exists\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("\nUsage: python create_solution.py <year> <day>")
        print("\t<year> must be a number between 2015 and the current year")
        print("\t<day> must be a number between 01 and 25 (always two digits)\n")
        sys.exit(1)

    year = sys.argv[1]
    day = sys.argv[2]

    create_solution(year, day)