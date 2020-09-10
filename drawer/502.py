from enum import Enum
from functools import lru_cache


def memoise(fun):
    @lru_cache(maxsize=None)
    def decorated(*args, **kwargs):
        return fun(*args, **kwargs)
    return decorated


class Parity(Enum):
    EVEN = 0
    ODD = 1

    @classmethod
    def get(cls, number):
        return cls(int(number) & 1)

    def inverted(self):
        return self.__class__(int(not self.value))


def castles(width, height):
    assert(width > 0 and height > 0)

    # rule 4 and 6 would contradict here because a
    # single-block castle would need an odd number of blocks.
    assert(height != 1)

    # rule 4: the bottom row is occupied by a block of length w.
    # that block may be ignored and the algorithm can be reduced
    # to the blocks above it. the parity is then required to be
    # odd (since that one block is already part of each castle).
    score_grown, score_less = solve(width, height - 1, Parity.ODD)

    return score_grown


# @memoise
def permutations(w):
    l = []

    if w == 1:
        return [
            [1] # +
        ]

    if w == 2:
        return [
            [1], # +.
            [1], # .+
            [2]  # ++
        ]

    if w == 3:
        return [
            [1],   # +..
            [1],   # .+.
            [1],   # ..+
            [1,1], # +.+
            [2],   # ++.
            [2],   # .++
            [3],   # +++
        ]

    raise Exception('not implemented')

    return l


parset = set()
parlst = list()


# @memoise
def solve(w, h, p):

    parset.add((w, h, p))
    parlst.append((w, h, p))

    if w == 1:
        p_h = Parity.get(h)
        score = int(p == p_h)
        return score, (h + 1) // 2 if p == Parity.ODD else h // 2

    if h == 1:
        score = sum(map(lambda o: Parity.get(len(o)) == p, permutations(w)))
        return score, score

    result_grown = 0
    result_less = 0


    for permutation in permutations(w):
        parity = p

        sum_grown = 0  # number of "grown" castles (having maximum height)
        sum_less = 0   # number of castles that are not grown

        for width in permutation:
            parity = parity.inverted()
            score_grown, score_less = solve(width, h - 1, parity)

            print((width, h - 1, parity), score_grown, score_less)

            # (1, 1, EVEN) = 0,0
            # (1, 1, EVEN) = 0,0
            # (2, 1, EVEN) = 0,0

            sum_grown += score_grown
            sum_less += 1 + score_less

        print()

        result_grown += sum_grown
        result_less += sum_less


    return result_grown, result_less

































    # if the width is one, then you can only stack blocks
    # up vertically. the height must then match the parity,
    # or otherwise there are no valid castles.












# class castle:

#     def permutations(self, w, l):
#         """ Returns the number of valid castles in a grid
#             with height 1, width `w` and a castle length `l`.
#         """

#         if w == l:
#             return 1



#         pass

#     pass


# def castle():

#     pass

"""

h=1:
    not possible,
    because then we'd only have one block which breaks rule #6.

=> h >= 2


w=1 and h is uneven:
    not possible,
    because every castle must achieve height h (rule #5)
    but w=1 and an uneven height means an uneven number of blocks
    which violates rule #6.

=>  w=1 => h is even


--- otherwise:
w=1 ? n=1
where n is the number of possible castles.



w=2 and h is uneven:
    not possible,
    for the same reason as above.

=>  w=2 => h is even


--- otherwise:
w=2 ? n=1








"""




"""

x---
-x--
--x-
---x

xx--
-xx-
--xx

   x-xx
   xx-x

xxx-
-xxx

xxxx





xxxx

xxx-
-xxx

xx--
-xx-
--xx
xx-x
x-xx

x-x-
-x-x


"""

