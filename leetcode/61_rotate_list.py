"""
61. Rotate List
- Medium
- Linked List, Two Pointers
- Link: https://leetcode.com/problems/rotate-list/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # Base case
        if not head:
            return head
        
        # Calculate list length
        l = 0
        dummy = head
        while dummy:
            l += 1
            dummy = dummy.next

        # if k is 0 or k equals the length of linked list -> return same list
        k %= l
        if k == 0:
            return head

        # Find new head and new tail
        step_to_walk = l - k
        fast, slow = head.next, head
        for _ in range(step_to_walk-1):
            fast = fast.next
            slow = slow.next

        # Connect two new pointers
        slow.next = None
        new_head = new_tail = fast
        while new_tail.next:
            new_tail = new_tail.next
        new_tail.next = head

        return new_head
