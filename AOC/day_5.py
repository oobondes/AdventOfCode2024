#! /usr/bin/env python3
# solution for https://adventofcode.com/2024/day/5


def validate(num, order, updates):
    """check that the second element in any tuple in order does not precede an instance of the first, in updates"""
    for first, second in order:
        if num == first and second in updates:
            return True
    return False


def correct_order(updates: list, order):
    changed = True
    while changed:
        changed = False
        for first, second in order:
            if first in updates and second in updates and updates.index(first) > updates.index(second):
                idx = updates.index(first)
                idx2 = updates.index(second)
                updates[idx], updates[idx2] = updates[idx2], updates[idx]
                changed = True


def part_1_day_5(text: str):
    # separate the order mapping from the updates
    order, updates = text.split("\n\n")
    orders = list(tuple(map(int, line.strip().split("|"))) for line in order.split())
    ans = 0

    for update in (list(map(int, line.strip().split(","))) for line in updates.split()):
        # skip all that are not valid udpates
        if any((validate(num, orders, update[:idx]) for idx, num in enumerate(update))):
            continue
        ans += update[(len(update) // 2)]
    return ans


def part_2_day_5(text: str):
    # separate the order mapping from the updates
    order, updates = text.split("\n\n")
    orders = [tuple(map(int, line.strip().split("|"))) for line in order.split()]
    ans = 0

    for update in (list(map(int, line.strip().split(","))) for line in updates.split()):
        # find and fix invalid updates
        if any((validate(num, orders, update[:idx]) for idx, num in enumerate(update))):
            # reorder properly
            correct_order(update, orders)
            ans += update[(len(update) // 2)]
    return ans
