# Given a words.txt file containing a newline-delimited list of dictionary
# words, please implement the Anagrams class so that the get_anagrams() method
# returns all anagrams from words.txt for a given word.
#
# Requirements:
#   - Optimise the code for fast retrieval
#   - Write more tests
#   - Thread safe implementation

import unittest
import itertools

class Anagrams:

    def __init__(self):
        self.words = open('words.txt').readlines()

    def get_anagrams(self, word):
        striped_words = [line.strip().lower() for line in self.words]
        anagrams = sorted([a for a in set(["".join(perm) for perm in itertools.permutations(word)]) if a in striped_words])
        return anagrams

all_words = Anagrams()
agrams = all_words.get_anagrams("")
print(agrams)
