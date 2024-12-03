#! /usr/bin/env python3
#solution for https://adventofcode.com/2024/day/2
from itertools import combinations
def is_safe(levels:list):
    """ ensures all numbers in the list are either increasing, or decreasing
    and that all numeric changes are within 1-3 difference of the preceeding number"""
    inc = levels[0] < levels[1]
    for i, num in enumerate(levels[:-1]):
        diff = levels[i+1] - num
        if (inc and diff < 0) or (not inc and diff > 0):
            return False
        if not 0 < abs(diff) <= 3:
            return False
    return True

def part_1_day_2(text:str):
    level_lists = [list(map(int,line.split())) for line in text.split('\n')]
    return sum((is_safe(levels) for levels in level_lists))


def part_2_day_2(text:str):
    level_lists = [list(map(int,line.split())) for line in text.split('\n')]
    ans = 0
    for level in level_lists:
        for combo in combinations(level,len(level)-1):
            if is_safe(combo):
                ans += 1
                break
    return ans


