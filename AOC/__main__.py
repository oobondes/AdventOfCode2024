from .aoc import AOC
from sys import argv
from datetime import datetime
from json import loads


if len(argv) == 3 and argv[1].lower() in ("-g", "--generate-file"):
    from pathlib import Path

    print("generating template files now")
    year = int(argv[2])
    aoc_dir = Path("AOC")
    for day in range(1, 25):
        file = aoc_dir / f"day_{day}.py"
        file.write_text(
            f"#! /usr/bin/env python3\n"
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
elif len(argv) == 4 and argv[1].lower() in ("--board", "-b"):
    year = int(argv[2])
    aoc = AOC(year)
    group_id = int(argv[3])
    data = aoc.get_leaderboards(group_id)
    data = loads(data)
    for member, member_data in sorted( data["members"].items(), key=lambda x: (x[1].get("local_score"), x[0]), reverse=True,):
        name = member_data.get("name", member) or member
        print(f"{name} ({member_data.get('local_score')})")
        for day, day_data in sorted(member_data["completion_day_level"].items(), key=lambda x: x[0]):
            part_1_time = datetime.fromtimestamp(int(day_data.get("1", {}).get("get_star_ts", 0xFFFFFFFF)))
            part_2_time = day_data.get("2", {}).get("get_star_ts")
            time_to_complete = None
            if part_2_time:
                part_2_time = datetime.fromtimestamp(int(part_2_time))
                time_to_complete = part_2_time - part_1_time
                print(f"\t{day:0>2}: {part_1_time:%F %T} - {part_2_time:%F %T}\n\t\telapsed time:{(part_2_time - part_1_time).seconds} seconds")
            else:
                print(f"\t{day:0>2}: {part_1_time:%F %T} - N/A")
        print("==================================")
elif len(argv) != 2:
    print("provide a year to grab input files from")
else:
    aoc = AOC(int(argv[1]))
    aoc.get_all_inputs()
