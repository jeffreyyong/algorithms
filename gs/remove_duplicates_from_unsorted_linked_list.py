'''
Write code to remove duplicates from an unsorted linked list
'''

class Solution:

    def delete_duplicate(self):

        cur = self.head
        dict = {}
        prev = None
        while cur is not None:

            # If the node has been seen
            if cur.val in dict:
                # The previous arrow will skip the next node and point to the next next node
                prev.next = cur.next
            else:
                dict[cur.val] = True
                prev = cur
            cur = cur.next

