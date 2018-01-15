'''
Remove all elements fmor a linked list of integers that have value val.

Example:
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
'''

class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def remove_elements(self, head, val):
        dummy = ListNode(-1)
        dummy.next = head
        next = dummy

        while next != None and next.next != None:
            if next.next.val == val:
                next.next = next.next.next
            else:
                next = next.next

        return dummy.next
