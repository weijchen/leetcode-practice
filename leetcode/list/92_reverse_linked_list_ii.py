"""
92. Reverse Linked List II
- Medium
- Linked List
- Link: https://leetcode.com/problems/reverse-linked-list-ii/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solution: Linked List (Iterative)
# Time: O(N) | Space: O(1)
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head:
            return None

        curr, prev = head, None
        while left > 1:
            prev = curr
            curr = curr.next
            left, right = left-1, right-1

        tail, conn = curr, prev

        while right:
            tmpNode = curr.next
            curr.next = prev
            curr, prev = tmpNode, curr
            right -= 1

        if conn:
            conn.next = prev
        else:
            head = prev

        tail.next = curr
        return head
