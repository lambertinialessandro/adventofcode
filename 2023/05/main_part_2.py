
'''
Your puzzle answer was 11611182.

Both parts of this puzzle are complete! They provide two gold stars: **
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file
from utils.test_solution import test_solution

import re

@test_solution(name="DAY 05 PART 2", runs=100)
def main():
    print("\n### DAY 05 PART 2 ###")

    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt"))
    if not content: return

    seeds_combo = list(map(int, re.findall(r"seeds: ([\d\s]+)\n\n", content)[0].split()))
    seeds2location = []
    for i in range(0, len(seeds_combo), 2):
        seeds2location.append([seeds_combo[i], seeds_combo[i+1]])
    print(seeds2location)

    seeds2soils = [list(map(int, soil.split())) for soil in re.findall(r"seed-to-soil map:\n([\d\s]+)\n\n", content)[0].split("\n")]
    for i in range(len(seeds2location)):
        [seed, seed_count] = seeds2location[i]
        for dst, src, count in seeds2soils:
            is_lower_in = src <= seed < src + count
            is_upper_in = src <= seed + seed_count <= src + count

            if is_lower_in and is_upper_in:
                #print(f"is_lower_in: {is_lower_in}, is_upper_in: {is_upper_in}")
                #print(f"seed, seed_count: {seed, seed_count}")
                seeds2location[i] = [seed + (dst - src), seed_count]
                break
            elif is_lower_in:
                #print(f"is_lower_in: {is_lower_in}, is_upper_in: {is_upper_in}")
                #print(f"seed, seed_count: {seed, seed_count}")
                #print(f"dst, src, count: {dst, src, count}")
                count_included = count - (seed - src)
                seeds2location[i] = [seed + (dst - src), count_included]
                seeds2location.append([src + count, seed_count - count_included])
                break
            elif is_upper_in:
                #print(f"is_lower_in: {is_lower_in}, is_upper_in: {is_upper_in}")
                #print(f"seed, seed_count: {seed, seed_count}")
                #print(f"dst, src, count: {dst, src, count}")
                count_not_included = src - seed
                seeds2location[i] = [dst, seed_count - count_not_included]
                seeds2location.append([seed, count_not_included])
                break
    print(seeds2location)

    soils2fertilizers = [list(map(int, fertilizer.split())) for fertilizer in re.findall(r"soil-to-fertilizer map:\n([\d\s]+)\n\n", content)[0].split("\n")]
    print(f"soils2fertilizers: {soils2fertilizers}")
    for i in range(len(seeds2location)):
        [seed, seed_count] = seeds2location[i]
        for dst, src, count in soils2fertilizers:
            is_lower_in = src <= seed < src + count
            is_upper_in = src <= seed + seed_count <= src + count

            if is_lower_in and is_upper_in:
                print(f"is_lower_in: {is_lower_in}, is_upper_in: {is_upper_in}")
                print(f"seed, seed_count: {seed, seed_count}")
                seeds2location[i] = [seed + (dst - src), seed_count]
                break
            elif is_lower_in:
                print(f"is_lower_in: {is_lower_in}, src, seed, src + count: {src, seed, src + count}")
                print(f"is_upper_in: {is_upper_in}, src, seed + seed_count, src + count: {src, seed + seed_count, src + count}")
                print(f"seed, seed_count: {seed, seed_count}")
                print(f"dst, src, count: {dst, src, count}")
                count_included = count - (seed - src)
                seeds2location[i] = [seed + (dst - src), count_included]
                seeds2location.append([src + count, seed_count - count_included])
                break
            elif is_upper_in:
                print(f"is_lower_in: {is_lower_in}, is_upper_in: {is_upper_in}")
                print(f"seed, seed_count: {seed, seed_count}")
                #print(f"dst, src, count: {dst, src, count}")
                count_not_included = src - seed
                seeds2location[i] = [dst, seed_count - count_not_included]
                seeds2location.append([seed, count_not_included])
                break
    print(seeds2location)

    fertilizers2waters = [list(map(int, water.split())) for water in re.findall(r"fertilizer-to-water map:\n([\d\s]+)\n\n", content)[0].split("\n")]
    for i in range(len(seeds2location)):
        [seed, seed_count] = seeds2location[i]
        for dst, src, count in fertilizers2waters:
            is_lower_in = src <= seed < src + count
            is_upper_in = src <= seed + seed_count <= src + count

            if is_lower_in and is_upper_in:
                seeds2location[i] = [seed + (dst - src), seed_count]
                break
            elif is_lower_in:
                count_included = count - (seed - src)
                seeds2location[i] = [seed + (dst - src), count_included]
                seeds2location.append([src + count, seed_count - count_included])
                break
            elif is_upper_in:
                count_not_included = src - seed
                seeds2location[i] = [dst, seed_count - count_not_included]
                seeds2location.append([seed, count_not_included])
                break
    print(seeds2location)
    
    waters2lights = [list(map(int, light.split())) for light in re.findall(r"water-to-light map:\n([\d\s]+)\n\n", content)[0].split("\n")]
    for i in range(len(seeds2location)):
        [seed, seed_count] = seeds2location[i]
        for dst, src, count in waters2lights:
            is_lower_in = src <= seed < src + count
            is_upper_in = src <= seed + seed_count <= src + count

            if is_lower_in and is_upper_in:
                seeds2location[i] = [seed + (dst - src), seed_count]
                break
            elif is_lower_in:
                count_included = count - (seed - src)
                seeds2location[i] = [seed + (dst - src), count_included]
                seeds2location.append([src + count, seed_count - count_included])
                break
            elif is_upper_in:
                count_not_included = src - seed
                seeds2location[i] = [dst, seed_count - count_not_included]
                seeds2location.append([seed, count_not_included])
                break
    print(seeds2location)
    
    lights2temperatures = [list(map(int, temperature.split())) for temperature in re.findall(r"light-to-temperature map:\n([\d\s]+)\n\n", content)[0].split("\n")]
    for i in range(len(seeds2location)):
        [seed, seed_count] = seeds2location[i]
        for dst, src, count in lights2temperatures:
            is_lower_in = src <= seed < src + count
            is_upper_in = src <= seed + seed_count <= src + count

            if is_lower_in and is_upper_in:
                seeds2location[i] = [seed + (dst - src), seed_count]
                break
            elif is_lower_in:
                count_included = count - (seed - src)
                seeds2location[i] = [seed + (dst - src), count_included]
                seeds2location.append([src + count, seed_count - count_included])
                break
            elif is_upper_in:
                count_not_included = src - seed
                seeds2location[i] = [dst, seed_count - count_not_included]
                seeds2location.append([seed, count_not_included])
                break
    print(seeds2location)
    
    temperatures2humiditys = [list(map(int, humidity.split())) for humidity in re.findall(r"temperature-to-humidity map:\n([\d\s]+)\n\n", content)[0].split("\n")]
    for i in range(len(seeds2location)):
        [seed, seed_count] = seeds2location[i]
        for dst, src, count in temperatures2humiditys:
            is_lower_in = src <= seed < src + count
            is_upper_in = src <= seed + seed_count <= src + count

            if is_lower_in and is_upper_in:
                seeds2location[i] = [seed + (dst - src), seed_count]
                break
            elif is_lower_in:
                count_included = count - (seed - src)
                seeds2location[i] = [seed + (dst - src), count_included]
                seeds2location.append([src + count, seed_count - count_included])
                break
            elif is_upper_in:
                count_not_included = src - seed
                seeds2location[i] = [dst, seed_count - count_not_included]
                seeds2location.append([seed, count_not_included])
                break
    print(seeds2location)
    
    humiditys2locations = [list(map(int, location.split())) for location in re.findall(r"humidity-to-location map:\n([\d\s]+)\n", content)[0].split("\n")]
    for i in range(len(seeds2location)):
        [seed, seed_count] = seeds2location[i]
        for dst, src, count in humiditys2locations:
            is_lower_in = src <= seed < src + count
            is_upper_in = src <= seed + seed_count <= src + count

            if is_lower_in and is_upper_in:
                seeds2location[i] = [seed + (dst - src), seed_count]
                break
            elif is_lower_in:
                count_included = count - (seed - src)
                seeds2location[i] = [seed + (dst - src), count_included]
                seeds2location.append([src + count, seed_count - count_included])
                break
            elif is_upper_in:
                count_not_included = src - seed
                seeds2location[i] = [dst, seed_count - count_not_included]
                seeds2location.append([seed, count_not_included])
                break
    print(seeds2location)
    
    min_location = min(seeds2location, key=lambda x: x[0])
    
    print(f"\n# SOLUTION: {min_location[0]}\n")

if __name__ == "__main__":
    main()