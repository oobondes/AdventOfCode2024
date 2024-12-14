#! /usr/bin/env python3
#solution for https://adventofcode.com/2024/day/14
from re import findall

def part_1_day_14(text:str):
    height = 103
    width = 101
    seconds = 100
    coordinates = list()
    i  = 0
    for x,y,x_v,y_v in findall(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", text):
        #print(x,y)
        x = (int(x) + (seconds*int(x_v)))%width
        y = (int(y) + (seconds*int(y_v)))%height
        coordinates.append((x,y))
        i+=1
    x_half = width//2
    y_half = height//2
    first_quad = sum(map(lambda coord: coord[0] < x_half and coord[1] > y_half, coordinates))
    second_quad = sum(map(lambda coord: coord[0] > x_half and coord[1] > y_half, coordinates))
    third_quad = sum(map(lambda coord: coord[0] < x_half and coord[1] < y_half, coordinates))
    fourth_quad = sum(map(lambda coord: coord[0] > x_half and coord[1] < y_half, coordinates))
    return first_quad * second_quad * third_quad * fourth_quad


def part_2_day_14(text:str):
    height = 103
    width = 101
    seconds = 1
    i  = 10
    vectors = findall(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", text)
    while seconds < 100000:
        coordinates = list()
        grid = [['.' for _ in range(width)] for __ in range(height)]
        for x,y,x_v,y_v in findall(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", text):
            #print(x,y)
            x = (int(x) + (seconds*int(x_v)))%width
            y = (int(y) + (seconds*int(y_v)))%height
            grid[y][x] = '#'
            coordinates.append((x,y))
        # check for the tree boarder and exit if found
        if any(("###########################" in ''.join(line) for line in grid)):
            print('\n'.join((''.join(line) for line in grid)))
            print(f"{seconds} seconds")
            break
        seconds += 1

    return seconds

