
'''
Your puzzle answer was 4145.

Both parts of this puzzle are complete! They provide two gold stars: **
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file

def main():
    print("\n### DAY 05 PART 2 ###")

    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt"))
    if not content: return

    rules, updates = content.split("\n\n")
    rules = rules.split("\n")
    updates = [update.split(",") for update in updates.split("\n")[:-1]]

    pageRules = {}
    for rule in rules:
        page1, page2 = rule.split("|")
        if page1 not in pageRules.keys():
            pageRules[page1] = {"before": [], "after": []}
        if page2 not in pageRules.keys():
            pageRules[page2] = {"before": [], "after": []}
        pageRules[page1]["before"].append(page2) # this page (page1) must be before this list of pages
        pageRules[page2]["after"].append(page1) # this page (page2) must be after this list of pages
    
    for key in pageRules:
        pageRules[key]["before"] = sorted(pageRules[key]["before"])
        pageRules[key]["after"] = sorted(pageRules[key]["after"])
    
    sumMiddle = 0
    for pages in updates:
        hasBeenUpdated = False
        while True:
            isCorrect = True
            for i, page1 in enumerate(pages):
                for j, page2 in enumerate(pages[i+1:], i+1):
                    if page2 in pageRules[page1]["after"] or page1 in pageRules[page2]["before"]:
                        isCorrect = False
                        break
                if not isCorrect:
                    pages[i], pages[j] = pages[j], pages[i]
                    hasBeenUpdated = True
                    break
            if isCorrect:
                if hasBeenUpdated:
                    sumMiddle += int(pages[len(pages) // 2])
                break

    print(f"\n# SOLUTION: The sum of the middle pages of the fixed updates is: {sumMiddle}\n")

if __name__ == "__main__":
    main()