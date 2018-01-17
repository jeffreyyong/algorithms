import unittest

from sort_array_in_wave_form import *

class SortInWaveTest(unittest.TestCase):

    def test_sort_in_wave(self):

        solution = Solution()
        arr = [10,90,49,2,1,5,23]
        actual = solution.sort_in_wave_2(arr, len(arr))
        self.assertListEqual([90,10,49,1,5,2,23], actual)
