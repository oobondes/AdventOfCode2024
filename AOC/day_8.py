#! /usr/bin/env python3
#solution for https://adventofcode.com/2024/day/8
from collections import defaultdict

def part_1_day_8(text:str):
	antinodes = set()
	grid = [list(line.strip()) for line in text.split()]
	height = len(grid)
	width = len(grid[0])
	letters = defaultdict(list)
	for y in range(height):
		for x in range(width):
			if grid[y][x] != '.':
				letters[grid[y][x]].append((x,y))
	for letter, coordinates in letters.items():
		for i in range(len(coordinates)):
			x,y = coordinates[i]
			for x2, y2 in coordinates[i+1:]:
				x_diff = x - x2
				y_diff = y - y2
				if 0 <= x_diff + x < width and 0 <= y_diff + y < height:
					antinodes.add((x_diff + x, y_diff + y))
				if 0 <= -x_diff + x2 < width and 0 <= -y_diff + y2 < height:
					antinodes.add((-x_diff + x2, -y_diff + y2))
	return len(antinodes)
				

def part_2_day_8(text:str):
	antinodes = set()
	grid = [list(line.strip()) for line in text.split()]
	height = len(grid)
	width = len(grid[0])
	letters = defaultdict(list)
	for y in range(height):
		for x in range(width):
			if grid[y][x] != '.':
				letters[grid[y][x]].append((x,y))
	for letter, coordinates in letters.items():
		for i in range(len(coordinates)):
			x,y = coordinates[i]
			antinodes.add((x,y))
			for x2, y2 in coordinates[i+1:]:
				x_diff = x - x2
				y_diff = y - y2
				temp_x = x + x_diff
				temp_y = y + y_diff
				while 0 <= temp_x < width and 0 <= temp_y < height:
					antinodes.add((temp_x, temp_y))
					temp_x += x_diff
					temp_y += y_diff
				temp_x = x2 - x_diff
				temp_y = y2 - y_diff
				while 0 <= temp_x < width and 0 <= temp_y < height:
					antinodes.add((temp_x, temp_y))
					temp_x -= x_diff
					temp_y -= y_diff
	return len(antinodes)

