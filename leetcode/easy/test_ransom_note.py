import unittest

from ransom_note import *

class RansomNoteTest(unittest.TestCase):

    def test_ransom_note(self):

        solution = Solution()
        actual = solution.can_construct("a", "b")
        self.assertEqual(False, actual)
