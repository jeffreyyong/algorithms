import unittest

from maximum_products_of_three_numbers import *

class MaximumProductTest(unittest.TestCase):

    def test_maximum_product(self):

        solution = Solution()
        actual = solution.maximum_product([1,2,3])
        self.assertEqual(6, actual)
        actual = solution.maximum_product([1,2,3,4])
        self.assertEqual(24, actual)
