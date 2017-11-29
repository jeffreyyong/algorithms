'''
Question:
Given a string, determine if a permutation of the string could form a palindrome.

For example,
"code" -> False, "aab" -> True, "carerac" -> True.
'''

'''
Answer:
The idea is to iterate over string, adding current character to set if set doesn't cantain
that character, or removing current character from set if set contains it.

When the iteration is finished, just retrun set.size()==0 || set.size()==1

set.size()==0 corresponds to the sutuation when there are even number of any character in the string
set.size()==1 corresponds to the fact that there are even number of any character except one.

'''

import collections

class Solution:

    def can_permutate_palindrome(self, s):

        setA = set()
        for i in s:
            if i in setA:
                setA.remove(i)
            else:
                setA.add(i)
        return len(setA) <= 1

