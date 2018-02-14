'''
Write a programme which takes as input an array of digits encoding a nonnegative decimal integer D
and updates the array to represent the integer D + 1. For example, if the input is <1,2,9> then you should
update the array to <1,3,0>. Your algorithm should work even if it is implemeted in a language that has
finite-precision arithmetic.
'''

'''
Solution:
A brute-force approach might be to convert the array of digits to the equivalent integer, increment that, 
and then convert the resulting value back to an array of digits. For example, if the array is <1,2,9>, we would
derive the integer 129, add one to get 130, then extract its digits to form <1,3,0> When implemented in a language
that imposes a limit on the range of values an integer type can take, this approach will fail inputs that encode
integers outside of the range.

We can avoid overflow issues by operating directly on the array digits. Specifically, we mimic the grade-school
algorithm for adding integers, which entails adding digits starting from the least significant digit and propogate
carries. If the result has an additional digit, e.g. 99 + 1 = 100. there is not enough storage in the array 
for the result. we need three digits to represent 100, but the input has only two digits.

For the given example, we would update 9 to 0 and carry-out 1. We update 2 to 3 (because of the carry-in). 
there is no carry-out, so we stop, the result is <1,3,0>

Complexity: 

The time complexity is O(n), where n is the length of A.
'''

class Solution:


    def plus_one(self, A):
        A[-1] += 1
        for i in reversed(range(1, len(A))):
            if A[i] != 10:
                break

            A[i] = 0
            A[i - 1] += 1

        if A[0] == 10:
            # There is a carry out, so we need one more digit to store the result.
            # A slick way to do this is to apped a 0 at the end of the array
            # and update the first entry to 1
            A[0] = 1
            A.append(0)

        return A
