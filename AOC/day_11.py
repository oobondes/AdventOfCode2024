#! /usr/bin/env python3
# solution for https://adventofcode.com/2024/day/11
from functools import cache

@cache
def cycle(round_num: int, stone: int):
    if not round_num:
        return 1
    if stone == 0:
        return cycle(round_num - 1, 1)
    elif not len(str(stone)) & 1:
        stone_str = str(stone)
        half = len(stone_str) // 2
        return cycle(round_num - 1, int(stone_str[half:])) + cycle(round_num - 1, int(stone_str[:half]))
    else:
        return cycle(round_num - 1, stone * 2024)

def part_1_day_11(text: str):
    stones = list(map(int, text.split()))
    cycles = 25
    ans = 0
    for stone in stones:
        ans += cycle(cycles, stone)
    return ans


def part_2_day_11(text: str):
    stones = list(map(int, text.split()))
    cycles = 75
    ans = 0
    for stone in stones:
        ans += cycle(cycles, stone)
    return ans
