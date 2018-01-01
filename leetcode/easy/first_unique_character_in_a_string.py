'''
Given a string, find the first non-repeating character in it and return its index, if it
doesn't exist, return -1

Note: May assume the string contains only lowercase letters
'''

class Solution:

    def first_uniq_char(self, s):
        letters='abcdefghijklmnopqrstuvwxyz'
        # Get the indices of non repeating characters and use list comprehension to put 
        # them in a list
        index = [s.index(l) for l in letters if s.count(l) == 1]
        return min(index) if len(index) > 0 else -1
