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
a word an a number are not guaranteed to be compatible with eachother yet
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

now we have a list of word-number pairs that are compatible with eachother.
if there's only only pair, then we ignore this group, as it's not possible
to create a square anagram word pair with only one word.

otherwise, any word-number pair can be combined with every other pair to
form a square anagram word pair. we can then pick the largest square number
and remember it as a possible solution to the problem.

repeat this process for every group.

"""


from functools import cached_property

from euler.data import read_data
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
    def sorted_letter_counts(self):
        return [ n for n in sorted(self.occurences.values()) ]

    def count(self, char):
        return self.occurences.get(char.upper(), 0)

    def is_anagram_of(self, other):
        return self.occurences == other.occurences

    def __len__(self):
        return len(self._value)

    def __repr__(self):
        return '{}("{}")'.format(self.__class__.__name__, self.raw)

    def __str__(self):
        return self.raw


@disk_cached
def anagram_groups(words):
    words = set(words)
    result = []

    while words:
        current = words.pop()
        group = [ current ]

        for word in words:
            if current.is_anagram_of(word):
                group.append(word)

        result.append(group)
        words -= set(group)

    return result


def solve():
    words = [ Word(w) for w in get_words() ]
    anagrams = anagram_groups(words)

    print([ g for g in anagrams if len(g) > 1 ])




args = ()
solution = ""
