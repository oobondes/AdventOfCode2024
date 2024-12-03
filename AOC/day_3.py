#! /usr/bin/env python3
#solution for https://adventofcode.com/2024/day/3
from re import findall, match
def part_1_day_3(text:str):
    return sum((int(x)*int(y) for x,y in findall("mul\((\d+),(\d+)\)", text)))

def part_2_day_3(text:str):
    ans = 0

    # strip away newlines so the whole file is treated as one line
    text = text.replace('\n','')

    # findall all text strings that are not after "don't()"
    for subtext in findall(r"^.*?don't\(\)|do\(\).*?don't\(\)|do\(\).*?$|^.*?(?<!don't)$", text):
        ans += sum((int(x)*int(y) for x,y in findall("mul\((\d+),(\d+)\)", subtext)))
    return ans

