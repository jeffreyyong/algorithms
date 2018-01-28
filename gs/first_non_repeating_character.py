'''
Given a string, find the first non-repeating character in it and return its index, if it
doesn't exist, return -1

Note: May assume the string contains only lowercase letters
'''

'''
Solution:

'''

import string

class Solution:

    def first_unique_char(self, s):

        min_index = len(s)

        for c in string.ascii_lowercase:

            curr_index = s.find(c)

            # if can find the character for the current index 
            # and current index is the highest index for that particular character
            # keep looking for the minimised index for all the characters

            if curr_index != -1 and curr_index == s.rfind(c):
                min_index = min(min_index, curr_index)

        return min_index if min_index != len(s) else -1
