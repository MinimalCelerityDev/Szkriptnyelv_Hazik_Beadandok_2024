# test_verem.py

import unittest
from verem import Verem

class TestVerem(unittest.TestCase):
    def test_initially_empty(self):
        v = Verem()
        self.assertTrue(v.ures())

    def test_betesz_kivesz(self):
        v = Verem()
        v.betesz(1)
        v.betesz(4)
        v.betesz(5)
        self.assertEqual(v.meret(), 3)
        self.assertFalse(v.ures())
        self.assertEqual(v.kivesz(), 5)
        self.assertEqual(v.kivesz(), 4)
        self.assertEqual(v.kivesz(), 1)
        self.assertTrue(v.ures())

    def test_kivesz_empty(self):
        v = Verem()
        self.assertIsNone(v.kivesz())

if __name__ == "__main__":
    unittest.main()
