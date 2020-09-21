#!/usr/bin/env python3
# https://projecteuler.net/problem=464


"""



"""


from math import floor, sqrt

from helper.prime import Primes


primes = Primes()


def divide_evenly(n, m):
    r = n // m
    if r * m == n:
        return r
    return False

def divides_evenly(n, m):
    return divide_evenly(n, m) != False


def is_squarefree(n):
    if n < 1:
        raise Exception('n cannot be less than 1')

    limit = floor(sqrt(n))

    for prime in primes(limit):
        n = divide_evenly(n, prime) or n
        if divides_evenly(n, prime):
            return False
        if n == 1:
            break

    return True


def omega(n):
    if n < 2:
        return []

    # n can only have prime factors below the square root of itself
    # if it's a composite number, otherwise it must be a prime number.
    limit = floor(sqrt(n))
    is_n_prime = True

    for prime in primes(limit):
        divided = False
        while True:
            m = divide_evenly(n, prime)
            if not m:
                break
            divided = True
            n = m
        if divided:
            yield prime
            is_n_prime = False
        if n == 1:
            break

    if is_n_prime:
        yield n


def moebius(n):
    if n == 1 or not is_squarefree(n):
        return 0

    r = -1
    for _ in omega(n):
        r *= -1

    return r


def generate_squarefree(limit):

    generators = [ primes(start=2) ]
    factors = [ next(gen) for gen in generators ]

    product = 1
    for fac in factors:
        product *= fac

    yielded = False
    depth = 1

    while True:

        if product >= limit:

            if depth == len(factors):  # time to add another factor.

                if not yielded:
                    # we haven't yielded anything with this many factors,
                    # so adding another one won't make the result smaller.
                    return

                factor_amount = len(factors)
                generators = [ primes(start=2) ]
                factors = [ next(generators[0]) ]
                product = factors[0]

                for _ in range(factor_amount):
                    fac = factors[len(factors) - 1]
                    gen = primes(start=fac + 1)
                    next_fac = next(gen)

                    generators.append(gen)
                    factors.append(next_fac)
                    product *= next_fac

                yielded = False
                depth = 1
                continue

            for _ in range(depth):
                product //= factors.pop()
                generators.pop()

            product //= factors.pop()
            next_factor = next(generators[len(factors)])
            factors.append(next_factor)
            product *= next_factor

            for _ in range(depth):
                fac = factors[len(factors) - 1]
                gen = primes(start=fac + 1)
                next_factor = next(gen)

                generators.append(gen)
                factors.append(next_factor)
                product *= next_factor

            depth += 1
            continue

        yield product
        yielded = True
        depth = 1

        product //= factors.pop()
        next_factor = next(generators[len(factors)])
        factors.append(next_factor)
        product *= next_factor





def solve():


    g = generate_squarefree(20000000 + 1)
    for n in g:
        pass


    # l = list(sorted(g))

    # print(len(l)) #, l)


    return

    n = 100000

    moe = [ None ] * (n + 1)
    for k in range(1, n + 1):
        moe[k] = moebius(k)

    print('moe calc\'d')

    acc_moe_P = 0
    acc_moe_N = 0

    a = 1
    d = dict()
    for b in range(a, n + 1):
        acc_moe_P += moe[b] == 1
        acc_moe_N += moe[b] == -1

        d[(a, b)] = {
            'P({}, {})'.format(a, b): acc_moe_P,
            'N({}, {})'.format(a, b): acc_moe_N
        }


    # for key, value in d.items():
    #     print(key, '->', value)





    pass




args = ()
solution = None
