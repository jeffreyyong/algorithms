'''
Given two strings `s` and `t`, determine if they are isomorphic.
Two strings are isomorphic if the characters in `s` can be replaced to get `t`

All occurrences of a character must be replaced with another character while preserving the order
of characters. No two characters may map to the same charcter but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.
'''

class Solution:

    def is_isomorphic_fastest(self, s, t):
        d1, d2 = {}, {}

        for i , val in enumerate(s):
            d1[val] = d1.get(val, []) + [i]

        for i, val in enumerate(t):
            d2[val] = d2.get(val, []) + [i]

        return sorted(d1.values()) == sorted(d2.values())


    def is_isomorphic(self, s, t):
        return len(set(zip(s,t))) == len(set(s)) == len(set(t))
