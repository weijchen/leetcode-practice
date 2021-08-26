"""
445. Add Two Numbers II
- Medium
- Linked List
- Link: https://leetcode.com/problems/add-two-numbers-ii/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Solution 1: Two Pointers + reverse linked list
# Time: O(max(N, M)) | Space: O(max(N, M)), where N and M is the length of l1 and l2
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        prehead = head = ListNode()
        p1 = self.reverse(l1)
        p2 = self.reverse(l2)
        carry = 0
        while p1 or p2 or carry:
            _sum = (p1.val if p1 else 0) + (p2.val if p2 else 0) + carry
            toAdd, carry = _sum % 10, _sum // 10
            head.next = ListNode(toAdd)
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
            head = head.next

        return self.reverse(prehead.next)

    def reverse(self, node):
        prev = None
        while node:
            tmp = node.next
            node.next = prev
            prev, node = node, tmp

        return prev


# Solution 2: Math
# Time: O(max(N, M)) | Space: O(max(N, M))
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum1, sum2 = 0, 0

        while l1 != None:
            sum1 *= 10
            sum1 += l1.val
            l1 = l1.next
        while l2 != None:
            sum2 *= 10
            sum2 += l2.val
            l2 = l2.next

        prehead = head = ListNode()
        for char in str(sum1 + sum2):
            head.next = ListNode(int(char))
            head = head.next

        return prehead.next
