
import unittest

from meeting_rooms import *

class MeetingRoomsTest(unittest.TestCase):

    def test_can_attend_meetings(self):
        interval1 = Interval(0, 30)
        interval2 = Interval(5, 10)
        interval3 = Interval(15, 20)
        solution = Solution()
        actual = solution.can_attend_meetings([interval1, interval2, interval3])
        self.assertEqual(False, actual)
