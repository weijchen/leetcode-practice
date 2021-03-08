"""
2. Add Two Numbers
- Medium
- Linked List, Math, Recursion
"""


# Definition for singly-linked list.
# Time: O(max(n, m))
# Space: O(max(n, m))
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = tail = ListNode(-1)
        s = 0

        while l1 or l2 or s:
            s += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            tail.next = ListNode(s % 10)

            s //= 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            tail = tail.next
        return dummy.next
