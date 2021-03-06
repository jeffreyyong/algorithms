'''
Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one 
more letter at a random position.

Find the letter that was added in t.
'''


class Solution:

    def find_the_difference(self, s, t):
        sum1 = sum(map(ord, [c for c in s]))
        sum2 = sum(map(ord, [c for c in t]))

        return chr(sum2-sum1)
