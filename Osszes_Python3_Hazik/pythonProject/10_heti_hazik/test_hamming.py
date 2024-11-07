# test_hamming.py

import unittest
from hamming import hamming_distance

class TestHammingDistance(unittest.TestCase):

    def test_equal_strings(self):

        self.assertEqual(hamming_distance("abc", "abc"), 0)

    def test_different_strings(self):

        self.assertEqual(hamming_distance("toned", "roses"), 3)

    def test_unequal_length(self):
        
        with self.assertRaises(ValueError):

            hamming_distance("abc", "ab")

if __name__ == "__main__":
    unittest.main()
