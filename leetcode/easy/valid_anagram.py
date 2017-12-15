'''
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
'''

import collections

class Solution:

    # def is_anagram(self, s, t):
    #     dict1, dict2 = {}, {}
    #     for item in s:
    #         dict1[item] = dict1.get(item, 0) + 1
    #     for item in t:
    #         dict2[item] = dict2.get(item, 0) + 1
    #     return dict1 == dict2


    # def is_anagram(self, s, t):
    #     dict1, dict2 = [0]*26, [0]*26
    #     for item in s:
    #         dict1[ord(item) - ord("a")] += 1

    #     for item in t:
    #         dict2[ord(item) - ord("a")] += 1
    #     return dict1 == dict2

    # def is_anagram(self, s, t):
    #     return sorted(s) == sorted(t)


    # # Using collections. Is collections fast enough?
    # def is_anagram(self, s, t):
    #     return collections.Counter(s) == collections.Counter(t)

    # The fastest solution. Because it's just O(n) and there's only one solution
    def is_anagram(self, s, t):
        letters = list('abcdefghijklmnopqrstuvwxyz')

        for l in letters:
            if s.count(l) != t.count(l):
                return False

        return True
    
    
