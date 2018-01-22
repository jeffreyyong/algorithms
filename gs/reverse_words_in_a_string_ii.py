'''
Given an input string, reverse the string word by word. A word is defined as a sequence of non-space
characters.

The input string does not contain leading or trailing spaces and the words are always separated by a single space.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Could you do it in-place without allocating extra space?
'''

class Solution:

    def reverse_words(self, s):
        def reverse(i, j):
            while 0 <= i < j < len(s):
                s[i], s[j] = s[j], s[i]
                i, j = i + 1, j - 1

        s.append(" ")
        start = 0
        for i, v in enumerate(s):
            if v == " ":
            	reverse(start, i - 1)
            	start = i + 1
        s.pop()
        reverse(0, len(s) - 1)
