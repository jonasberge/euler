#!/usr/bin/env python3
# https://projecteuler.net/problem=15


from math import factorial


def binomial(n, k):
    return factorial(n) // factorial(k) // factorial(n - k)


def solve(n, m):
    return binomial(n + m, n)


args = (20, 20)
solution = 137846528820
