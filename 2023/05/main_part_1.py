
'''
Your puzzle answer was 173706076.

The first half of this puzzle is complete! It provides one gold star: *
'''

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils.read_file import read_file
from utils.test_solution import test_solution

import re

@test_solution(name="DAY 05 PART 1", runs=100)
def main():
    print("\n### DAY 05 PART 1 ###")

    content = read_file(os.path.join(os.path.dirname(__file__),"input.txt"))
    if not content: return

    seeds = list(map(int, re.findall(r"seeds: ([\d\s]+)\n\n", content)[0].split()))
    #print(f"seeds: {seeds}\n")

    seeds2location = [seed for seed in seeds]
    #print(f"seeds2location: {seeds2location}")

    #associations = {}
    seeds2soils = [list(map(int, soil.split())) for soil in re.findall(r"seed-to-soil map:\n([\d\s]+)\n\n", content)[0].split("\n")]
    #associations["s2s"] = {src + i: dst + i for dst, src, count in seeds2soils for i in range(count)}
    for i, seed in enumerate(seeds2location):
        for dst, src, count in seeds2soils:
            if src <= seed <= src + count:
                seeds2location[i] = seed + (dst - src)
                break
    
    #print(f"seeds2location: {seeds2location}")
    #print(f"associations[\"s2s\"]: {associations["s2s"]}\n")

    soils2fertilizers = [list(map(int, fertilizer.split())) for fertilizer in re.findall(r"soil-to-fertilizer map:\n([\d\s]+)\n\n", content)[0].split("\n")]
    #associations["s2f"] = {src + i: dst + i for dst, src, count in soils2fertilizers for i in range(count)}
    for i, seed in enumerate(seeds2location):
        for dst, src, count in soils2fertilizers:
            if src <= seed <= src + count:
                seeds2location[i] = seed + (dst - src)
                break
    
    #print(f"seeds2location: {seeds2location}")
    #print(f"associations[\"s2f\"]: {associations["s2f"]}\n")

    fertilizers2waters = [list(map(int, water.split())) for water in re.findall(r"fertilizer-to-water map:\n([\d\s]+)\n\n", content)[0].split("\n")]
    #associations["f2w"] = {src + i: dst + i for dst, src, count in fertilizers2waters for i in range(count)}
    for i, seed in enumerate(seeds2location):
        for dst, src, count in fertilizers2waters:
            if src <= seed <= src + count:
                seeds2location[i] = seed + (dst - src)
                break
    
    #print(f"seeds2location: {seeds2location}")
    #print(f"associations[\"f2w\"]: {associations["f2w"]}\n")

    waters2lights = [list(map(int, light.split())) for light in re.findall(r"water-to-light map:\n([\d\s]+)\n\n", content)[0].split("\n")]
    #associations["w2l"] = {src + i: dst + i for dst, src, count in waters2lights for i in range(count)}
    for i, seed in enumerate(seeds2location):
        for dst, src, count in waters2lights:
            if src <= seed <= src + count:
                seeds2location[i] = seed + (dst - src)
                break
    
    #print(f"seeds2location: {seeds2location}")
    #print(f"associations[\"w2l\"]: {associations["w2l"]}\n")

    lights2temperatures = [list(map(int, temperature.split())) for temperature in re.findall(r"light-to-temperature map:\n([\d\s]+)\n\n", content)[0].split("\n")]
    #associations["l2t"] = {src + i: dst + i for dst, src, count in lights2temperatures for i in range(count)}
    for i, seed in enumerate(seeds2location):
        for dst, src, count in lights2temperatures:
            if src <= seed <= src + count:
                seeds2location[i] = seed + (dst - src)
                break
    
    #print(f"seeds2location: {seeds2location}")
    #print(f"associations[\"l2t\"]: {associations["l2t"]}\n")

    temperatures2humiditys = [list(map(int, humidity.split())) for humidity in re.findall(r"temperature-to-humidity map:\n([\d\s]+)\n\n", content)[0].split("\n")]
    #associations["t2h"] = {src + i: dst + i for dst, src, count in temperatures2humiditys for i in range(count)}
    for i, seed in enumerate(seeds2location):
        for dst, src, count in temperatures2humiditys:
            if src <= seed <= src + count:
                seeds2location[i] = seed + (dst - src)
                break
    
    #print(f"seeds2location: {seeds2location}")
    #print(f"associations[\"t2h\"]: {associations["t2h"]}\n")

    humiditys2locations = [list(map(int, location.split())) for location in re.findall(r"humidity-to-location map:\n([\d\s]+)\n", content)[0].split("\n")]
    #associations["h2l"] = {src + i: dst + i for dst, src, count in humiditys2locations for i in range(count)}
    for i, seed in enumerate(seeds2location):
        for dst, src, count in humiditys2locations:
            if src <= seed <= src + count:
                seeds2location[i] = seed + (dst - src)
                break
    
    #print(f"seeds2location: {seeds2location}")
    #print(f"associations[\"h2l\"]: {associations["h2l"]}\n")

    min_location = min(seeds2location)
    
    print(f"\n# SOLUTION: lowest location number: {min_location}\n")

if __name__ == "__main__":
    main()