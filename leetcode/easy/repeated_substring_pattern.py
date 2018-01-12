'''
Given a non-empty string check if it can be constructed by taking a substring of it and appending
multiple copies of the substring together. You may assume the given string consists of lowercase
English letters only and its length will not exceed 10000.

Example 1:
    Input: "abab"
    Output: True
    Explanation: It's the substring "ab" twice

Example 2:
    Input: "aba"
    Output: False

Example 3:
    Input: "abcabcabcabc"
    Output: True
    Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
'''

'''
Solution:
    1. First char of input string is first char of repeated substring
    2. Last char of input string is last char of repeated substring
    3. Let S1 = S + S (where S in input string)
    4. Remove first and last char of S1. Let this be S2
    5. If S exists in S2 then return true else false
    6. Let i be index in S2 where S starts then repeated substring length i + 1 and repeated substring
        S[0: i + 1]
'''

class Solution:

    def repeated_substring_pattern(self, s):
        return s in (s+s)[1:-1]
