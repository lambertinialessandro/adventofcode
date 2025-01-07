
"""
@ Description:
    Download the problem statement for a specific year/day of the Advent of Code
    The AOC_SESSION environment variable must be set with the session cookie
@ Parameters:
    year: Year of the Advent of Code
    day: Day of the Advent of Code
@ Return:
    Write the problem statement in the respective year/day folder

@ Example:
    download_problem 2015 01
"""

import os
import sys
import requests
import time

def download_input(year, day):

    assert os.getenv("AOC_SESSION"), "AOC_SESSION environment variable is not set"

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

    if not os.path.exists(os.path.join(os.path.dirname(__file__), "..", year, day, "input.txt")):
        session = requests.Session()
        session.cookies.set("session", os.getenv("AOC_SESSION"))
        response = session.get(f"https://adventofcode.com/{year}/day/{int_day}/input")

        if response.status_code == 200:
            os.makedirs(os.path.join(os.path.dirname(__file__), "..", year, day), exist_ok=True)
            with open(os.path.join(os.path.dirname(__file__), "..", year, day, "input.txt"), "w") as f:
                f.write(response.text)
            print(f"\033[94mInput file\033[0m for year {year} day {day} downloaded successfully\n")
        else:
            print(f"Failed to download \033[94minput file\033[0m for year {year} day {day}\n")
    else:
        print(f"\033[94mInput file\033[0m for year {year} day {day} already exists\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("\nUsage: python download_input.py <year> <day>")
        print("\t<year> must be a number between 2015 and the current year")
        print("\t<day> must be a number between 01 and 25 (always two digits)\n")
        sys.exit(1)

    year = sys.argv[1]
    day = sys.argv[2]

    download_input(year, day)
