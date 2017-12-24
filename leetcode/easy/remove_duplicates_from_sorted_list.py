'''
Given a sorted linked list, delete all duplicates such taht each element appear only once

For example,
Given 1 -> 1 -> 2, return 1 -> 2
Given
'''

class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    '''
    This is a simple problem that merely tests the manipulation of list node pointers.
    Because the input list is sorted, can determine if a node is a duplicate by 
    comparing its value to the node after it in the list. If it is a duplicate, 
    change the next pointer fo the current node so that it skips the next node and points
    directly to the one after the next node.

    Complexity Analysis:
    Because each ndoe in the list is checked exactly once to determine if it is a duplicate 
    or not, the total run time O(n), where n is the number of nodes in the list

    Space complexity is O(1) since no additional space is used


    Correctness:

        We can prove the correctness of this code by defining a loop invariant. A loop invariant
        is condition that is before and after eveyr iteration of the loop.

        In this case, a loop invariant that helps us prove correctnes is this:
            All nodes in the lsit up to the pointer current do not contain duplicate elements

        We can prove that this condition is indeed a loop invariant by induction, Before going 
        into the loop, current points to the head of the list, Therefore, the part of the 
        list up to current contains only the head. And so it can contain any duplicate elements
        Now suppose current is now pointing to some node in the list (but not the last element)

        and the part of the list up to current contains no duplicate elements. 
        After another loop iteration, one of two things happen

        1. current.next was a duplicate of current. In this case, the duplicate node at 
            current.next is deleted, and current stays pointing to the same node as before
            Therefore, the condition still holds,; there are still no duplicates up to current.

        2. current.next was no a duplicate current (and, becaues the list is sorted, current.next
            is also not a duplicate of any other element appearing before current). In this case
            current moves forward one step to point to current.next. Threfore, the condition
            still holds; there are no duplicates up to current.

        As the last iteration of the loop, current must point to the last element, because
        afterwards, current.next = null. Therefore, after the loop ends, all elements up
        to the last element do not contian duplicates
    '''

    def delete_duplicates(self, head):

        '''
        :type head: ListNode
        :rtype: ListNode
        '''

        cur = head

        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next # skip duplicated node
            cur = cur.next # not duplicate of current node, move to next node
        return head


    def delete_duplicates_1(self, head):

        '''
        :type head: ListNode
        :rtype: ListNode
        '''

        if not head:
            return []

        p = head

        while(p.next):
            if (p.val == p.next.val):
                p.next = p.next.next
            else:
                p = p.next # no duplicate, move to the next node

        return head
