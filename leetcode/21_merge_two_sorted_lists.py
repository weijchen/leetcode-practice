"""
21. Merge Two Sorted Lists
- Easy
- Linked List, Recursive
- Link: https://leetcode.com/problems/merge-two-sorted-lists/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Space: O(1)
    # Time: O(min(m,n)) where m = len(l1) and n = len(l2)
    def mergeTwoLists_Iterative(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = tail = ListNode(-1)

        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        tail.next = l1 or l2

        return dummy.next

    # Space: O(m + n) where m = len(l1) and n = len(l2)
    # Time: O(min(m,n))
    def mergeTwoLists_Recursive(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val <= l2.val:
            l1.next = self.mergeTwoLists_Recursive(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists_Recursive(l1, l2.next)
            return l2
