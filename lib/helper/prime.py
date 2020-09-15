from math import floor, ceil, log

import numpy as np


def approx_nth_prime(n):
    """ approximation for the nth prime number. """
    if n <= 0: raise ValueError('n may not be 0 or less')
    n += 1; return ceil(n * log(n))

def approx_nth_prime_upper(n):
    """ approximate upper limit for the nth prime number. """
    return ceil(1.2 * approx_nth_prime(n))

def approx_gap_after(p):
    """ approximates the gap after a prime near p. """
    return floor(log(p) ** 2 * 0.85)


class Primes:
    def __init__(self, *, initial_capacity=101):
        self._sieve = np.ones(initial_capacity, dtype=bool)
        self._sieve[0] = self._sieve[1] = False
        self._primes = []

        self._generator = self._generate()

    def _extend_capacity(self, amount):
        sieve = self._sieve

        print('resize', amount)

        length = len(sieve) + amount
        extended = np.ones(length, dtype=bool)
        extended[:len(sieve)] = sieve

        index = len(sieve)
        sieve = extended

        for prime in self._primes:
            first = prime * ((index - 1) // prime + 1)
            sieve[first :: prime] = False

        self._sieve = sieve

    def _ensure_capacity(self, amount):
        missing = amount - len(self._sieve)
        if missing > 0:
            self._extend_capacity(missing)

    def _generate(self):
        primes = self._primes

        p, is_prime = 2, True

        while True:
            if is_prime:
                primes.append(p)
                self._sieve[p + p :: p] = False
                yield p

            k = None  # overwrite any value from the previous iteration

            for k in range(p + 1, len(self._sieve)):
                if self._sieve[k]:
                    p = k
                    break

            is_prime = True

            if p != k:
                if k is not None:
                    p = k

                self._extend_capacity(p + len(primes))
                is_prime = False

    def __getitem__(self, index):
        if isinstance(index, slice):
            raise TypeError("'{}' object is not sliceable"
                            .format(self.__class__.__name__))
        if index < 0:
            raise IndexError('index out of range')

        missing = index - len(self._primes) + 1
        for _ in range(missing):
            next(self._generator)

        return self._primes[index]

    def __iter__(self):
        index = 0

        for prime in self._primes:
            yield prime
            index += 1

        while True:
            yield self[index]
            index += 1

    def __call__(self, limit=None, /, *, start=0, end=None):

        if limit and limit < 0:
            raise ValueError('limit may not be less than 0')

        if end and end <= start:
            raise ValueError('end must be greater than start')

        iteration = 0
        yielded = 0

        sufficient_capacity = False

        if end:
            self._ensure_capacity(end + approx_gap_after(end))
            sufficient_capacity = True

        for prime in self:

            if limit and yielded == limit: return
            if end and prime >= end: return

            if prime >= start:

                if limit and not sufficient_capacity:
                    last_prime_index = iteration + limit
                    upper_limit = approx_nth_prime_upper(last_prime_index)
                    self._ensure_capacity(upper_limit)
                    sufficient_capacity = True

                yield prime
                yielded += 1

            iteration += 1


def primes(limit=None, /, *, start=0, end=None, initial_capacity=101):
    primes = Primes(initial_capacity=initial_capacity)
    yield from primes(limit, start=start, end=end)
