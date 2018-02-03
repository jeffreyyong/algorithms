'''
Given a string `s` and a non-empty string `p`, find all the start indices of `p's` anagram in `s`.

String consists of lowercase English letters only and the length of both strings `s` and `p`
will not be larger than 2w0,100

The order of output does not matter


Example 1:
Input:
    s: "cbaebabacd" p: "abc"

Output:
    [0,6]

Explanation:
    The substring with start index = 0 is "cba", which is an anagram of "abc"
    The substring with start index = 6 is "bac", which is an anagram of "abc"


Example 2:
Input:
    s: "abab" p: "ab"

Output:
    [0,1,2]

Explanation:
    The substring with start index = 0 is "ab", which is an anagram of "ab"
    The substring with start index = 1 is "ba", which is an anagram of "ab"
    The substring with start index = 2 is "ab", which is an anagram of "ab"
'''

from collections import Counter

class Solution:

    def find_anagrams(self, s, p):

        res = []
        p_counter = Counter(p)
        s_counter = Counter(s[:len(p)-1])

        for i in range(len(p) - 1, len(s)):
            s_counter[s[i]] += 1 # include the new char in the window

            if s_counter == p_counter: # This step is O(1), since there are at most 26 English letters
                res.append(i - len(p) + 1) # Append the starting index

            s_counter[s[i - len(p) + 1]] -= 1 # Decrease the count of oldest char in the window
            if s_counter[s[i - len(p) + 1]] == 0:
                del s_counter[s[i - len(p) + 1]] # Remove the count if it is 0


        return res





