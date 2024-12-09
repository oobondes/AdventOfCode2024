#! /usr/bin/env python3
# solution for https://adventofcode.com/2024/day/9
def checksum(nums: list[int]):
    return sum((i * num for i, num in enumerate(nums)))


def part_1_day_9(text: str):
    disk = list()
    id_num = 0

    # parse the file
    for idx, num in enumerate(map(int, text.strip())):
        if idx & 1:
            disk.extend(list("." * num))
        else:
            disk.extend((id_num for _ in range(num)))
            id_num += 1

    # fit the high ID files chunks into empty space at the beginning
    for i in range(len(disk) - 1, -1, -1):
        if type(disk[i]) == int:
            idx = disk.index(".")
            if idx >= 0 and idx < i:
                disk[idx] = disk.pop(i)
            else:
                break

    # strip the "." at the end
    disk = disk[: disk.index(".")]

    return checksum(disk)


class Disk:
    """represent the space a file takes up on space, the amount of free space that follows it,
    and the ID number of the file"""

    def __init__(self, ID, length, free_space):
        self.ID = ID
        self.length = length
        self.free_space = free_space

    def __repr__(self):
        return f"{self.ID}-{self.length}-{self.free_space}"

    def __str__(self):
        return f"{self.ID}-{self.length}-{self.free_space}"


def part_2_day_9(text: str):
    disk = list()
    id_num = 0
    # parse the file into Disk objects
    for idx, num in enumerate(map(int, text.strip())):
        if idx & 1:
            disk[-1].free_space = num
        else:
            disk.append(Disk(id_num, num, 0))
            id_num += 1

    idx = len(disk) - 1
    while idx > 0:
        for file_idx, file in enumerate(disk[:idx]):
            if file.free_space >= disk[idx].length:
                mv_file = disk.pop(idx)
                disk[idx - 1].free_space += mv_file.length + mv_file.free_space
                mv_file.free_space = file.free_space - mv_file.length
                file.free_space = 0
                disk.insert(file_idx + 1, mv_file)
                break
        else:
            # only decrement index if for loop finishes
            idx -= 1

    # calculate checksum
    checksum = 0
    idx = 0
    for file in disk:
        for _ in range(file.length):
            checksum += file.ID * idx
            idx += 1
        idx += file.free_space

    return checksum
