'''
Given a non-empty string `s`, may delete at most one character. Judge whether you can
make it a palindrome

Example 1:

Input: "aba"
Output: True

Example 2:

Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
'''

'''
Solution:

We can use the standard two-pointer approach that starts at the left and right
of the string and move inwards. Whenever there is a mismatch, we can either exclude
the character at the left or the right pointer. Can then take two remaining
substrings and compare against its reversed and see if either one is palindrome.

Time complexity: O(n)
Space complexity: O(n)
'''

class Solution:

    def valid_palindrome(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                one, two = s[left: right], s[left + 1:right + 1]
                return one == one[::-1] or two == two[::-1]
            left, right = left + 1, right - 1
        return True


    '''
    Approach #1: Brute Force [Time Limit Exceeded]

    Intuition and Algorithm:
    For each index `i` in the given string, let's remove that character, then check if the 
    resulting string is a palindrome. If it is (or if the original string was a palindrome), 
    then we'll return `True`

    Complexity Analysis:

        Time complexity: O(n^2) where N is the length of the string. We do the following N
        times: create a string of length N and iterate over it

        Space complexity: O(N), the space used by our candidate answer.
    '''

    def valid_palindrome_1(self, s):
        for i in range(len(s)):
            t = s[:i] + s[i+1:]
            if t == t[::-1]: return True

        return s == s[::-1]
