
'''
Your puzzle answer was 21607792.

Both parts of this puzzle are complete! They provide two gold stars: **
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file

def main():
    print("\n### DAY 01 PART 2 ###")

    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt"))
    if not content: return

    pairs = [pair.split("   ") for pair in content.split("\n")]
    pairs.pop()
    listA, listB = [list(map(int, i)) for i in zip(*pairs)]
    dictA = {key: listA.count(key) for key in listA}
    dictB = {key: listB.count(key) for key in listB}

    print("\nExample:")
    print(f"Dict A: {({key: dictA[key] for key in sorted(list(dictA))[:10]})}")
    print(f"Dict B: {({key: dictB[key] for key in sorted(list(dictB))[:10]})}")
    print(f"Similarities: {[key * dictA[key] * dictB[key] if key in dictB else 0 for key in sorted(list(dictA))[:10] ]}")
    print(f"Similarity score: {sum([key * dictA[key] * dictB[key] if key in dictB else 0 for key in sorted(list(dictA))[:10] ])}")
    
    similarityScore = sum([key * dictA[key] * dictB[key] if key in dictB else 0 for key in list(dictA)])
    print(f"\n# SOLUTION: Similarity score: {similarityScore}\n")

if __name__ == "__main__":
    main()