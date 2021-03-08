"""
83. Remove Duplicates from Sorted List
- Easy
- Linked List
- Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # Base cases
        if not head or not head.next:
            return head

        fast, slow = head.next, head
        while fast:
            if slow.val == fast.val:
                # fast meets the end
                if fast.next == None:
                    slow.next = None
                fast = fast.next
            else:
                slow.next = fast
                slow, fast = fast, fast.next

        return head
