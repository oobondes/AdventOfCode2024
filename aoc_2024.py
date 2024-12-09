#! /usr/bin/env python3
from AOC.aoc import AOC
import argparse
from pathlib import Path

def get_input(aoc: AOC, b_online: bool, day: int):
    if b_online:
        return aoc.get_input(day)
    else:
        file = Path(f"day_{day}.txt")
        if file.exists():
            return file.read_text().strip()

def day(num):
    if not 0 < int(num) < 26:
        raise ValueError("not a valid day")
    return int(num)

parser = argparse.ArgumentParser(__file__)
parser.add_argument("day", type=int, nargs="+", help="sets the day to be ran")
parser.add_argument("-o", "--online", action="store_true", help="this flag causes the script to pull the input from the website. Otherwise, it will use dayX.txt as input.")
parser.add_argument("-s", "--submit", action="store_true", help="this flag will submit the answer generated to advent of code.")
parser.add_argument("-1", "--part_one", action="store_true", help="run the first part of the puzzle")
parser.add_argument("-2", "--part_two", action="store_true", help="run the second part of the puzzle")
args = parser.parse_args()

if not args.part_two:
    args.part_one = True

aoc = AOC(2024)

if 1 in args.day and args.part_one:
    day = 1
    from AOC.day_1 import part_1_day_1
    text = get_input(aoc, args.online, day)
    ans = part_1_day_1(text)
    if not ans is None:
        if args.submit:
            aoc.submit_input(day, 1, ans)
        print(ans)
    else:
        print("day 1 part 1 not complete")

if 1 in args.day and args.part_two:
    day = 1
    from AOC.day_1 import part_2_day_1
    text = get_input(aoc, args.online, day)
    ans = part_2_day_1(text)
    if not ans is None:
        if args.submit:
            print(aoc.submit_input(day, 2, ans))
        print(ans)
    else:
        print("day 1 part 2 not complete")

if 2 in args.day and args.part_one:
    day = 2
    from AOC.day_2 import part_1_day_2
    text = get_input(aoc, args.online, day)
    ans = part_1_day_2(text)
    if not ans is None:
        if args.submit:
            print(aoc.submit_input(day, 1, ans))
        print(ans)
    else:
        print("day 2 part 1 not complete")

if 2 in args.day and args.part_two:
    day = 2
    from AOC.day_2 import part_2_day_2
    text = get_input(aoc, args.online, day)
    ans = part_2_day_2(text)
    if not ans is None:
        if args.submit:
            print(aoc.submit_input(day, 2, ans))
        print(ans)
    else:
        print("day 2 part 2 not complete")

if 3 in args.day and args.part_one:
    day = 3
    from AOC.day_3 import part_1_day_3
    text = get_input(aoc, args.online, day)
    ans = part_1_day_3(text)
    if not ans is None:
        if args.submit:
            print(aoc.submit_input(day, 1, ans))
        print(ans)
    else:
        print("day 3 part 1 not complete")

if 3 in args.day and args.part_two:
    day = 3
    from AOC.day_3 import part_2_day_3
    text = get_input(aoc, args.online, day)
    ans = part_2_day_3(text)
    if not ans is None:
        if args.submit:
            print(aoc.submit_input(day, 2, ans))
        print(ans)
    else:
        print("day 3 part 2 not complete")

if 4 in args.day and args.part_one:
    day = 4
    from AOC.day_4 import part_1_day_4
    text = get_input(aoc, args.online, day)
    ans = part_1_day_4(text)
    if not ans is None:
        if args.submit:
            print(aoc.submit_input(day, 1, ans))
        print(ans)
    else:
        print("day 4 part 1 not complete")

if 4 in args.day and args.part_two:
    day = 4
    from AOC.day_4 import part_2_day_4
    text = get_input(aoc, args.online, day)
    ans = part_2_day_4(text)
    if not ans is None:
        if args.submit:
            print(aoc.submit_input(day, 2, ans))
        print(ans)
    else:
        print("day 4 part 2 not complete")

if 5 in args.day and args.part_one:
    day = 5
    from AOC.day_5 import part_1_day_5
    text = get_input(aoc, args.online, day)
    ans = part_1_day_5(text)
    if not ans is None:
        if args.submit:
            print(aoc.submit_input(day, 1, ans))
        print(ans)
    else:
        print("day 5 part 1 not complete")

if 5 in args.day and args.part_two:
    day = 5
    from AOC.day_5 import part_2_day_5
    text = get_input(aoc, args.online, day)
    ans = part_2_day_5(text)
    if not ans is None:
        if args.submit:
            print(aoc.submit_input(day, 2, ans))
        print(ans)
    else:
        print("day 5 part 2 not complete")

