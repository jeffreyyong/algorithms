import unittest

from reshape_matrix import Solution

class ReshapeMatrixTest(unittest.TestCase):

    def test_reshape_matrix_1(self):
        solution = Solution()
        actual = solution.matrix_reshape([[1,2],[3,4]], 1, 4)
        self.assertListEqual([[1,2,3,4]], actual)

    def test_reshape_matrix_1(self):
        solution = Solution()
        actual = solution.matrix_reshape([[1,2],[3,4]], 2, 4)
        self.assertListEqual([[1,2], [3,4]], actual)
