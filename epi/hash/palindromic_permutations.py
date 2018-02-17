"""
A palindrome is a string that reads the same forwards and backwards eg. "level", "rotator" and "foobaraboof".

Write a progrm to test whether the letters forming a string can be permuted to form a palindrome. For example,
"edified" can be permuted to form "deified".

Hint: Find a simple characterization of strings that can be permuted to form a palindrome.
"""

"""
Solution:

A brute force approach is to compute all permutations of the string, and test each one for palindromicity. 
This has a very high time complexity. Examining the approach in more detail, one thing to note is that 
if a string begins with say 'a', then we only need consider permutations that end with 'a'. This observation
can be used to prune the permutation-based algorithm. 

A more powerful conclusion is that all charactesr must occur in pairs for a string to be permutable into a palindrome,
with one exception, if the string is of odd length. For excample, for the string "edified", which is of odd length 7
there are two 'e', two 'd', two 'i' and one 'f' - this is enough to guarantee that "edified" can be permuted into 
a palindrome.

More formally, if the string is of even length, a necessary and sufficient condition for it to be a paindrome is that each 
character in the string appears an even number of times. If the length is odd, all but one character should appear an even
number of times. Both these cases are covered by testing that at most one character appears an odd number of times, which 
can be checked using a hashtable mapping characters to frequencies.

Time complexity is O(n), where n is the length of the string. The space complexity is O(c), where c is the number of
distinct characters appearing in the string.
"""

import collections

class Solution:

    def can_form_palindrome(self, s):
        # A string can be permuted for form a palindrome if and only if the number
        # of chars whose frequencies is odd is at most 1.
        return sum(v % 2 for v in collections.Counter(s).values()) <= 1
