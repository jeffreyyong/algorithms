import unittest

from excel_sheet_column_number import *

class ExcelSheetColumnNumberTest(unittest.TestCase):

    def test_title_to_number(self):
        solution = Solution()
        actual = solution.title_to_number("A")
        self.assertEqual(1, actual)
        actual = solution.title_to_number("B")
        self.assertEqual(2, actual)
        actual = solution.title_to_number("Z")
        self.assertEqual(26, actual)
        actual = solution.title_to_number("AA")
        self.assertEqual(27, actual)

        
