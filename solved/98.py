#!/usr/bin/env python3
# https://projecteuler.net/problem=98


"""

before we try to find all "square anagram word pairs"
we can take note of the following things:

- words can only be (square) anagrams of eachother if they have the same length
- each word of such an anagram group must have the exact same letters as
  any other. that is the same letters, but also the exact same number of
  occurences of each letter


1. categorise all words into anagram-groups
-> words that are anagrams of eachother belong to the same group
-> palindromic words are not anagrams of themselves

now we can do the following for each anagram group:

2. discard groups that have more than ten different letters.
-> there are only ten different digits. it would be impossible to
   assign each letter a unique digit with more than ten letters.

3. check if the group contains two or more words, otherwise discard it.
-> we cannot find square anagram word pairs with just one word.


now let's discuss how we're going to assign digits to letters.

since there's the restriction that numbers need to be square numbers and that
they need to have the same length as the word (i.e. the same number of digits
as there are letters), we can break our problem space down to only a handful
of numbers that are possible solutions for a certain group of anagrams.

e.g. there are only 217 square numbers with 5 digits:

>>> digits = 5
>>> a = ceil(sqrt(10 ** (digits - 1)))
>>> b = floor(sqrt(10 ** digits - 1))
>>> b - a + 1
217


knowing this, we're able to precompute all square numbers for a certain
number of digits. with knowledge about these, we can continue:

each square number has a certain set of digits and each of these digits
also occurs a certain amount of times. this is exactly the same property
as described above with words and their letters.

now, like we've done with words, we can also group square numbers into groups
with the same number digits and their respective amount of occurences.


at this point we have two groups:

- words that are anagrams of eachother
- numbers that are anagrams of eachother

what we need to do now is map each group of words to a group of numbers:

1. both groups need to have the same length i.e. amount of letters/digits.
2. both groups need to have the exact same number of occurences.
   it is only when this condition is met, that we're able
   to map a digit to a letter without any conflicts.

for each matching pair of groups we need to do one more step.
a word and a number are not guaranteed to be compatible with eachother yet
because it's possible that a number that occurs multiple times is associated
with two different letters that aren't at the right position, e.g.:

112 and ABA: A would be assigned 1 and then 2, which is not possible.


to figure out which words and letters of those
groups are compatible we do the following:

1. pick the next word, or finish
2. pick the next number, or go to (1) if there's no number left
3. compute which letter gets which digit
4. if a conflict occurs, i.e. a digit was already assigned to a letter,
   then ignore this number and continue at step (2)
5. memorise this word-number pair and go to (2)

TODO: rework this ->

now we have a list of word-number pairs that are compatible with eachother.
if there's only one pair for a word then we ignore it, as it's not
possible to create a square anagram word pair with only one word.

otherwise, any word-number pair can be combined with every other pair to
form a square anagram word pair. we can then pick the largest square number
and remember it as a possible solution to the problem.

repeat this process for every group.

"""


from collections import defaultdict
from itertools import groupby
from functools import cached_property
from math import floor, ceil, sqrt

from euler.problem import read_data
from euler.cache import disk_cached


def get_words():
    words = read_data('words.txt')
    words = words.split(',')
    return [ w[1:-1] for w in words ]


class Word:
    def __init__(self, word):
        self._raw = word
        self._value = word.upper()

    @property
    def raw(self):
        return self._raw

    @property
    def value(self):
        return self._value

    @cached_property
    def letters(self):
        return set(self.value)

    @cached_property
    def occurences(self):
        word = self.value
        return { c: word.count(c) for c in word }

    @cached_property
    def sorted_characters(self):
        return ''.join(sorted(self.value))

    @cached_property
    def sorted_letter_counts(self):
        return [ n for n in sorted(self.occurences.values()) ]

    def count(self, char):
        return self.occurences.get(char.upper(), 0)

    def is_anagram_of(self, other):
        return self.occurences == other.occurences

    def __len__(self):
        return len(self._value)

    def __repr__(self):
        return '{}({!r})'.format(self.__class__.__name__, self.raw)

    def __str__(self):
        return self.raw


@disk_cached
def group_anagrams(words):
    key = lambda w: w.sorted_characters
    words = sorted(words, key=key)
    anagrams = groupby(words, key)
    return [ list(g) for _, g in anagrams ]


def solve():

    words = map(Word, get_words())
    words = [ w for w in words if len(w.letters) <= 10 ]

    anagrams = group_anagrams(words)
    anagrams = [ g for g in anagrams if len(g) > 1 ]


    square_anagrams_for_digits = dict()

    for digits in range(1, 10 + 1):
        lo = ceil(sqrt(10 ** (digits - 1)))
        hi = floor(sqrt(10 ** digits - 1))

        squares = []

        for base in range(lo, hi + 1):
            square = base ** 2
            square = Word(str(square))
            squares.append(square)

        square_anagrams = [ g for g in group_anagrams(squares) if len(g) > 1 ]
        square_anagrams_for_digits[digits] = square_anagrams


    compatibles = defaultdict(list)

    for group in anagrams:
        for word in group:
            for numbers in square_anagrams_for_digits[len(word)]:
                for number in numbers:
                    char_map, digit_map = dict(), dict()
                    compatible = True
                    for char, digit in zip(word.value, number.value):
                        if char_map.get(char, digit) != digit or \
                                digit_map.get(digit, char) != char:
                            compatible = False
                            break
                        char_map[char] = digit
                        digit_map[digit] = char
                    if not compatible:
                        continue
                    items = sorted(char_map.items())
                    chars = ''.join(str(k) for k, _ in items)
                    numbers = ''.join(str(v) for _, v in items)
                    compatibles[chars + numbers].append((word, number))

    compatibles = { k: v for k, v in compatibles.items() if len(v) > 1 }

    highest = 0

    for pairs in compatibles.values():
        for word, number in pairs:
            number = int(number.value)
            highest = max(highest, number)

    return highest


args = ()
solution = 18769
