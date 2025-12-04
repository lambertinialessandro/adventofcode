"""
@ Description:
    Start a problem for a specific year/day of the Advent of Code
    The AOC_SESSION environment variable must be set with the session cookie
    The USER_AGENT environment variable must be set
@ Parameters:
    year: Year of the Advent of Code
    day: Day of the Advent of Code
@ Return:
    Write the problem statement in the respective year/day folder.
    Create 2 new files for the solution.

@ Example:
    start_problem 2015 01
"""

import os
import sys
import time
from dotenv import load_dotenv

load_dotenv()

from download_input import download_input
from download_problem import download_problem
from create_solution import create_solution

def start_problem(year, day):
    assert os.getenv("AOC_SESSION"), "AOC_SESSION environment variable is not set"
    assert os.getenv("USER_AGENT"), "USER_AGENT environment variable is not set"

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
    
    print(f"\n --::@ Problem {int_year} {int_day} at https://adventofcode.com/{int_year}/day/{int_day}\n")

    try:
        download_input(year, day)
    except:
        print("\033[91mError\033[0m while downloading input file\n")

    try:
        download_problem(year, day)
    except:
        print("\033[91mError\033[0m while downloading problem files\n")

    try:
        create_solution(year, day)
    except:
        print("\033[91mError\033[0m while downloading problem files\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("\nUsage: python start_problem.py <year> <day>")
        print("\t<year> must be a number between 2015 and the current year")
        print("\t<day> must be a number between 01 and 25 (always two digits)\n")
        sys.exit(1)

    year = sys.argv[1]
    day = sys.argv[2]

    start_problem(year, day)