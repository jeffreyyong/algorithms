'''
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede"

Note:
The vowels does not include the letter "y"
'''

'''
Solution:
Using two pointer solutions for finding out where the vowels are, then swap it
'''


class Solution:

    def reverse_vowels(self, s):

        vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        s = list(s)
        x = 0
        y = len(s) - 1

        while x < y:
            while x < y and s[x] not in vowel:
                x += 1
            while x < y and s[y] not in vowel:
                y -= 1
            s[x], s[y] = s[y], s[x]
            x += 1
            y -= 1

        return "".join(s)
