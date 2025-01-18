
'''
Your puzzle answer was 6431472344710.

Both parts of this puzzle are complete! They provide two gold stars: **
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file
from utils.test_solution import test_solution

@test_solution(name="DAY 09 PART 2", runs=10)
def main():
    print("\n### DAY 09 PART 2 ###")

    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt")).strip()
    if not content: return

    places = []
    idx = 0
    for i in range(0, len(content)-1, 2):
        [val, sp] = [*map(int, content[i:i+2])]

        places.append([True, val, idx])
        places.append([False, sp])
        
        idx += 1
    places.append([True, int(content[-1]), idx])

    i = len(places)-1
    while i >= 0:
        place = places[i]
        if not place[0]:
            i -= 1
            continue
        
        for j in range(i):
            tmp_place = places[j]
            if tmp_place[0]:
                continue

            if tmp_place[1] == place[1]:
                places[j] = [*place]
                places[i] = [False, place[1]]
                break
            elif tmp_place[1] > place[1]:
                places[j] = [*place]
                places[i] = [False, place[1]]
                places.insert(j+1, [False, tmp_place[1] - place[1]])
                i += 1
                break
        i -= 1

    pos = 0
    sumChecksum = 0
    for place in places:
        if place[0]:
            for _ in range(place[1]):
                sumChecksum += place[2]*pos
                pos += 1
        else:
            pos += place[1]

    print(f"\n# SOLUTION: filesystem checksum: {sumChecksum}\n")

if __name__ == "__main__":
    main()
