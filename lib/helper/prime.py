from math import ceil, log

import numpy as np


def approx_nth_prime(n):
    if n <= 0: raise ValueError('n may not be 0 or less')
    n += 1; return ceil(n * log(n))

def approx_nth_prime_upper(n):
    return ceil(1.2 * approx_nth_prime(n))


def _extend_prime_table(table, primes, n):

    index = len(table)

    extended = np.ones(len(table) + n, dtype=bool)
    extended[:len(table)] = table
    table = extended

    for prime in primes:
        first = prime * ((index - 1) // prime + 1)
        table[first::prime] = False

    return table


def primes(limit=None, /, *, start=0, end=None, initial_capacity=101):

    if limit and limit < 0:
        raise ValueError('limit may not be less than 0')

    if end and end < start:
        raise ValueError('end may not be less than start')

    p, is_prime = 2, True

    if initial_capacity < p:
        raise ValueError('initial_capacity may not be less than {}'.format(p))

    initial_capacity += end or start
    step_size = 7

    table = np.ones(initial_capacity)
    table[0] = table[1] = False

    primes = []
    count = 0

    limit_extended = False

    while True:
        if is_prime:

            if p >= start:
                if limit and count == limit: return
                if end and p >= end: return

                if limit and not limit_extended:

                    last_prime_index = len(primes) + limit
                    upper_limit = approx_nth_prime_upper(last_prime_index)
                    extend_by = upper_limit - len(table)

                    table = _extend_prime_table(table, primes, n=extend_by)
                    limit_extended = True

                yield p
                count += 1

            primes.append(p)
            table[p + p::p] = False

        k = None  # overwrite any value from previous the iteration

        for k in range(p + 1, len(table)):
            if table[k]:
                p = k
                break

        is_prime = True

        if p != k:
            if k is not None:
                p = k

            table = _extend_prime_table(table, primes, n = p + len(primes))
            is_prime = False
