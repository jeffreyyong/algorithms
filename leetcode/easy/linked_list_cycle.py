'''
Given a linked list, determine if it has a cycle in it.

Follow up:
    can you solve it without using extra space?
'''

'''
Solution:

Imagine two runners running on a track at different speed. What happens when the track is actually a circle?

Algorithm

The space complexity can be reduced to O(1) by considering two pointers at different speed - a slow pointer
and a fast pointer. The slow pointer moves one step at a time while the fast pointer moves two steps at
a time

If there is no cycle in the list, the fast pointer will eventually reach the end and we can return false in this
case

Now consider a cyclic list and imagine the slow and fast pointers are two runners racing around a circle track.
The fast runner will eventually meet the slow runner. Why? Consider this case (we name it case A) - the fast
runner is just one step behind the slow runner. In the next iteration, they both increment one and two 
steps respectively and meet each other

How about other cases? For example, we have not considered cases where the fast runner is two or three steps behind
the slow runner yet. This is simple, because in the next or next's next iteration, this case will be reduced
to the case A mentioned above.

Complexity analysis:

    Time complexity O(n) Let us denote n as the total number of nodes in the linked list. To analyze its time complexity
    we consider the two cases separately

    - List has no cycle:
        The fast pointer reaches the end first and the run time depends on the list's length, which is O(n).

    - List has cycle:
        We break down the movement of the slow pointer into two steps, the non-cyclic part and the cyclic part

            1. The slow pointer takes "non-cyclic lengtt" steps to enter the cycle. At this point, the fast pointer 
                has already reached the cycle.
                Number of iterations = non-cyclic length = N

            2. Noth pointers are now in the cycle. Consider two runners running in a cycle - the fast runner 
                moves 2 steps while slow runner moves 1 step at a time. Since the speed difference is 1,
                it takes (distance between the 2 runners) divided by (difference of speed) loops for the fast
                runner to catch up with the slow runner. As the distance is at most "cyclic length K" and the speed
                difference is 1, we conclude that Number of iterations = almost "cyclic length K"

                Therefore, the worst case time complexity is O(N + K), which is O(n)


        space complexity: O(1), we only use two nodes (slow and fast) so the space complexity is O(1).

Also, use the pythonic way of doing "Easier to ask for forgiveness than permission"
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def has_cycle(self, head):
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False
