#! /usr/bin/env python3
#solution for https://adventofcode.com/2024/day/15
def next_pos(start, move):
    """ add 2 tuples of coordinates together """
    return start[0] + move[0], start[1] + move[1]

def push_stone(start:tuple[int, int], direction:tuple[int, int], grid:list):
    """ moves a line of stones in direction (+/-x,+/-y) so long as there is no wall at the end of them
    returns true if no wall was hit
    """
    end = start
    while grid[end[1]][end[0]] == 'O':
        end = next_pos(end, direction)
    if grid[end[1]][end[0]] != '#':
        grid[start[1]][start[0]], grid[end[1]][end[0]] = grid[end[1]][end[0]], grid[start[1]][start[0]]
        # did not hit a wall
        return True
    # hit a wall
    return False

def part_1_day_15(text:str):
    directions = {'<':(-1,0), '>':(1,0), 'v':(0,1), '^':(0,-1)}
    grid, moves = text.split('\n\n')
    moves = moves.replace('\n','')
    grid = [list(line) for line in grid.split()]
    pos = None
    x = 0
    for y, line in enumerate(grid):
        if '@' in line:
            x = line.index('@')
            pos = (x,y)
            break

    # make movements
    for move in moves:
        x,y = next_pos(directions[move],pos)
        cur_x, cur_y = pos
        if grid[y][x] == '.':
            grid[cur_y][cur_x], grid[y][x] = grid[y][x], grid[cur_y][cur_x]
            pos = (x,y)
        elif grid[y][x] == '#':
            continue
        elif grid[y][x] == 'O':
            if (push_stone((x,y), directions[move], grid)):
                grid[cur_y][cur_x], grid[y][x] = grid[y][x], grid[cur_y][cur_x]
                pos = (x,y)
    # add up total scores of rocks
    ans = 0
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            if grid[y][x] == 'O':
                ans += (100*y) + x
    return ans

def can_move(x,y, direction, grid):
    """determine if a piece of a box can move up/down"""
    if grid[y][x] == '#':
        return False
    if grid[y][x] == '.':
        return True
    if grid[y][x] == ']':
        return can_move(*next_pos((x,y), direction), direction, grid) and can_move(*next_pos(((x-1),y),direction), direction, grid)
    if grid[y][x] == '[':
        return can_move(*next_pos((x,y), direction), direction, grid) and can_move(*next_pos(((x+1),y),direction), direction, grid)
    return False

def move(x,y, direction, grid):
    """ moves a set of boxes (that take up two spaces) up or down """
    x_next, y_next = next_pos((x,y), direction)
    # This can be the base case because it will only be called if no walls are involved
    if grid[y][x] == '.':
        return
    # recurse so boxes further down are moved out of the way for this one
    move(*next_pos((x,y),direction), direction, grid)
    letter = grid[y][x] # save the letter value before it is changed
    grid[y][x], grid[y_next][x] = grid[y_next][x], grid[y][x]
    if letter == ']':
        move(x-1, y, direction, grid)
    if letter == '[':
        move(x+1, y, direction, grid)


def push_big_stone_vertical(start, direction, grid):
    if can_move(*start, direction, grid):
        move(*start, direction, grid)
        return True
    return False

def push_big_stone_sideways(start:tuple[int, int], direction:tuple[int, int], grid:list):
    end = start
    while grid[end[1]][end[0]] in '[]':
        end = next_pos(end, direction)
    if grid[end[1]][end[0]] != '#':
        rev_dir = (-direction[0], direction[1])
        mid = next_pos(end,rev_dir)
        while end != start:
            grid[mid[1]][mid[0]], grid[end[1]][end[0]] = grid[end[1]][end[0]], grid[mid[1]][mid[0]]
            end = next_pos(end, rev_dir)
            mid = next_pos(end,rev_dir)
        # did not hit a wall
        return True
    # hit a wall
    return False

def part_2_day_15(text:str):
    directions = {'<':(-1,0), '>':(1,0), 'v':(0,1), '^':(0,-1)}
    grid, moves = text.split('\n\n')
    moves = moves.replace('\n','')
    grid = grid.replace("#", "##").replace('O','[]').replace('.','..').replace('@','@.')
    grid = [list(line) for line in grid.split()]
    pos = None
    x = 0
    for y, line in enumerate(grid):
        if '@' in line:
            x = line.index('@')
            pos = (x,y)
            break

    # move boxes around
    for move in moves:
        x,y = next_pos(directions[move],pos)
        cur_x, cur_y = pos
        if grid[y][x] == '.':
            grid[cur_y][cur_x], grid[y][x] = grid[y][x], grid[cur_y][cur_x]
            pos = (x,y)
        elif grid[y][x] == '#':
            continue
        elif grid[y][x] in '[]':
            if (move in '<>' and push_big_stone_sideways((x,y), directions[move], grid)) or (move in 'v^' and push_big_stone_vertical((x,y), directions[move], grid)):
                grid[cur_y][cur_x], grid[y][x] = grid[y][x], grid[cur_y][cur_x]
                pos = (x,y)

    # score box positions
    ans = 0
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            if grid[y][x] == '[':
                ans += (100*y) + x
    return ans

