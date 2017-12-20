import unittest

from license_key_formatting import *

class LicenseKeyFormattingTest(unittest.TestCase):

    def test_license_key_formatting(self):

        solution = Solution()
        actual = solution.license_key_formatting("5F3Z-2e-9-w", 4)
        self.assertEqual("5F3Z-2E9W", actual)
        actual = solution.license_key_formatting("2-5g-3-J", 2)
        self.assertEqual("2-5G-3J", actual)
