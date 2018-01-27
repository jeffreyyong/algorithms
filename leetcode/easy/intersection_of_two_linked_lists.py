'''
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3

being to intersect at c1.


Notes:

    - If the two linekd lists have on intersection at all, return null
    - The linked lists must retain their origianl structure after the function returns
    - May assume there are no cycles anywhere in the entire linked structure
    - Code should probably run in O(n) time and use only O(1) memory.
'''

class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    '''
    Approach #3(two pointers)

    - Maintain two pointers pA and pB initialised at the head of A and B, respectively. Then let them both
      traverse through the lists, one node at a time.
    '''

    def get_intersection_node_two_pointers(self, head_a, head_b):
        if head_a is None or head_b is None:
            return None

        # 2 pointers
        pa = head_a 
        pb = head_b

        while pa is not pb:
            # if either pointer hits the end, switch head and continue the second traversal
            # if not hit the end, just move on to next

            pa = head_b if pa is None else pa.next
            pb = head_a if pb is None else pb.next

        return pa # only 2 ways to get out of the loop, they meet or both hit the end=None

    # the idea is if you switch head, the possible difference between length would be countered.
    # On the second traversal, they either hit or miss.
    # If they meet, pa or pb would be the node we are looking for
    # if they didn't meet, they will hit the end at the same iteration, pb == pa == None, return either one of them is the same, None

