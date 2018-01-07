'''
Merge two sorted linked lists and return it as  anew list. The new list should be 
made by splicing together the nodes of the first two lists.

Example:
    Input: 1->2->4, 1->3->4
    Output: 1->1->2->3->4->4
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

'''
Can recursively define the result of a merge operation on two lists as the following

list1[0] + merge(list1[1:], list2)  if list1[0] < list2[0]
list2[0] + merge(list1, list2[1:])  if otherwise

Namely the smaller of the two lists's heads plus the result of a merge on the rest 
of the elements

Algorithm:
Model the recurrence directly, first accounting for edge cases. Specifically, if either of
l1 or l2 is initially null, there is no merge to perform, so simply return the non-null list.

Otherwise, determine which of l1 and l2 has a smaller head, and recursively set the next
value for that head to the next merge result. Given that both lists are null-terminated
the recursion will eventually terminate.

Complexity Analysis:
Time complexity: O(n + m)
Because each recursive call increments the pointer to l1 or l2 by one (approachning the 
dangling null at the end of each list), there will be exactly one call to merge_two_lists
per element in each list. Therefore, the time complexity is linear in the combined
size of the lists.

Space complexity: O(n + m)
The first call to merge_two_lists does not return until the ends of both l1 and l2 have
been reached, so n + m stack rames consume O(n + m) space.
'''

class Solution:

    # iteratively
    def merge_two_lists(self, l1, l2):
        dummy = cur = ListNode(0)

        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next

    # recursively
    def merge_two_lists(self, l1, l2):

        if not l1 or not l2:
            return l1 or l2

        if l1.val < l2.val:
            l1.next = self.merge_two_lists(l1.next, l2)
            return l1

        else:
            l2.next = self.merge_two_lists(l1, l2.next)
            return l2
