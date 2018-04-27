'''
Write a function to find the longest common prefix string amongst an array of strings.
'''

'''
Logic:
    1. Pick a character at i=0th location and compare it with the character at that location in every string.
    2. If anyone doesn't have that just return ""
    3. Else append that character into the result
    4. Increment i and do steps 1-3 till the length of the string
    5. return result
'''

class Solution:

    def longest_common_prefix(self, strs):

        if not strs:
            return ""

        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
            else:
                return min(strs)
