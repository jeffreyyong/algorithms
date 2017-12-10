'''
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
'''
from functools import reduce

class Solution:

    # @return a string
    def title_to_number(self, string):
        return reduce(lambda x, y : x * 26 + y, [ord(c) - 64 for c in list(string)])

