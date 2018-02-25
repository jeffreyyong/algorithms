import unittest

from delete_min_max import *

class DeleteMinMaxTest(unittest.TestCase):

    def test_delete_min_max(self):
        actual = delete_min_max([3,2,5,1,2,4])
        self.assertEqual(actual, [3,2,2,4])
