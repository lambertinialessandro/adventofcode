
"""
@ Description:
    Download the problem statement for a specific year/day of the Advent of Code
    The AOC_SESSION environment variable must be set with the session cookie
    The USER_AGENT environment variable must be set
@ Parameters:
    year: Year of the Advent of Code
    day: Day of the Advent of Code
@ Return:
    Write the problem statement in the respective year/day folder

@ Example:
    download_problem 2015 01
"""

import os
import re
import sys
import time
import requests
from dotenv import load_dotenv

load_dotenv()

def download_problem(year, day):
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

    if not os.path.exists(os.path.join(os.path.dirname(__file__), "..", year, day, "problem_part_1.txt")) \
        or not os.path.exists(os.path.join(os.path.dirname(__file__), "..", year, day, "problem_part_2.txt")):
        session = requests.Session()
        session.cookies.set("session", os.getenv("AOC_SESSION"))
        session.headers.update({"User-Agent": os.getenv("USER_AGENT")})
        response = session.get(f"https://adventofcode.com/{year}/day/{int_day}")

        if response.status_code == 200:
            main_content = re.search(r"<main>(.*?)</main>", response.text, re.DOTALL)

            if main_content:
                main_text = main_content.group(1)
        
                formatted_text = re.sub(r"<h2.*?>(.*?)</h2>", r"\1\n\n", main_text)
                formatted_text = re.sub(r"<p.*?>(.*?)</p>", r"\1\n\n", formatted_text)
                
                formatted_text = re.sub(r"<.*?>", "", formatted_text)
                formatted_text = re.sub(r"\s+\n", "\n", formatted_text).strip()

                part_one = None
                part_two = None
                if "--- Part Two" in formatted_text:
                    part_one = re.findall(r"(--- Day.*?)Your puzzle answer was", formatted_text, re.DOTALL)[0]

                    if "Answer:" in formatted_text:
                        part_two = re.findall(r"(--- Part Two.*?)Answer:", formatted_text, re.DOTALL)[0]
                    elif "You don't have enough stars" in formatted_text:
                        # TODO: maybe is better to set part_two = None
                        part_two = re.findall(r"(--- Part Two.*?)You don't have enough stars", formatted_text, re.DOTALL)[0]
                    elif formatted_text.count("Your puzzle answer was") == 2:
                        part_two = re.findall(r"(--- Part Two.*?)Your puzzle answer was", formatted_text, re.DOTALL)[0]
                    else:
                        part_two = re.findall(r"(--- Part Two.*?)Both parts of this puzzle are complete!", formatted_text, re.DOTALL)[0]
                else:
                    part_one = re.findall(r"(--- Day.*?)To begin, get your puzzle input", formatted_text, re.DOTALL)[0]

                if not os.path.exists(os.path.join(os.path.dirname(__file__), "..", year, day, "problem_part_1.txt")):
                    os.makedirs(os.path.join(os.path.dirname(__file__), "..", year, day), exist_ok=True)
                    with open(os.path.join(os.path.dirname(__file__), "..", year, day, "problem_part_1.txt"), "w") as f:
                        f.write(part_one)
                    print(f"\033[93mPart 1 file\033[0m for year {year} day {day} downloaded successfully\n")
                else:
                    print(f"\033[93mPart 1 file\033[0m for year {year} day {day} already exists\n")

                if not os.path.exists(os.path.join(os.path.dirname(__file__), "..", year, day, "problem_part_2.txt")):
                    if part_two:
                        with open(os.path.join(os.path.dirname(__file__), "..", year, day, "problem_part_2.txt"), "w") as f:
                            f.write(part_two)
                        print(f"\033[93mPart 2 file\033[0m for year {year} day {day} downloaded successfully\n")
                    else:
                        print(f"\033[93mPart 2 file\033[0m for year {year} day {day} not found, the first part is still to be solved\n")
                else:
                    print(f"\033[93mPart 2 file\033[0m for year {year} day {day} already exists\n")

        else:
            print(f"Failed to download \033[93mproblem text file\033[0m for year {year} day {day}\n")
    else:
        print(f"Both \033[93mproblem text files\033[0m for year {year} day {day} already exists\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("\nUsage: python download_problem.py <year> <day>")
        print("\t<year> must be a number between 2015 and the current year")
        print("\t<day> must be a number between 01 and 25 (always two digits)\n")
        sys.exit(1)

    year = sys.argv[1]
    day = sys.argv[2]

    download_problem(year, day)
