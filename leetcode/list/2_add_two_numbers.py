"""
2. Add Two Numbers
- Medium
- Linked List, Math, Recursion
- Link: https://leetcode.com/problems/add-two-numbers/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Approach 1: Two pointers
# Time: O(max(N, M)) | Space: O(max(N, M)), where N and M is the length of l1 and l2
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        prehead = head = ListNode()
        p1, p2, carry = l1, l2, 0

        while p1 or p2 or carry:
            _sum = (p1.val if p1 else 0) + (p2.val if p2 else 0) + carry
            toAdd, carry = _sum % 10, _sum >= 10
            head.next = ListNode(toAdd)
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
            head = head.next
        return prehead.next
