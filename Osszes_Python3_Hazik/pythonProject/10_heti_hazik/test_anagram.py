# test_anagram.py

import unittest
from anagram import is_anagram

class TestIsAnagram(unittest.TestCase):
    def test_anagrams(self):
        self.assertTrue(is_anagram("listen", "silent"))
        self.assertTrue(is_anagram("A gentleman", "Elegant man"))

    def test_not_anagrams(self):
        self.assertFalse(is_anagram("hello", "world"))

if __name__ == "__main__":
    unittest.main()
