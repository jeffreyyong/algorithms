import unittest

from add_two_numbers_linked_list import *

class AddTwoNumbersLinkedList(unittest.TestCase):

    def test_delete_min_max(self):
        a = ListNode(2)
        b = ListNode(4)
        c = ListNode(3)
        a.next = b
        b.next = c

        d = ListNode(5)
        e = ListNode(6)
        f = ListNode(4)
        d.next = e
        e.next = f

        h = ListNode(7)
        i = ListNode(0)
        j = ListNode(8)
        h.next = i
        i.next = j

        actual = add_two_numbers(a, d)
        self.assertEqual(actual.val, h.val)
        self.assertEqual(actual.next.val, h.next.val)
        self.assertEqual(actual.next.next.val, h.next.next.val)
