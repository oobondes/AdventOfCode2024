#! /usr/bin/env python3
#solution for https://adventofcode.com/2024/day/16
from queue import PriorityQueue

def solve_maze(grid:list[list[str]], pos: tuple[int, int], turning = False):
    x,y = pos
    if grid[y][x] == 'E':
        return 1


def part_1_day_16(text:str):
    NORTH, SOUTH, EAST, WEST = (0,-1), (0,1), (1,0), (-1,0)
    directions = {SOUTH: (SOUTH,WEST,EAST),
                  NORTH: (NORTH,WEST,EAST),
                  EAST: (EAST, SOUTH,NORTH),
                  WEST: (WEST, SOUTH,NORTH),
                  }
    turn = {SOUTH: (EAST, WEST),
            NORTH: (EAST, WEST),
            EAST: (NORTH, SOUTH),
            WEST: (NORTH, SOUTH)
            }

    grid = [list(line) for line in text.split('\n')]
    cost_grid = [[9999999999999 for _ in line] for line in grid]
    start = (-1,-1)

    for y in range(len(grid)):
        if 'S' in grid[y]:
            start = (grid[y].index('S'), y)
    q = PriorityQueue()
    #      score, pos, direction, visited
    q.put((0, start, EAST, tuple()))
    lowest = 99999999999999999

    while q.qsize() != 0:
        score, pos, direction, visited = q.get()
        visited = (*visited, pos)
        if score > lowest:
            continue
        x,y = pos
        if grid[y][x] == 'E':
            lowest = score
        if grid[y][x] == '#':
            continue
        for next_direction in directions[direction]:
            add_score = 1
            if next_direction != direction:
                add_score += 1000
            next_x = x + next_direction[0]
            next_y = y + next_direction[1]
            new_score = add_score + score
            if new_score < cost_grid[next_y][next_x] and (next_x, next_y) not in visited:
                cost_grid[next_y][next_x] = new_score
                q.put((score + add_score, (next_x, next_y), next_direction, visited))
    return lowest

def part_2_day_16(text:str):
    NORTH, SOUTH, EAST, WEST = (0,-1), (0,1), (1,0), (-1,0)
    directions = {SOUTH: (SOUTH,WEST,EAST),
                  NORTH: (NORTH,WEST,EAST),
                  EAST: (EAST, SOUTH,NORTH),
                  WEST: (WEST, SOUTH,NORTH),
                  }
    turn = {SOUTH: (EAST, WEST),
            NORTH: (EAST, WEST),
            EAST: (NORTH, SOUTH),
            WEST: (NORTH, SOUTH)
            }

    grid = [list(line) for line in text.split('\n')]
    cost_grid = [[99999999999 for _ in line] for line in grid]
    start = (-1,-1)

    for y in range(len(grid)):
        if 'S' in grid[y]:
            start = (grid[y].index('S'), y)
    q = PriorityQueue()
    #      score, pos, direction, visited
    q.put((0, start, EAST, tuple()))
    lowest = 9999999999999999999
    good_seats = set()
    iteration = 0

    while q.qsize() != 0:
        score, pos, direction, visited = q.get()
        visited = (*visited, pos)
        if score > lowest:
            continue
        iteration += 1
        if not iteration%1000:
            print(pos)
        x,y = pos
        if grid[y][x] == 'E':
            if score > lowest:
                continue
            elif score < lowest:
                lowest = score
                good_seats = set(visited)
            else:
                good_seats = good_seats.union(set(visited))
        if grid[y][x] == '#':
            print("wall")
            continue
        for next_direction in directions[direction]:
            add_score = 1
            if next_direction != direction:
                add_score += 1000
            next_x = x + next_direction[0]
            next_y = y + next_direction[1]
            new_score = add_score + score
            #                                         +1000 to buffer for turns
            if new_score <= cost_grid[next_y][next_x] + 1000 and (next_x, next_y) not in visited:
                cost_grid[next_y][next_x] = new_score
                q.put((new_score, (next_x, next_y), next_direction, visited))
    return len(good_seats)

