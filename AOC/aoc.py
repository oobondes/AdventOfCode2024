"""
This module manages the user data for
"""
#! /usr/bin/env python3
import requests
from pathlib import Path

class AOC:

    def __init__(self, year:int, token_file:str = ".token"):
        """gather year and user token for requests"""
        self.year = year
        self.token = Path(token_file).read_text().strip()
        self.folder = Path(str(year))
        self.folder.mkdir(exist_ok=True)

    def get_input(self, day:int):
        """gather input data for given day from adventofcode.com"""
        file = self.folder/f"day_{day}.txt"
        if file.exists():
            return file.read_text()
        headers = {"user-agent": "github.com/oobondes"}
        s = requests.Session()
        cookie = {"session": self.token}
        day = f"https://adventofcode.com/{self.year}/day/{day}/input"
        text =  s.get(day, cookies=cookie).content.decode().strip("\n")
        file.write_text(text)
        return text

    def submit_input(self, day: int, part: int, ans: str):
        """submits the AOC answer for the specified day"""
        s = requests.Session()
        cookie = {"session":self.token}
        submit_answer_url = f"https://adventofcode.com/{self.year}/day/{day}/answer"
        data = {"level": str(part), "answer": ans}
        resp = s.post(submit_answer_url.format(day), data=data, cookies=cookie)
        print(resp.text)
        if "day-success" in resp.text:
            print("success!")
        else:
            print("try again...")

    def get_leaderboards(self, group_id):
        headers = {"user-agent": "github.com/oobondes"}
        s = requests.Session()
        cookie = {"session": self.token}
        url = f"https://adventofcode.com/{self.year}/leaderboard/private/view/{group_id}.json"
        text =  s.get(url, cookies=cookie).content
        return text

    def get_all_inputs(self):
        """get all input files for a given year and write them to a file"""
        for day in range(1,26):
            text = self.get_input(day)

if __name__ == "__main__":
    aoc = AOC(2015)
    aoc.get_all_inputs()
