import unittest

from zigzag_conversion import *

class ConvertTest(unittest.TestCase):

    def test_convert(self):

        solution = Solution()
        actual = solution.convert("PAYPALISHIRING", 3)
        self.assertEqual("PAHNAPLSIIGYIR", actual)
