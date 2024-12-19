#! /usr/bin/env python3
#solution for https://adventofcode.com/2024/day/18
from queue import PriorityQueue
def part_1_day_18(text:str):
    width, height = 0, 0
    walls = list()
    # find all walls and size of grid
    for x,y in list(map(lambda x: map(int,x.split(',')), text.strip().split()))[:1024]:
        if x > width:
            width = x
        if y > height:
            height = y
        walls.append((x,y))
    grid = [['#' if (x,y) in walls else '.' for x in range(width+1)] for y in range(height+1)]
    cost_grid = [[9999999999999 for x in range(width+1)] for y in range(height+1)]

    print('\n'.join((''.join(line) for line in grid)))

    start = (0,0)
    end = (width, height)

    to_search = PriorityQueue()
    to_search.put((0, start, set()))
    ans = -1
    while not to_search.empty():
        score, point, visited = to_search.get()
        visited.add(point)
        x,y = point
        next_score = score+1
        for add_x, add_y in ((0,-1),(0,1),(1,0),(-1,0)):
            next_x, next_y = x+add_x, y+add_y
            if  0 <= next_x <= width and 0 <= next_y <= height and next_score < cost_grid[next_y][next_x] and (next_x, next_y) not in visited and grid[next_y][next_x] != '#':
                cost_grid[next_y][next_x] = next_score
                if (next_x, next_y) == end:
                    ans = next_score
                    return ans
                to_search.put(( score+1, (next_x,next_y),visited.copy()))

    return ans


def part_2_day_18(text:str):
    width, height = 0, 0
    cutoff = 1024
    walls = list(map(lambda x: tuple(map(int,x.split(','))), text.strip().split()))
    # find all walls and size of grid
    for x,y in walls[:cutoff]:
        if x > width:
            width = x
        if y > height:
            height = y
        walls.append((x,y))
    grid = [['#' if (x,y) in walls[:cutoff] else '.' for x in range(width+1)] for y in range(height+1)]
    cost_grid = [[9999999999999 for x in range(width+1)] for y in range(height+1)]

    print('\n'.join((''.join(line) for line in grid)))

    start = (0,0)
    end = (width, height)


    print(cutoff)
    print(walls)
    for wall in walls[cutoff:]:
        cost_grid = [[9999999999999 for x in range(width+1)] for y in range(height+1)]
        to_search = PriorityQueue()
        to_search.put((0, start, set()))
        x,y = wall
        if x >= width or y >= height:
            pass
        grid[y][x] = '#'
        found = False
        while not to_search.empty():
            score, point, visited = to_search.get()
            visited.add(point)
            x,y = point
            next_score = score+1
            for add_x, add_y in ((0,-1),(0,1),(1,0),(-1,0)):
                next_x, next_y = x+add_x, y+add_y
                if  0 <= next_x <= width and 0 <= next_y <= height and next_score < cost_grid[next_y][next_x] and (next_x, next_y) not in visited and grid[next_y][next_x] != '#':
                    cost_grid[next_y][next_x] = next_score
                    if (next_x, next_y) == end:
                        found = True
                        break
                    to_search.put(( score+1, (next_x,next_y),visited.copy()))
            if found:
                break
        # return if this iteration did not find the end
        if not found:
            return ','.join(map(str,wall))


    return -1

