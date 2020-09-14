from math import ceil, log10


def count_digits(n):
    return ceil(log10(n + 1))
