'''
Delete a node in the middle of a singly linked list.
Given access only to that node
'''
class Solution:

    def delete_node(self, node):
        node.val = node.next.val
        node.next = node.next.next
