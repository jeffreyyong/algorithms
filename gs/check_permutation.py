'''
Check permutation:

Given two strings, write a method to decide if one is a permutationn of the other.
'''

# O(n)

from collections import Counter

class Solution:

    def check_permutation(self, str1, str2):
        if len(str1) != len(str2):
            return False

        counter = Counter()
        for c in str1:
            counter[c] += 1
        for c in str2:
            if counter[c] == 0:
                return False
            counter[c] -= 1
        return True
