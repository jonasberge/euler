#!/usr/bin/env python3
# https://projecteuler.net/problem=6


"""

TODO: solve this with a formula instead of the trivial way.

"""


def solve(n):
    numbers = range(1, n + 1)
    sqofsum = sum(numbers) ** 2
    sumofsq = sum(x ** 2 for x in numbers)
    return abs(sqofsum - sumofsq)


numbers = 100

if __name__ == '__main__':
    print(solve(numbers))  # 25164150
