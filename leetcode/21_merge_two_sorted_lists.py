"""
21. Merge Two Sorted Lists
- Easy
- Linked List, Recursive
- Link: https://leetcode.com/problems/merge-two-sorted-lists/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Solution 1: Two Pointers + List
# Time: O(max(N, M)) | Space: O(max(N, M)), where N and M is the length of l1 and l2
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        list1, list2 = [], []

        while l1:
            list1.append(l1.val)
            l1 = l1.next
        while l2:
            list2.append(l2.val)
            l2 = l2.next

        prehead = head = ListNode()
        while list1 or list2:
            if not list1:
                toAdd = list2.pop(0)
            elif not list2:
                toAdd = list1.pop(0)

            if list1 and list2:
                toAdd = list1.pop(0) if list1[0] <= list2[0] else list2.pop(0)
            head.next = ListNode(toAdd)
            head = head.next

        return prehead.next


# Solution 2: Two Pointers (Iterative)
# Time: O(max(N, M)) | Space: O(1), where N and M is the length of l1 and l2
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        prehead = head

        while l1 and l2:
            if l1.val >= l2.val:
                head.next = l2
                l2 = l2.next
            else:
                head.next = l1
                l1 = l1.next
            head = head.next

        head.next = l1 or l2

        return prehead.next


# Solution 3: Two Pointers (Recursive)
# Time: O(max(N, M)) | Space: O(max(N, M)), where N and M is the length of l1 and l2 (recursive stack)
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