if 6 in args.day and args.part_one:
    day = 6
    from AOC.day_6 import part_1_day_6
    text = get_input(aoc, args.online, day)
    ans = part_1_day_6(text)
    if not ans is None:
        if args.submit:
            print(aoc.submit_input(day, 1, ans))
        print(ans)
    else:
        print("day 6 part 1 not complete")

if 6 in args.day and args.part_two:
    day = 6
    from AOC.day_6 import part_2_day_6
    text = get_input(aoc, args.online, day)
    ans = part_2_day_6(text)
    if not ans is None:
        if args.submit:
            print(aoc.submit_input(day, 2, ans))
        print(ans)
    else:
        print("day 6 part 2 not complete")

if 7 in args.day and args.part_one:
    day = 7
    from AOC.day_7 import part_1_day_7
    text = get_input(aoc, args.online, day)
    ans = part_1_day_7(text)
    if not ans is None:
        if args.submit:
            print(aoc.submit_input(day, 1, ans))
        print(ans)
    else:
        print("day 7 part 1 not complete")

if 7 in args.day and args.part_two:
    day = 7
    from AOC.day_7 import part_2_day_7
    text = get_input(aoc, args.online, day)
    ans = part_2_day_7(text)
    if not ans is None:
        if args.submit:
            print(aoc.submit_input(day, 2, ans))
        print(ans)
    else:
        print("day 7 part 2 not complete")

if 8 in args.day and args.part_one:
    day = 8
    from AOC.day_8 import part_1_day_8
    text = get_input(aoc, args.online, day)
    ans = part_1_day_8(text)
    if not ans is None:
        if args.submit:
            print(aoc.submit_input(day, 1, ans))
        print(ans)
    else:
        print("day 8 part 1 not complete")

if 8 in args.day and args.part_two:
    day = 8
    from AOC.day_8 import part_2_day_8
    text = get_input(aoc, args.online, day)
    ans = part_2_day_8(text)
    if not ans is None:
        if args.submit:
            print(aoc.submit_input(day, 2, ans))
        print(ans)
    else:
        print("day 8 part 2 not complete")

if 9 in args.day and args.part_one:
    day = 9
    from AOC.day_9 import part_1_day_9
    text = get_input(aoc, args.online, day)
    ans = part_1_day_9(text)
    if not ans is None:
        if args.submit:
            print(aoc.submit_input(day, 1, ans))
        print(ans)
    else:
        print("day 9 part 1 not complete")

if 9 in args.day and args.part_two:
    day = 9
    from AOC.day_9 import part_2_day_9
    text = get_input(aoc, args.online, day)
    ans = part_2_day_9(text)
    if not ans is None:
        if args.submit:
            print(aoc.submit_input(day, 2, ans))
        print(ans)
    else:
        print("day 9 part 2 not complete")

if 10 in args.day and args.part_one:
    day = 10
    from AOC.day_10 import part_1_day_10
    text = get_input(aoc, args.online, day)
    ans = part_1_day_10(text)
    if not ans is None:
        if args.submit:
            print(aoc.submit_input(day, 1, ans))
        print(ans)
    else:
        print("day 10 part 1 not complete")

if 10 in args.day and args.part_two:
    day = 10
    from AOC.day_10 import part_2_day_10
    text = get_input(aoc, args.online, day)
    ans = part_2_day_10(text)
    if not ans is None:
        if args.submit:
            print(aoc.submit_input(day, 2, ans))
        print(ans)
    else:
        print("day 10 part 2 not complete")

if 11 in args.day and args.part_one:
    day = 11
    from AOC.day_11 import part_1_day_11
    text = get_input(aoc, args.online, day)
    ans = part_1_day_11(text)
    if not ans is None:
        if args.submit:
            print(aoc.submit_input(day, 1, ans))
        print(ans)
    else:
        print("day 11 part 1 not complete")

if 11 in args.day and args.part_two:
    day = 11
    from AOC.day_11 import part_2_day_11
    text = get_input(aoc, args.online, day)
    ans = part_2_day_11(text)
    if not ans is None:
        if args.submit:
            print(aoc.submit_input(day, 2, ans))
        print(ans)
    else:
        print("day 11 part 2 not complete")

if 12 in args.day and args.part_one:
    day = 12
    from AOC.day_12 import part_1_day_12
    text = get_input(aoc, args.online, day)
    ans = part_1_day_12(text)
    if not ans is None:
        if args.submit:
            print(aoc.submit_input(day, 1, ans))
        print(ans)
    else:
        print("day 12 part 1 not complete")

