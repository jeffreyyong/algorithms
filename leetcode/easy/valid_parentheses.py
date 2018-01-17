'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the 
input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

'''

class Solution:

    def is_valid(self, s):
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}

        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                # Used to check that the parentheses should start with the beginning one first
                # Pop the corresponding matching parentheses along the way
                if stack == [] or dict[char] != stack.pop():
                    return False

        # Make sure that the stack should be empty in the end, so that all of them are being matched
        return True if len(stack) == 0 else False
