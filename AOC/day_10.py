#! /usr/bin/env python3
#solution for https://adventofcode.com/2024/day/10
from itertools import combinations

def trail_score(grid:list,next_step:int, x:int, y:int, ends:set):
	if not (0<= x < len(grid[0])) or not (0<= y < len(grid)):
		return False
	if grid[y][x] != next_step:
		return False
	if next_step == 9:
		ends.add((x,y))
		return True
	return sum((trail_score(grid, next_step+1, x + x_add, y + y_add, ends) for x_add, y_add in ((1,0), (-1,0), (0,1), (0,-1))))

def part_1_day_10(text:str):
	grid = [list(map(int,line)) for line in text.split()]
	ans = 0
	for y in range(len(grid)):
		for x in range(len(grid[0])):
			ends = set()
			trail_score(grid, 0, x, y, ends)
			ans += len(ends)
	return ans

def part_2_day_10(text:str):
	grid = [list(map(int,line)) for line in text.split()]
	ans = 0
	for y in range(len(grid)):
		for x in range(len(grid[0])):
			ans += trail_score(grid, 0, x, y, set())
	return ans

