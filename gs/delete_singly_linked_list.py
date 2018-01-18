'''
Given a pointer to a node to be deleted, delete the node. Note that we don't have
pointer to head node.

A simple solution is to traverse the linked list until you find the node you want to delete.
But this solution requires pointer to the head node which contradicts the problem statement.
'''

'''
Approach: Swap with Next Node [Accepted]

The usual way of deleting node `node` from a linkd list is to modify the `next` pointer 
of the node before it, to point to the node after it.

Since we do not hvae access to the node before the one we want to delete, we cannot 
modify the `next` pointer of that node in any way. Instead, we have to replace the value
of the node we want to delete with the value in the node after it, and then delete the node 
after it.


Because we know that the node we want to delete is not the tail of the list, we can guarantee
that this approach is possible
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def delete_node(self, node):
        node.val = node.next.val
        node.next = node.next.next


