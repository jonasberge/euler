#!/usr/bin/env python3
# https://projecteuler.net/problem=2


"""

odd + odd = even
even + odd = odd (commutative)
even + even = even

=> whenever there is just one odd number, the result is odd.

the fibonacci sequence starts with two odd numbers (1 and 1):

1, 1 -> 2  // odd + odd = even (1)
1, 2 -> 3  // odd + even = odd (2)
2, 3 -> 5  // even + odd = odd (3)
3, 5 -> 8  // odd + odd = even (1) -- repeats

=> every third number is even.

consider the following scheme:
(assign the letter with the number below it)

a b c d e f
1 1 2 3 5 8

init = [1, 1, 2]
     = [a, b, c]

we can get the three next values like this:

d = b + c

e = c + d
  = c + (b + c)
  = b + 2c

f = d + e
  = (b + c) + (c + (b + c))
  = 2b + 3c

next = [
    b + c,
    b + 2c,
    2b + 3c
]

from the initial values (init above) we have:

- b is odd
- c is even

we can prove that c (= 2b + 3c) always stays even:

2 * odd + 3 * even =
even * odd + odd * even =
even + even =
even

=> c (third entry) is always even.

prove that a and b are not even:

a = b + c = odd + even = odd
b = b + 2c = odd + even * even = odd + even = odd

=> c is the only even number.

"""


def solve(limit):

    fib = [1, 1]
    fib.append(sum(fib))

    res = 0

    while fib[2] <= limit:

        b = fib[1]
        c = even = fib[2]

        res += even

        fib = [
            b + c,
            b + 2 * c,
            2 * b + 3 * c
        ]

    return res


limit = int(4e6)

args = (limit,)
solution = 4613732
