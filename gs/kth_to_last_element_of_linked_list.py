'''
Implement an algorithm to find the nth to last element of a singly linked list
'''

class Solution:

    def kth_element_from_last(self, k):

        p1 = self.head
        p2 = self.head

        if k != 0:
            for i in range(k):
                p2 = p2.next
            # over flow k is greater than linked list length
            if p2 is None:
                return None

        while p2.next is not None:
            p2 = p2.next
            p1 = p1.next

        # since p2 - p1 is the k, now p1 position is the kth from last node

        return p1.val
