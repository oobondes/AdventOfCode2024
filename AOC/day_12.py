#! /usr/bin/env python3
# solution for https://adventofcode.com/2024/day/12
def area_perimeter(grid: list, plant: str, x: int, y: int, visited: set):
    """find the area that plant takes up in grid, and returns that with the parameter"""
    if (x, y) in visited:
        return 0, 0
    visited.add((x, y))
    perimeter = 0
    area = 1
    for x2, y2 in ((0, 1), (0, -1), (-1, 0), (1, 0)):
        x2, y2 = x + x2, y + y2
        if not (0 <= x2 < len(grid[0])) or not (0 <= y2 < len(grid)):
            perimeter += 1
            continue
        if grid[y2][x2] == plant:
            a, p = area_perimeter(grid, plant, x2, y2, visited)
            perimeter += p
            area += a
        else:
            perimeter += 1
    return area, perimeter


def part_1_day_12(text: str):
    grid = [list(line) for line in text.split()]
    visited = set()
    ans = 0
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            area, perimeter = area_perimeter(grid, grid[y][x], x, y, visited)
            ans += area * perimeter
    return ans


def count_solid_walls(grid: list, points: set, letter: str):
    """shoots a line through and determines where a section of outside wall is of the given letter"""
    x_max = max(map(lambda x: x[0], points))
    x_min = min(map(lambda x: x[0], points))
    y_max = max(map(lambda x: x[1], points))
    y_min = min(map(lambda x: x[1], points))
    num_walls = 0

    # find vertical wall count
    for x in range(x_min, x_max + 1):
        awall = False
        bwall = False
        for y in range(y_min, y_max + 1):
            if not awall and (x, y) in points and (x == 0 or grid[y][x - 1] != letter):
                num_walls += 1
                awall = True
            elif awall and ((x, y) not in points or (x and grid[y][x - 1] == letter)):
                awall = False

            if not bwall and (x, y) in points and (x == len(grid[0]) - 1 or grid[y][x + 1] != letter):
                num_walls += 1
                bwall = True
            elif bwall and ((x, y) not in points or (x < len(grid[0]) - 1 and grid[y][x + 1] == letter)):
                bwall = False

    # find horizontal wall count
    for y in range(y_min, y_max + 1):
        awall = False
        bwall = False
        for x in range(x_min, x_max + 1):
            if not awall and (x, y) in points and (y == 0 or grid[y - 1][x] != letter):
                num_walls += 1
                awall = True
            elif awall and ((x, y) not in points or (y and grid[y - 1][x] == letter)):
                awall = False

            if not bwall and (x, y) in points and (y == len(grid) - 1 or grid[y + 1][x] != letter):
                num_walls += 1
                bwall = True
            elif bwall and ((x, y) not in points or (y < len(grid) - 1 and grid[y + 1][x] == letter)):
                bwall = False
    return num_walls


def part_2_day_12(text: str):
    grid = [list(line) for line in text.split()]
    visited = set()
    ans = 0
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            if (x, y) not in visited:
                letter_visited = set()
                area, _ = area_perimeter(grid, grid[y][x], x, y, letter_visited)
                visited = visited.union(letter_visited)
                perimeter = count_solid_walls(grid, letter_visited, grid[y][x])
                ans += area * perimeter
    return ans
