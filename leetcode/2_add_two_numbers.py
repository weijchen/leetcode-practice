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


# Approach 1: two pointers + math + iteration
# Time: O(max(n, m))
# Space: O(max(n, m))
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(None)
        cur = dummy
        carry = 0
        p1 = l1
        p2 = l2

        while p1 or p2 or carry:
            p1_val = p1.val if p1 else 0
            p2_val = p2.val if p2 else 0
            _sum, carry = (p1_val + p2_val +
                           carry) % 10, (p1_val + p2_val + carry) // 10
            cur.next = ListNode(_sum)
            cur = cur.next
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
        return dummy.next
