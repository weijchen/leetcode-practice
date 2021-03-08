"""
19. Remove Nth Node From End of List
- Medium
- Linked List, Two Pointers
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Using reverse list
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        head = self.reverseList(head)
        prev, last = head, head.next

        if n == 1:
            if not last:
                return None
            else:
                head = last

        if not last:
            return head

        while n > 2:
            prev = prev.next
            last = last.next
            n -= 1

        if not last:
            head = prev
        else:
            prev.next = last.next
        return self.reverseList(head)

    def reverseList(self, head: ListNode) -> ListNode:
        last = None

        while head:
            tmp = head.next
            head.next = last
            last = head
            head = tmp

        return last


# Without using reverse list
# Utilize two pointers and the gap between pointers
# Time: O(n) -> makes one traversal of the list, length of the list
# Space: O(1)
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = slow = dummy = head

        for _ in range(n):
            fast = fast.next

        while fast:
            fast = fast.next
            dummy = slow
            slow = slow.next

        dummy.next = slow.next
        if slow == dummy:
            return head.next

        return head
