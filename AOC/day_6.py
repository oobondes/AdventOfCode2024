#! /usr/bin/env python3
#solution for https://adventofcode.com/2024/day/6
# 2080 is too high
# not 2007
#TODO: 1930 is too low for gmail account
from pprint import pprint

turns = {(0,-1):(1,0), (1,0):(0,1), (0,1):(-1,0), (-1,0):(0,-1)}

def forward(cur_pos, direction):
    return cur_pos[0] + direction[0], cur_pos[1] + direction[1]

def part_1_day_6(text:str):
    grid = list()
    start = tuple()
    for y, line in enumerate(text.split()):
        grid.append(list(line))
        if '^' in grid[-1]:
            start = (grid[-1].index('^'), y)
    direction = (0,-1)
    visited = set()

    cur_pos = start
    while True:
        visited.add(cur_pos)
        next_pos = forward(cur_pos, direction)
        if (not 0 <= next_pos[1] < len(grid)) or (not 0 <= next_pos[0] < len(grid[0])):
            break
        while grid[next_pos[1]][next_pos[0]]== '#':
            direction = turns[direction]
            next_pos = forward(cur_pos, direction)
        cur_pos = next_pos

    return len(visited)

def can_loop(grid, cur_pos, direction, visited):
    """infinite loop detection"""
    while True:
        if (direction, cur_pos) in visited:
            return True
        visited.add((direction, cur_pos))
        next_pos = forward(cur_pos, direction)
        if (not 0 <= next_pos[1] < len(grid)) or (not 0 <= next_pos[0] < len(grid[0])):
            break
        while grid[next_pos[1]][next_pos[0]] == '#':
            direction = turns[direction]
            next_pos = forward(cur_pos, direction)
        cur_pos = next_pos
    return False

def part_2_day_6(text:str):
    grid = list()
    start = tuple()
    for y, line in enumerate(text.split()):
        grid.append(list(line))
        if '^' in grid[-1]:
            start = (grid[-1].index('^'), y)

    direction = (0,-1)
    visited = set()
    cur_pos = start
    while True:
        visited.add(cur_pos)
        next_pos = forward(cur_pos, direction)
        if (not 0 <= next_pos[1] < len(grid)) or (not 0 <= next_pos[0] < len(grid[0])):
            break
        while grid[next_pos[1]][next_pos[0]]== '#':
            direction = turns[direction]
            next_pos = forward(cur_pos, direction)
        cur_pos = next_pos

    ans = 0
    for x,y in visited:
        grid[y][x] = '#'
        if can_loop(grid, start, (0,-1), set()):
            ans += 1
        grid[y][x] = '.'
    return ans
