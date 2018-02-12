'''
Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot 
be planted in adjacent plots - they woulud compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), 
and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: True

Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: False
'''

'''
We need to justify greedy solution.


Call a plot ready if the very first flower is allowed to be planted there.

'''

class Solution:

    '''
    Python solution
    '''

    def can_place_flowers(self, flowerbed, n):
        for i, x in enumerate(flowerbed):
            if (not x and (i == 0 or flowerbed[i - 1] == 0) 
                and (i == len(flowerbed) - 1 or flowerbed[i+1] == 0)):

                n -= 1
                flowerbed[i] = 1
        return n <= 0

    '''
    Approach #1 Single Scan [Accepted]

    The solution is very simple. We can find out the extra maximum number of flowers, `count`, that can be planted
    for the given `flowerbed` arragement. To do so, we can traverse over all the elements of the `flowerbed` and 
    find out those elements which are 0 (implying an empty position). For every such element, we check if its both
    adjacent positions are also empty. If so, we can plant a flower at the current position without violating
    the no-adjacent-flowers-rule. For the fisrt and last elements, we need not check the previous and next adjacent positions

    If the `count` obtained is greater than or equal to n, the required number of flowers to be planted, we can plant
    n flowers in the empty spaces, otherwise not.

    Complexity Analysis:

        Time complexity: O(n). A single scan of the `flowerbed` array of size n is done.
        Space complexity: O(1)
    '''

    def can_place_flowers_1(self, flowerbed, n):
        i, count = 0, 0

        while (i < len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed) - 1
                                                                          or flowerbed[i + 1] == 0):

                flowerbed[i] = 1
                count += 1

            i += 1

        return count >= n



    '''
    Approach #2 Optimized [Accepted]

    Algorithm

    Instead of finding the maximum value of count that can be obtained, as done in the last approach, 
    we can stop the process of checking the positions for planting the flowers as soon as count becomes 
    equal to n. Doing this leads to an optimization of the first approach. If count never becomes equal to n,
    n flowers can't be planted at the empty positions.
    '''


    def can_place_flowers_2(self, flowerbed, n):

        i, count = 0, 0

        while (i < len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed) - 1
                                                                          or flowerbed[i + 1] == 0):
                flowerbed[i + 1] = 1
                count += 1

            if count >= n:
                return True
            i += 1

        return False


