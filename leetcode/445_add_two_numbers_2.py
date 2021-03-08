"""
445. Add Two Numbers II
- Medium
- Linked List
- Link: https://leetcode.com/problems/add-two-numbers-ii/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)

        prehead = ListNode(-1)
        prev = prehead
        carry = 0

        while l1 or l2:
            tmp = (l1.val if l1 is not None else 0) + \
                (l2.val if l2 is not None else 0) + carry

            if tmp >= 10:
                tmp -= 10
                carry = 1
            else:
                carry = 0

            prev.next = ListNode(tmp)
            prev = prev.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry:
            prev.next = ListNode(1)

        return self.reverseList(prehead.next)

    def reverseList(self, node: ListNode):
        last = None

        while node:
            tmp = node.next
            node.next = last
            last = node
            node = tmp

        return last
