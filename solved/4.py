#!/usr/bin/env python3
# https://projecteuler.net/problem=4


"""

1: generate palindrome numbers, from largest to smallest.

an implementation of this is rather trivial
and realized in the PalindromeNumber class.

2: check if the palindrome can be computed by multiplying two numbers.

this is done as follows:

9009 = 91 * 99

this example has the nice property of being
transformable to the third binomial formula:

9009 = (95 - 4) * (95 + 4)

which lead me to the following idea:

1. find the square root of the target palindrome number and ceil it.
2. iterate by adding one in each step until the largest three-digit number:
   a. compute the following difference: x * x - target
      where x is the current value of the iteration
   b. if this difference is a square, then the palindrome number
      can be represented as the third binomial formula
   c. check if both multipliers are three-digit numbers -> then done

"""

from collections import deque
from functools import cached_property
from itertools import chain, takewhile
from math import floor, ceil, log10, sqrt

from helper.number import count_digits


class Number:
    def __init__(self, value):
        if value < 0:
            raise Exception('negative values are not supported')
        self._value = value

    @property
    def value(self):
        return self._value

    @cached_property
    def digits(self):
        result = deque()
        value = self.value
        while value:
            digit = value % 10
            value = value // 10
            result.appendleft(digit)
        return list(result)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, str(self))


class PalindromeNumber(Number):
    def __init__(self, value):
        super().__init__(value)
        if not self._is_palindrome():
            raise Exception('%d is not a palindrome number' % (value,))

    def _is_palindrome(self):
        digits = self.digits
        zipped = zip(digits, reversed(digits))
        return all(a == b for a, b in zipped)

    @property
    def is_odd(self):
        return bool(len(self) & 1)

    @property
    def is_even(self):
        return not self.is_odd

    @cached_property
    def center_zeroes(self):
        digits = self.digits
        digits_right = digits[len(digits) // 2:]
        zeroes = takewhile(lambda x: x == 0, digits_right)

        count = sum(1 for _ in zeroes)
        odd = len(digits) % 2 == 1
        result = 2 * count - odd

        return max(0, result)

    @cached_property
    def without_center_zeroes(self):
        if self.center_zeroes == 0:
            return self

        outer = (len(self) - self.center_zeroes) // 2
        left = self.digits[:outer]

        number = 0
        for digit in chain(left, reversed(left)):
            number *= 10
            number += digit

        return PalindromeNumber(number)

    def next_smaller(self):

        zeroes = self.center_zeroes
        outer = (len(self) - zeroes) // 2

        if len(self) == 1:
            subtract = 1

        elif self.value == 11 or self.without_center_zeroes.value == 11:
            subtract = 2

        elif zeroes > 0:
            offset = (outer - 1)
            subtract = 11 * 10 ** offset

        else:
            center = 11 if self.is_even else 1
            offset = (len(self) - 1) // 2
            subtract = center * 10 ** offset

        return PalindromeNumber(self.value - subtract)

    def __len__(self):
        return len(self.digits)


def palindrome_numbers(start):
    p = PalindromeNumber(start)

    while p.value > 0:
        yield p.value
        p = p.next_smaller()


def solve():
    factor_digits = 3
    largest = 997799  # largest palindrome number below 999 * 999 = 998001

    for p in palindrome_numbers(largest):

        factor = ceil(sqrt(p))
        if count_digits(factor) != factor_digits:
            factor = 10 ** (factor_digits - 1)

        for factor in range(factor, 10 ** factor_digits):
            diff = factor ** 2 - p
            root = floor(sqrt(diff))

            if root ** 2 == diff:
                a = factor + root
                b = factor - root

                if count_digits(a) != factor_digits or \
                        count_digits(b) != factor_digits:
                    continue

                return a * b

    return None


args = ()
solution = 906609
