#! /usr/bin/env python3
# solution for https://adventofcode.com/2024/day/4


def x_mas_search(grid: list, x: int, y: int):
    """check is the current index is an A that is at the center of a "MAS" cross"""
    if grid[y][x] != "A" or x <= 0 or y <= 0:
        return False
    try:
        upper_left, upper_right, lower_left, lower_right = grid[y + 1][x - 1], grid[y + 1][x + 1], grid[y - 1][x - 1], grid[y - 1][x + 1]
        #  does the upper left corner to the lower corner spell "MAS"?                       does the upper right corner to the lower left corner spell "MAS"?
        if upper_left != lower_right and sorted([upper_left, lower_right]) == ["M", "S"] and upper_right != lower_left and sorted([upper_right, lower_left]) == ["M", "S"]:
            return True
        return False
    except IndexError:
        return False


def word_search(grid: list, word: str, x: int, y: int):
    """check if "word" exists at this index, going out in any one of the 8 possible directions"""
    length = len(word)
    total = 0
    for add_x, add_y in [(1, 1), (-1, 1), (1, -1), (-1, -1), (0, 1), (1, 0), (-1, 0), (0, -1)]:
        try:
            for idx in range(length):
                next_x = (add_x * idx) + x
                next_y = (add_y * idx) + y
                if grid[next_y][next_x] != word[idx] or 0 > next_x or 0 > next_y:
                    break
            else:
                total += 1
        except IndexError:
            continue
    return total


def part_1_day_4(text: str):
    grid = [list(line) for line in text.split()]
    ans = 0
    for length in range(len(grid[0])):
        for height in range(len(grid)):
            ans += word_search(grid, "XMAS", length, height)
    return ans


def part_2_day_4(text: str):
    grid = [list(line) for line in text.strip().split()]
    ans = 0
    for length in range(1, len(grid[0]) - 1):
        for height in range(1, len(grid) - 1):
            if x_mas_search(grid, length, height):
                ans += 1
    return ans
