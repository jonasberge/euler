#!/usr/bin/env python3
# https://projecteuler.net/problem=200


"""


2 3
2 5
2 7
3 2
3 5
3 7





"""

from math import log

from helper.prime import Primes



def squbes(primes=Primes()):

    p_i = 1
    q_i = 0

    p = lambda: primes[p_i]
    q = lambda: primes[q_i]

    sqube = lambda: p() ** 2 * q() ** 3





    pass



def solve():

    primes = Primes()

    sqi = 1  # square index
    cui = 0  # cube index

    sq = primes[sqi]
    cu = primes[cui]

    current = sq ** 2 * cu ** 3

    print(squbes())









    pass




args = ()
solution = None
