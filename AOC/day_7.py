#! /usr/bin/env python3
# solution for https://adventofcode.com/2024/day/7


def solve(total: int, calibration: int, nums: list[int]):
    """recursively find if any combination of addition and multiplication of the list can procude total"""
    if not nums and total == calibration:
        return total
    if not nums or calibration > total:
        return
    if add := solve(total, calibration + nums[0], nums[1:]):
        return add
    elif mul := solve(total, calibration * nums[0], nums[1:]):
        return mul
    return False


def solve2(total: int, calibration: int, nums: list[int]):
    """recursively find if any combination of addition, multiplication, and concatination of the list can procude total"""
    if not nums and total == calibration:
        return total
    if not nums or calibration > total:
        return
    if pipe := solve2(total, int(f"{calibration}{nums[0]}"), nums[1:]):
        return pipe
    if add := solve2(total, calibration + nums[0], nums[1:]):
        return add
    if mul := solve2(total, calibration * nums[0], nums[1:]):
        return mul
    return False


def part_1_day_7(text: str):
    ans = 0
    for line in text.split("\n"):
        total, nums = line.split(": ")
        solution = solve(int(total), 0, list(map(int, nums.split())))
        if solution:
            ans += solution
    return ans


def part_2_day_7(text: str):
    ans = 0
    for line in text.split("\n"):
        total, nums = line.split(": ")
        solution = solve2(int(total), 0, list(map(int, nums.split())))
        if solution:
            ans += solution
    return ans