if 12 in args.day and args.part_two:
    day = 12
    from AOC.day_12 import part_2_day_12
    text = get_input(aoc, args.online, day)
    ans = part_2_day_12(text)
    if not ans is None:
        if args.submit:
            print(aoc.submit_input(day, 2, ans))
        print(ans)
    else:
        print("day 12 part 2 not complete")

if 13 in args.day and args.part_one:
    day = 13
    from AOC.day_13 import part_1_day_13
    text = get_input(aoc, args.online, day)
    ans = part_1_day_13(text)
    if not ans is None:
        if args.submit:
            print(aoc.submit_input(day, 1, ans))
        print(ans)
    else:
        print("day 13 part 1 not complete")

if 13 in args.day and args.part_two:
    day = 13
    from AOC.day_13 import part_2_day_13
    text = get_input(aoc, args.online, day)
    ans = part_2_day_13(text)
    if not ans is None:
        if args.submit:
            print(aoc.submit_input(day, 2, ans))
        print(ans)
    else:
        print("day 13 part 2 not complete")

if 14 in args.day and args.part_one:
    day = 14
    from AOC.day_14 import part_1_day_14
    text = get_input(aoc, args.online, day)
    ans = part_1_day_14(text)
    if not ans is None:
        if args.submit:
            print(aoc.submit_input(day, 1, ans))
        print(ans)
    else:
        print("day 14 part 1 not complete")

if 14 in args.day and args.part_two:
    day = 14
    from AOC.day_14 import part_2_day_14
    text = get_input(aoc, args.online, day)
    ans = part_2_day_14(text)
    if not ans is None:
        if args.submit:
            print(aoc.submit_input(day, 2, ans))
        print(ans)
    else:
        print("day 14 part 2 not complete")

if 15 in args.day and args.part_one:
    day = 15
    from AOC.day_15 import part_1_day_15
    text = get_input(aoc, args.online, day)
    ans = part_1_day_15(text)
    if not ans is None:
        if args.submit:
            print(aoc.submit_input(day, 1, ans))
        print(ans)
    else:
        print("day 15 part 1 not complete")

if 15 in args.day and args.part_two:
    day = 15
    from AOC.day_15 import part_2_day_15
    text = get_input(aoc, args.online, day)
    ans = part_2_day_15(text)
    if not ans is None:
        if args.submit:
            print(aoc.submit_input(day, 2, ans))
        print(ans)
    else:
        print("day 15 part 2 not complete")

if 16 in args.day and args.part_one:
    day = 16
    from AOC.day_16 import part_1_day_16
    text = get_input(aoc, args.online, day)
    ans = part_1_day_16(text)
    if not ans is None:
        if args.submit:
            print(aoc.submit_input(day, 1, ans))
        print(ans)
    else:
        print("day 16 part 1 not complete")

if 16 in args.day and args.part_two:
    day = 16
    from AOC.day_16 import part_2_day_16
    text = get_input(aoc, args.online, day)
    ans = part_2_day_16(text)
    if not ans is None:
        if args.submit:
            print(aoc.submit_input(day, 2, ans))
        print(ans)
    else:
        print("day 16 part 2 not complete")

if 17 in args.day and args.part_one:
    day = 17
    from AOC.day_17 import part_1_day_17
    text = get_input(aoc, args.online, day)
    ans = part_1_day_17(text)
    if not ans is None:
        if args.submit:
            print(aoc.submit_input(day, 1, ans))
        print(ans)
    else:
        print("day 17 part 1 not complete")

if 17 in args.day and args.part_two:
    day = 17
    from AOC.day_17 import part_2_day_17
    text = get_input(aoc, args.online, day)
    ans = part_2_day_17(text)
    if not ans is None:
        if args.submit:
            print(aoc.submit_input(day, 2, ans))
        print(ans)
    else:
        print("day 17 part 2 not complete")

if 18 in args.day and args.part_one:
    day = 18
    from AOC.day_18 import part_1_day_18
    text = get_input(aoc, args.online, day)
    ans = part_1_day_18(text)
    if not ans is None:
        if args.submit:
            print(aoc.submit_input(day, 1, ans))
        print(ans)
    else:
        print("day 18 part 1 not complete")

if 18 in args.day and args.part_two:
    day = 18
    from AOC.day_18 import part_2_day_18
    text = get_input(aoc, args.online, day)
    ans = part_2_day_18(text)
    if not ans is None:
        if args.submit:
            print(aoc.submit_input(day, 2, ans))
        print(ans)
    else:
        print("day 18 part 2 not complete")

if 19 in args.day and args.part_one:
    day = 19
    from AOC.day_19 import part_1_day_19
    text = get_input(aoc, args.online, day)
    ans = part_1_day_19(text)
    if not ans is None:
        if args.submit:
            print(aoc.submit_input(day, 1, ans))
        print(ans)
    else:
        print("day 19 part 1 not complete")

