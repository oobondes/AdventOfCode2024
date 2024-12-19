#! /usr/bin/env python3
#solution for https://adventofcode.com/2024/day/19
from functools import cache

def get_valid_towels(towels, combo):
    return [towel for towel in towels if ''.join(towel) in ''.join(combo)]

def can_make(towels:list[str], combo:str):
    # base case
    if not combo:
        return True

    valid_towels = list(filter(lambda x: combo.startswith(x), towels))
    for towel in valid_towels:
        if can_make(towels, combo[len(towel):]):
            return True

    return False

def part_1_day_19(text:str):
    towels, combos = text.split('\n\n')
    towels = towels.split(', ')
    counts = [can_make(get_valid_towels(towels, combo), combo) for combo in combos]
    print(counts)
    return sum(counts)


@cache
def can_make_num(towels:tuple, combo:str):
    # base case
    if not combo:
        return 1
    ans = 0

    valid_towels = list(filter(lambda x: combo.startswith(x), towels))
    for towel in valid_towels:
        ans+= can_make_num(towels, combo[len(towel):])

    return ans

def part_2_day_19(text:str):
    towels, combos = text.split('\n\n')
    towels = towels.split(', ')
    combos = combos.split()
    ans = 0
    for combo in combos:
        print(combo)
        ans += can_make_num(tuple(towels), combo)
    return ans
