import unittest

from string_compression_using_repeated_character_counts import *

class CompressTest(unittest.TestCase):

    def test_compress_word(self):

        solution = Solution()
        actual = solution.compress_word("aabccccaa")
        self.assertEqual("a2b1c4a2", actual)
