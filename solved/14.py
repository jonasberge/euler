#!/usr/bin/env python3
# https://projecteuler.net/problem=14


"""

Remember the length of all chains of numbers that were encountered before.
(dynamic programming)

"""


def collatz(n):
    if n & 1:
        return 3 * n + 1
    return n // 2


def solve(n):

    dp = [ None ] * (n + 1)

    root = 1
    dp[root] = 1
    longest = root

    for k in range(root + 1, len(dp)):
        kk = k

        path = [k]
        length = 1
        while k != 1:
            if k < len(dp) and dp[k] is not None:
                length += dp[k] - 1
                break  # we've already been at this point

            k = collatz(k)
            path.append(k)
            length += 1

        for i, e in enumerate(path):
            if e < len(dp):
                dp[e] = length - i

        if length > dp[longest]:
            longest = kk

    return longest


args = (1000000 - 1,)
solution = 837799
