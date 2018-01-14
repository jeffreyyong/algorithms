'''
We are playing the Guess game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1,1,0):
    -1: My number is lower
    1: My number is higher
    0: Congrats! You got it!

Example:
'''

'''
Solution:

Can apply Binary Search to find the given number. Start with the mid number. We pass the number to the
guess function. If it returns a -1, it implies that the guessed number is larger than the required one

Thus, we use Binary Search for numbers lower than itself. Similarly, if it returns a 1, use Binary Search
for numbers higher than itself.
'''

class Solution:

    def guess_number(self, n):

        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) / 2
            if guess(mid) == 1:
                lo = mid + 1
            else:
                hi = mid
        return lo
