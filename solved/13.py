#!/usr/bin/env python3
# https://projecteuler.net/problem=13


from math import floor, log10

from euler.problem import read_data
from euler.cache import disk_cached

from helper.number import count_digits


def get_numbers():
    numbers = read_data('numbers.txt')
    return numbers.strip().split('\n')


def solve(digit_count):

    numbers = get_numbers()
    length = len(numbers[0])

    digit = length - 1
    power = 1
    shift = 0

    result = 0

    while digit >= 0:
        for number in numbers:
            result += int(number[digit]) * 10 ** (power - shift)

        remove = max(0, count_digits(result) - digit_count)
        result //= 10 ** remove

        digit -= 1
        power += 1
        shift += remove

    return result


args = (10,)
solution = 5537376230
