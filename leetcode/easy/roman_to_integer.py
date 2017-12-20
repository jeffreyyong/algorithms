'''
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
'''

'''
The trick is that last letter is always added. Except the last one, if one letter is less 
than its latter one, this letter is subtracted.
'''


class Solution:

    def roman_to_int(self, s):
        roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

        z = 0

        for i in range(0, len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]:
                z -= roman[s[i]]
            else:
                z += roman[s[i]]

        return z + roman[s[-1]]


    def roman_to_int(self, s):
        roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

        res, i = 0, 0
        for i in range(len(s)):
            curr, nxt = s[i], s[i+1:i+2]
            if nxt and roman[curr] < roman[nxt]:
                res -= roman[curr]
            else:
                res += roman[curr]
        return res

