#!/usr/bin/env python3
# https://projecteuler.net/problem=3


"""

if n is not a prime number, then it must have a prime factor
less than or equal to the square root of n.[citation needed]

to find the prime factors of n, we can check all prime numbers
until the square root of n and pick the largest that divides n evenly.

this is the solution to the problem.

to find those prime numbers we can utilize the sieve of eratosthenes.

"""


from math import sqrt


def sieve(n):
    n = n + 1  # our indices are based at 1, not 0

    table = [True] * n
    table[0] = table[1] = False  # 0 and 1 are not prime numbers

    i = 2
    while i < n:
        for k in range(i + i, n, i):
            table[k] = False

        for j in range(i + 1, n):
            if table[j]:
                i = j
                break

        if i != j:
            break

    return [
        n
        for n, is_prime in enumerate(table)
        if is_prime
    ]


def solve(n):

    limit = int(sqrt(n))
    primes = sieve(limit)

    for p in reversed(primes):
        if n % p == 0:
            return p

    return None


n = 600851475143

if __name__ == '__main__':
    print(solve(n))  # 6857
