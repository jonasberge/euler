#!/usr/bin/env python3
# https://projecteuler.net/problem=5


"""

a subset of the prime factorization of the desired number
needs to be able to represent any number between 1 and 20.

if this condition is met, then the number is
evenly divisible by any of those 20 numbers.

how can this be guaranteed?

for the prime factorization use each prime number that is
smaller than the largest number that is to be divided (20).

give each prime factor a power that makes it the largest number below 20.
e.g. the prime number 2 would get the power 4, because 2**4 = 16 < 20.

why is this rule true?

every number that is less than or equal to 20 can be split into their
prime factors. those prime factors WILL be a subset of the prime factors
described above because every factor has a power that guarantees it to be
the largest number below 20.

eg. 18 = 2 * 9
or: 16 = 2 ** 4

"""


from math import floor, log2 as log

from helper.prime import primes


def solve(digits):
    product = 1
    for prime in primes(end=digits):
        power = floor(log(digits) / log(prime))
        product *= prime ** power
    return product


digits = 20

args = (digits,)
solution = 232792560
