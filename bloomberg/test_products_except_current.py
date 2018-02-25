import unittest

from products_except_current import *

class ProductsExceptCurrentTest(unittest.TestCase):

    def test_products(self):
        actual = solution([1,7,3,4])
        self.assertEqual(actual, [84,12,28,21])
