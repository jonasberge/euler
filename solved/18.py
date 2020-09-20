#!/usr/bin/env python3
# https://projecteuler.net/problem=18


from euler.problem import read_data


def get_triangle():
    triangle = []
    data = read_data('triangle.txt')
    for row in data.split('\n'):
        triangle.append([ int(n) for n in row.split() ])
    return triangle


def solve():
    triangle = get_triangle()

    for i in reversed(range(0, len(triangle) - 1)):
        j = i + 1

        for k in range(len(triangle[i])):
            c = k
            n = k + 1

            triangle[i][k] += max(triangle[j][c], triangle[j][n])

    return triangle[0][0]


args = ()
solution = 1074
