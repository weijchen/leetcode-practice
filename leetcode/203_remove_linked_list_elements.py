"""
203. Remove Linked List Elements
- Easy
- Linked List
- Link: https://leetcode.com/problems/remove-linked-list-elements/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Approach 1: sentinel node + two pointers + linked list remove
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        prev, curr = dummy, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next  # *** prev 可以不需要移動

        return dummy.next
