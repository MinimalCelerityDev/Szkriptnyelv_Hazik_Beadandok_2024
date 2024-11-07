# test_sum_of_digits.py

import unittest
from sum_of_digits import sum_of_digits

class TestSumOfDigits(unittest.TestCase):
    def test_small_number(self):
        self.assertEqual(sum_of_digits(32768), 26)

    def test_large_power_of_two(self):
        self.assertEqual(sum_of_digits(2**15), 26)
        self.assertEqual(sum_of_digits(2**1000), 1366)

if __name__ == "__main__":
    unittest.main()
