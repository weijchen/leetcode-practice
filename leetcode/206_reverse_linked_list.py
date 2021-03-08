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

# Time: O(n)
# Space O(1)
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        last = None

        while head:
            # save tmp node
            tmp = head.next
            head.next = last
            last = head
            head = tmp

        return last
