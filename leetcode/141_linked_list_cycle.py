"""
141. Linked List Cycle
- Easy
- Hash Table, Linked List, Two Pointers
- Link: https://leetcode.com/problems/linked-list-cycle/
"""


# Solution 1: Hash Table
# Time: O(N) | Space: O(N)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        d = {}

        node = head
        while node:
            if node in d:
                return True
            else:
                d[node] = node.val
            node = node.next
        return False


# Solution 2: Two Pointers
# Time: O(N) -> length of cycle | Space: O(1)
# (2t - p - 1) % q = (t - p - 1) % q
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False

        slow, fast = head.next, head.next.next

        while slow and fast:
            if slow == fast:
                return True
            if not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return False
