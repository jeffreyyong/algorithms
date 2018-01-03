import unittest

from student_attendance_record import *

class CheckRecordTest(unittest.TestCase):

    def test_check_record(self):

        solution = Solution()
        actual = solution.check_record("PPALLP")
        self.assertEqual(True, actual)
        actual = solution.check_record("PPALLLL")
        self.assertEqual(False, actual)
