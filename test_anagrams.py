import unittest
from anagrams import Anagrams

class TestAnagrams(unittest.TestCase):
   
    def test_3_letter(self):
        anagrams = Anagrams()
        self.assertEqual(anagrams.get_anagrams('eat'), ['ate', 'eat', 'tea'])

    def test_4_letter(self):
        anagrams = Anagrams()
        self.assertEqual(anagrams.get_anagrams('stop'), ['opts', 'post', 'pots', 'spot', 'stop', 'tops'])

    def test_5_letter(self):
        anagrams = Anagrams()
        self.assertEqual(anagrams.get_anagrams('spear'), ['pares', 'parse', 'pears', 'rapes', 'reaps', 'spare', 'spear'])

    def test_6_letter(self):
        anagrams = Anagrams()
        self.assertEqual(anagrams.get_anagrams('plates'), ['palest', 'pastel', 'petals', 'plates', 'staple'])

    def test_7_letter(self):
        anagrams = Anagrams()
        self.assertEqual(anagrams.get_anagrams('stripes'), ['persist', 'stripes'])

if __name__ == '__main__':
    unittest.main()
