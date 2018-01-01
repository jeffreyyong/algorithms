"""
Given a string which consists of lowercase or uppercase letters, find the length of the 
longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""

"""
Solution:
Count how many letters appear an odd number of times. Because we can use all letter
except for each odd-count letter we must leave one, except one of them we can use.
"""

import collections

class Solution:

    def longest_palindrome(self, s):
        odds = sum(v & 1 for v in collections.Counter(s).values())
        return len(s) - odds + bool(odds)
