#! /usr/bin/env python3
#solution for https://adventofcode.com/2024/day/17

#this is not right
#5,5,3,6,4,2,7,0,2

from math import trunc
class three_bit:
    def __init__(self, A, B, C, instructions):
        self.A = A
        self.B = B
        self.C = C
        self.instructions = instructions
        self.expected = [_ for _ in instructions]
        self.output = ""
        self.idx = 0

    def combo(self, operand):
        if operand == 4:
            return self.A
        if operand == 5:
            return self.B
        if operand == 6:
            return self.C
        if operand == 7:
            raise Exception("help")
        return operand

    def adv(self, operand):
        operand = self.combo(operand)
        self.A = trunc(self.A / (2**operand))
        self.idx += 2

    def r_adv(self, operand):
        operand = self.combo(operand)
        temp = (2**operand) * self.A

        if operand == 4:
            self.A = temp
        elif operand == 5:
            self.B = temp
        elif operand == 6:
            self.C = temp
        self.idx -= 2

    def bxl(self, operand):
        self.B = self.B ^ operand
        self.idx += 2

    def r_bxl(self, operand):
        self.B = self.B ^ operand
        self.idx -= 2

    def bst(self, operand):
        operand = self.combo(operand)
        self.B = operand % 8
        self.idx += 2

    def r_bst(self, operand):
        if operand == 4:
            self.A = operand
        elif operand == 6:
            self.C = operand
        else:
            self.B = operand
        self.idx -= 2

    def jnz(self, operand):
        if self.A:
            self.idx = operand
        else:
            self.idx += 2

    def r_jnz(self, operand):
        self.idx -= 2

    def bxc(self, operand):
        self.B = self.C ^ self.B
        self.idx += 2

    def r_bxc(self, operand):
        self.C = self.C ^ self.B
        self.idx -= 2

    def out(self, operand):
        operand = self.combo(operand)%8
        if self.output:
            self.output = f"{self.output},{operand}"
        else:
            self.output = f"{operand}"
        self.idx += 2

    def r_out(self, operand):
        if operand == 4:
            self.A = self.expected.pop(-1)
        elif operand == 5:
            self.B = self.expected.pop(-1)
        elif operand == 6:
            self.C = self.expected.pop(-1)
        self.idx -= 2

    def bdv(self, operand):
        operand = self.combo(operand)
        self.B = trunc(self.A / (2**operand))
        self.idx += 2

    def r_bdv(self, operand):
        temp = (2**operand) * self.B

        if operand == 4:
            self.A = temp
        elif operand == 5:
            self.B = temp
        elif operand == 6:
            self.C = temp
        self.idx -= 2

    def cdv(self, operand):
        operand = self.combo(operand)
        self.C = trunc(self.A / (2**operand))
        self.idx += 2

    def r_cdv(self, operand):
        temp = (2**operand) * self.C

        if operand == 4:
            self.A = temp
        elif operand == 5:
            self.B = temp
        elif operand == 6:
            self.C = temp
        self.idx -= 2

    def run(self):
        try:
            while self:
                operation, operand = self.instructions[self.idx:self.idx+2]

                if operation == 0:
                    self.adv(operand)
                elif operation == 1:
                    self.bxl(operand)
                elif operation == 2:
                    self.bst(operand)
                elif operation == 3:
                    self.jnz(operand)
                elif operation == 4:
                    self.bxc(operand)
                elif operation == 5:
                    self.out(operand)
                elif operation == 6:
                    self.bdv(operand)
                elif operation == 7:
                    self.cdv(operand)
        except IndexError:
            print(self)
        return self.output

    def solve(self):
        self.idx = len(self.instructions) - 2
        self.A = 1
        while self.expected:
            if self.idx < 0:
                self.idx = len(self.instructions) - 2
            print(self)
            print(self.expected)
            operation, operand = self.instructions[self.idx:self.idx+2]

            if operation == 0:
                self.r_adv(operand)
            elif operation == 1:
                self.r_bxl(operand)
            elif operation == 2:
                self.r_bst(operand)
            elif operation == 3:
                self.r_jnz(operand)
            elif operation == 4:
                self.r_bxc(operand)
            elif operation == 5:
                self.r_out(operand)
            elif operation == 6:
                self.r_bdv(operand)
            elif operation == 7:
                self.r_cdv(operand)
        return self.A


    def __bool__(self):
        return self.idx < len(self.instructions)

    def __str__(self):
        return f"{self.idx}: A({self.A}),B({self.B}),C({self.C})"

def part_1_day_17(text:str):
    registers, code = text.split('\n\n')
    instructions = list(map(int, code.split(': ')[1].strip().split(',')))
    cpu = three_bit(*(int(line.split(': ')[-1]) for line in registers.split('\n')), instructions)
    return cpu.run()

def part_2_day_17(text:str):
    registers, code = text.split('\n\n')
    registers = list(int(line.split(': ')[-1]) for line in registers.split('\n'))
    instructions = list(map(int, code.split(': ')[1].strip().split(',')))
    cpu = three_bit(*registers, instructions)
    instructions = ','.join(map(str,instructions))
    iteration = 0
    # while True:
        # if not iteration% 1000:
            # print(iteration)
        # iteration += 1
        # cpu.A = iteration
        # cpu.B = registers[1]
        # cpu.C = registers[2]
        # cpu.idx = 0
        # cpu.output = ""
        # output = cpu.run()
        # if output == instructions:
            # break
    ans = cpu.solve()
    print(cpu)
    return ans

