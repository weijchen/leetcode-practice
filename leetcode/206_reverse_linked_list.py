"""
206. Reverse Linked List
- Easy
- Linked List
- Link: https://leetcode.com/problems/reverse-linked-list/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solution 1: Linked List
# Time: O(n) | Space O(1)
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None

        while head:
            tmpNode = head.next
            head.next = prev
            head, prev = tmpNode, head

        return prev
