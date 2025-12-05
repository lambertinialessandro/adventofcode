"""
@ Description:
    Generate a progress bar string based on a given percentage.
    The function takes a completion percentage and returns a visual
    representation of progress using a textual bar.
@ Parameters:
    persentage: Completion percentage (0-100).
@ Return:
    A string representing the progress bar.

@ Example:
    generate_progress_bar 10
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.enum import SmartEnum

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))


class Progress(SmartEnum):
    five = "█"
    four = "▓"
    three = "▓"
    two = "▒"
    one = "▒"
    zero = "░"


progress_map = {
    5: Progress.five,
    4: Progress.four,
    3: Progress.three,
    2: Progress.two,
    1: Progress.one,
    0: Progress.zero,
}


def generate_progress_bar(persentage):
    assert persentage.isdigit(), "Year must be a number"
    int_persentage = int(persentage)
    assert 0 <= int_persentage <= 100, "persentage must be between 0 and 100"
    
    full = int_persentage // 5
    rest = int_persentage % 5

    progress_bar = Progress.five() * full
    if rest > 0:
        progress_bar += progress_map[rest]()
        
    missing_bars = 100 // 5 - len(progress_bar)
    progress_bar += Progress.zero() * (missing_bars)

    return progress_bar


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("\nUsage: python generate_progress_bar.py <persentage>")
        print("\t<persentage> must be a number between 0 and 100")
        sys.exit(1)

    persentage = sys.argv[1]
    
    progress_bar = generate_progress_bar(persentage)
    print(f"{" "*(3-len(persentage))}{persentage}%: {progress_bar}")

    #for persentage in range(0, 101):
    #    progress_bar = generate_progress_bar(str(persentage))
    #    print(f"{" "*(3-len(str(persentage)))}{persentage}%: {progress_bar}")
