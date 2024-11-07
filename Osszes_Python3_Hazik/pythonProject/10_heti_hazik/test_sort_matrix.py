# test_sort_matrix.py

import unittest
from sort_matrix import sort_matrix

class TestSortMatrix(unittest.TestCase):
    def test_sort_matrix(self):
        matrix = [[2, 6], [1, 3], [5, 4]]
        sorted_matrix = [[1, 3], [5, 4], [2, 6]]
        self.assertEqual(sort_matrix(matrix), sorted_matrix)

if __name__ == "__main__":
    unittest.main()
