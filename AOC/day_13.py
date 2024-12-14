#! /usr/bin/env python3
from re import findall
from math import sqrt
import math

def part_1_day_13(text:str):
    ans = 0
    for machine in text.split('\n\n'):
        button_a, button_b, prize = machine.split('\n')
        _, x_add_a, __, y_add_a = button_a.replace(', ', "+").split('+')
        _, x_add_b, __, y_add_b = button_b.replace(', ', "+").split('+')
        _, x_prize, __, y_prize = prize.replace(', ', "=").split('=')
        x_add_a = int(x_add_a)
        y_add_a = int(y_add_a)
        x_add_b = int(x_add_b)
        y_add_b = int(y_add_b)
        x_prize = int(x_prize)
        y_prize = int(y_prize)
        max_push = max((x_prize//x_add_a, y_prize//y_add_a))
        for i in range(max_push):
            x_diff = x_prize - (i * x_add_a)
            y_diff = y_prize - (i * y_add_a)
            if (x_diff % x_add_b == 0) and (y_diff % y_add_b == 0) and (x_diff // x_add_b == y_diff // y_add_b):
                ans += (3 * i) + (x_diff // x_add_b)
                break

    return ans

def calc_primes(end, nums = None):
    if nums is None:
        nums = [2, 3]
    num = nums[-1] + 2
    while num <= end:
        break_num = sqrt(num)//1
        for prime in filter(lambda x: x <= break_num, nums):
            if not num % prime:
                break
        else:
            nums.append(num)
        num += 2
    return nums

def get_prime_factors(primes, num):
    factors = list()
    primes = calc_primes(num, primes)
    idx = 0
    while num > 1:
        prime = primes[idx]
        if not num % prime:
            factors.append(prime)
            num = num // prime
        else:
            idx += 1
    return factors

def calc(primes, x_prize, y_prize, x_add_a, y_add_a, x_add_b, y_add_b):
    primes = [2]
    return 0

def part_2_day_13(text:str):
    conversion =10000000000000
    ans = 0
    for machine in text.split('\n\n'):
        button_a, button_b, prize = machine.split('\n')
        _, x_add_a, __, y_add_a = button_a.replace(', ', "+").split('+')
        _, x_add_b, __, y_add_b = button_b.replace(', ', "+").split('+')
        _, x_prize, __, y_prize = prize.replace(', ', "=").split('=')
        x_add_a = int(x_add_a)
        y_add_a = int(y_add_a)
        x_add_b = int(x_add_b)
        y_add_b = int(y_add_b)
        x_prize = conversion + int(x_prize)
        y_prize = conversion + int(y_prize)
        max_push = max((x_prize//x_add_b, y_prize//y_add_b))
        x = (y_prize - ((y_add_a * x_prize)/x_add_a))/(y_add_b - (y_add_a*x_add_b/x_add_a))
        y = (x_prize - ((x_add_b * y_prize)/y_add_b))/(x_add_a - (x_add_b*y_add_a/y_add_b))
        int_x = round(x)
        int_y = round(y)
        if int_x > 0 and int_y > 0 and x_prize == ((int_x*x_add_b) + (int_y*x_add_a)) and y_prize == ((int_x*y_add_b) + (int_y*y_add_a)):
            ans += (3*int_y) + int_x

    return ans

