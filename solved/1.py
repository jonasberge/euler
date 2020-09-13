#!/usr/bin/env python3
# https://projecteuler.net/problem=1


# computes the sum of all multiples until a limit.
def sum_of_multiple(multiple, limit):
    n = limit // multiple
    gauss_sum = n * (n + 1) // 2
    return multiple * gauss_sum


def solve(a, b, limit):

    result = sum(sum_of_multiple(m, limit) for m in (a, b))

    # remove those that were added twice.
    # (numbers which have both a and b as a multiple)
    result -= sum_of_multiple(a * b, limit)

    return result


a = 3
b = 5
limit = 1000

args = (a, b, limit - 1)
solution = 233168
