'''
Given a string and an integer k, you need to reverse the first k characters for every 2k
characters counting from the start of the string. If there are less than k characters left,
reverse all of them. If there are lessn than 2k but greater than or equal to k character,
then reverse the first k characteres and leave the other one as original.


Example:

Input: s = "abcdefg", k = 2
Output: "bacdfeg"

Restrictions:

    The string consists of lower English letters only.
    Length of the given string and k will in the range [1, 10000]
'''


'''
Solution:
    For every block of 2k characters starting with position i, we wan to replace
    S[i:i + k] with its reverse
'''

class Solution:
    def reverse_string(self, s, k):
        s = list(s)
        for i in range(0, len(s), 2*k):
            s[i:i+k] = reversed(s[i:i+k])
            print(s)
        return "".join(s)
