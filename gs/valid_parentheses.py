'''
Given a string containing just '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''

'''
Analysis:
Use a stack to store the chars, scan from the 1st to the last char in string s.


( [ { are free to push in the stack.
When meets ) if stack top is (, then pop (.
When meets ] if stack top is [, then pop [.
When meets } if stack top is {, then pop {.
Otherwise return false

In the end, if the stack is empty, return true. (to handle "()(" case )
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
