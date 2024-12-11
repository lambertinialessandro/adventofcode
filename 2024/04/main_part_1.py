
'''
Your puzzle answer was 2427.

The first half of this puzzle is complete! It provides one gold star: *
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file
from utils.test_solution import test_solution

from abc import ABC
import re

YELLOW = '\033[33m'
RESET = '\033[0m'

class text_iterator(ABC):
    name = "Text Iterator"
    current = 0
    end = 0
    text = ""

    def __str__(self):
        return self.name

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            value = self.text[self.current]
            self.current += 1
            return value
        else:
            raise StopIteration

class horizontal_iterator(text_iterator):
    name = "Horizontal Iterator"
    def __init__(self, text):
        self.current = 0
        self.end = len(text)

        self.text = text

class vertical_iterator(text_iterator):
    name = "Vertical Iterator"
    def __init__(self, text):
        self.current = 0

        newText = ["".join(chars) for chars in zip(*text)]
        self.end = len(newText)
        self.text = newText

class diagonal_p_iterator(text_iterator):
    name = "Primary Diagonal Iterator"
    def __init__(self, text):
        self.current = 0

        diagonals = {}
        for row_idx, row in enumerate(text):
            for col_idx, char in enumerate(row):
                diagonal_key = row_idx - col_idx
                if diagonal_key not in diagonals:
                    diagonals[diagonal_key] = ""
                diagonals[diagonal_key] += char
        
        newText = [diagonals[key] for key in sorted(diagonals.keys())]
        self.end = len(newText)
        self.text = newText

class diagonal_s_iterator(text_iterator):
    name = "Secondary Diagonal Iterator"
    def __init__(self, text):
        self.current = 0

        diagonals = {}
        for row_idx, row in enumerate(text):
            for col_idx, char in enumerate(row):
                diagonal_key = row_idx + col_idx
                if diagonal_key not in diagonals:
                    diagonals[diagonal_key] = ""
                diagonals[diagonal_key] += char
        
        newText = [diagonals[key] for key in sorted(diagonals.keys())]
        self.end = len(newText)
        self.text = newText

@test_solution(name="DAY 04 PART 1", runs=100)
def main():
    print("\n### DAY 04 PART 1 ###")

    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt"))
    if not content: return

    text = content.split("\n")

    iterators = [
        horizontal_iterator(text),
        vertical_iterator(text),
        diagonal_p_iterator(text),
        diagonal_s_iterator(text)
    ]

    exampleText = text[7][:35] + text[7][60:90]
    print("\nExample:")
    print(f"Line: {exampleText}")
    print(f"Number of XMAS (or SAMX) counted: {len(re.findall("XMAS", exampleText)) + len(re.findall("SAMX", exampleText))}")
    matches = re.finditer("XMAS|SAMX", exampleText)
    last_end = 0
    highlighted_line = ""
    for match in matches:
        highlighted_line += exampleText[last_end:match.start()] + YELLOW + match.group(0) + RESET
        last_end = match.end()
    highlighted_line += exampleText[last_end:]
    print(f"Line: {highlighted_line}")

    countWords = 0
    for i in iterators:
        currCount = 0
        for line in i:
            currCount += len(re.findall("XMAS", line)) + len(re.findall("SAMX", line))
        countWords += currCount
    
    print(f"\n# SOLUTION: Counted words: {countWords}\n")

if __name__ == "__main__":
    main()