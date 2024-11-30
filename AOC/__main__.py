from .aoc import AOC
from sys import argv

if len(argv) == 3 and argv[1].lower() in ("-g", "--generate-file"):
    from pathlib import Path
    print("generating template files now")
    year = int(argv[2])
    aoc_dir = Path("AOC")
    for day in range(1,25):
        file = aoc_dir/f"day_{day}.py"
        file.write_text(f"#! /usr/bin/env python3\n"
                        f"#solution for https://adventofcode.com/{year}/day/{day}"
                        f"\n"
                        f"def part_1_day_{day}(text:str):\n"
                        f"    return None\n"
                        f"\n"
                        f"def part_2_day_{day}(text:str):\n"
                        f"    return None\n"
                        f"\n"
                        )

    print("files generated")

if len(argv) != 2:
    print("provide a year to grab input files from")
else:
    aoc = AOC(int(argv[1]))
    aoc.get_all_inputs()
