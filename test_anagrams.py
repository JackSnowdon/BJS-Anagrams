import unittest
from anagrams import Anagrams

class TestAnagrams(unittest.TestCase):
   
    def test_3_letter(self):
        anagrams = Anagrams()
        self.assertEqual(anagrams.get_anagrams('eat'), ['ate', 'eat', 'tea'])

    def test_6_letter(self):
        anagrams = Anagrams()
        self.assertEqual(anagrams.get_anagrams('plates'), ['palest', 'pastel', 'petals', 'plates', 'staple'])

if __name__ == '__main__':
    unittest.main()
