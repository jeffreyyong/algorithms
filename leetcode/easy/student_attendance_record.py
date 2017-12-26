'''
You are given a string representing an attendance record for a student.
The record only contains the following three characters:
1. 'A': Absent
2. 'L': Late
3. 'P': Present

A student could be rewarded if his attendace record doesn't contain more than one
'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.\
Example 1:

Input: "PPALLP"
Output: True

Example 2:

Input: "PPALLL"
Output: False
'''

class Solution:
    # Just check that there aren't two 'A' or three consecutive 'L' (takes care of all
    # "more than two" cases). Easiest with a regular expression, though at least
    # Python has a nice "count A" and "contains LLL" functionality.
    def check_record(self, s):
        return not (s.count('A') > 1 or 'LLL' in s)