if 19 in args.day and args.part_two:
    day = 19
    from AOC.day_19 import part_2_day_19
    text = get_input(aoc, args.online, day)
    ans = part_2_day_19(text)
    if not ans is None:
        if args.submit:
            print(aoc.submit_input(day, 2, ans))
        print(ans)
    else:
        print("day 19 part 2 not complete")

if 20 in args.day and args.part_one:
    day = 20
    from AOC.day_20 import part_1_day_20
    text = get_input(aoc, args.online, day)
    ans = part_1_day_20(text)
    if not ans is None:
        if args.submit:
            print(aoc.submit_input(day, 1, ans))
        print(ans)
    else:
        print("day 20 part 1 not complete")

if 20 in args.day and args.part_two:
    day = 20
    from AOC.day_20 import part_2_day_20
    text = get_input(aoc, args.online, day)
    ans = part_2_day_20(text)
    if not ans is None:
        if args.submit:
            print(aoc.submit_input(day, 2, ans))
        print(ans)
    else:
        print("day 20 part 2 not complete")

if 21 in args.day and args.part_one:
    day = 21
    from AOC.day_21 import part_1_day_21
    text = get_input(aoc, args.online, day)
    ans = part_1_day_21(text)
    if not ans is None:
        if args.submit:
            print(aoc.submit_input(day, 1, ans))
        print(ans)
    else:
        print("day 21 part 1 not complete")

if 21 in args.day and args.part_two:
    day = 21
    from AOC.day_21 import part_2_day_21
    text = get_input(aoc, args.online, day)
    ans = part_2_day_21(text)
    if not ans is None:
        if args.submit:
            print(aoc.submit_input(day, 2, ans))
        print(ans)
    else:
        print("day 21 part 2 not complete")

if 22 in args.day and args.part_one:
    day = 22
    from AOC.day_22 import part_1_day_22
    text = get_input(aoc, args.online, day)
    ans = part_1_day_22(text)
    if not ans is None:
        if args.submit:
            print(aoc.submit_input(day, 1, ans))
        print(ans)
    else:
        print("day 22 part 1 not complete")

if 22 in args.day and args.part_two:
    day = 22
    from AOC.day_22 import part_2_day_22
    text = get_input(aoc, args.online, day)
    ans = part_2_day_22(text)
    if not ans is None:
        if args.submit:
            print(aoc.submit_input(day, 2, ans))
        print(ans)
    else:
        print("day 22 part 2 not complete")

if 23 in args.day and args.part_one:
    day = 23
    from AOC.day_23 import part_1_day_23
    text = get_input(aoc, args.online, day)
    ans = part_1_day_23(text)
    if not ans is None:
        if args.submit:
            print(aoc.submit_input(day, 1, ans))
        print(ans)
    else:
        print("day 23 part 1 not complete")

if 23 in args.day and args.part_two:
    day = 23
    from AOC.day_23 import part_2_day_23
    text = get_input(aoc, args.online, day)
    ans = part_2_day_23(text)
    if not ans is None:
        if args.submit:
            print(aoc.submit_input(day, 2, ans))
        print(ans)
    else:
        print("day 23 part 2 not complete")


if 24 in args.day and args.part_one:
    day = 24
    from AOC.day_24 import part_1_day_24
    text = get_input(aoc, args.online, day)
    ans = part_1_day_24(text)
    if not ans is None:
        if args.submit:
            print(aoc.submit_input(day, 1, ans))
        print(ans)
    else:
        print("day 24 part 1 not complete")

if 24 in args.day and args.part_two:
    day = 24
    from AOC.day_24 import part_2_day_24
    text = get_input(aoc, args.online, day)
    ans = part_2_day_24(text)
    if not ans is None:
        if args.submit:
            print(aoc.submit_input(day, 2, ans))
        print(ans)
    else:
        print("day 24 part 2 not complete")


if 25 in args.day and args.part_one:
    day = 25
    from AOC.day_25 import part_1_day_25
    text = get_input(aoc, args.online, day)
    ans = part_1_day_25(text)
    if not ans is None:
        if args.submit:
            print(aoc.submit_input(day, 1, ans))
        print(ans)
    else:
        print("day 25 part 1 not complete")

if 25 in args.day and args.part_two:
    day = 25
    from AOC.day_25 import part_2_day_25
    text = get_input(aoc, args.online, day)
    ans = part_2_day_25(text)
    if not ans is None:
        if args.submit:
            print(aoc.submit_input(day, 2, ans))
        print(ans)
    else:
        print("day 25 part 2 not complete")

