"""
25. Reverse Nodes in k-Group
- Hard
- Linked List, Recursion
- Link: https://leetcode.com/problems/reverse-nodes-in-k-group/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Solution 1: Recursive
# Time: O(N) | Space: O(N/k)
class Solution:
    def reverseLinkedList(self, head, k):
        prev, ptr = None, head
        while k:
            next_node = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = next_node

            k -= 1

        return prev

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        count = 0
        ptr = head

        while count < k and ptr:
            ptr = ptr.next
            count += 1

        if count == k:
            reversedHead = self.reverseLinkedList(head, k)

            head.next = self.reverseKGroup(ptr, k)
            return reversedHead
        return head
