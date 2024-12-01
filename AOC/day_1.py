#! /usr/bin/env python3
#solution for https://adventofcode.com/2024/day/1
def part_1_day_1(text:str):
    nums = [int(num) for num in text.split()]
    left = sorted(nums[::2])
    right = sorted(nums[1::2])
    return sum((abs(x-y) for x,y in zip(left,right)))

def part_2_day_1(text:str):
    nums = [int(num) for num in text.split()]
    left = sorted(nums[::2])
    right = sorted(nums[1::2])
    return sum((x * right.count(x) for x in left))

