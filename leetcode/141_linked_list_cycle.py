"""
141. Linked List Cycle
- Easy
- Linked List, Two Pointers
- Link: https://leetcode.com/problems/linked-list-cycle/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Two Pointers
# Time: O(n) -> length of cycle
# Space: O(1)
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False

        fast, slow = head.next.next, head.next

        while fast and slow:
            if fast == slow:
                return True
            else:
                if not fast.next:
                    return False
                fast = fast.next.next
                slow = slow.next

        return False
