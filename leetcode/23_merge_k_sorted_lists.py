"""
23. Merge K Sorted Lists
- Hard
- Linked List, Divide and Conquer, Heap, Merge Sort
- Link: https://leetcode.com/problems/merge-k-sorted-lists/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solution 1: Sorting
# Time: O(N logN) | Space: O(N)
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        l = []
        for _list in lists:
            while _list:
                l.append(_list.val)
                _list = _list.next

        l.sort(reverse=True)

        head = ListNode(None)
        prehead = head

        while l:
            head.next = ListNode(l.pop())
            head = head.next

        return prehead.next


# Solution 2: Heap
# Time: O(N logN) | Space: O(N)
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        h = []

        for _list in lists:
            while _list:
                h.append(_list.val)
                _list = _list.next

        heapq.heapify(h)

        head = ListNode(None)
        prehead = head
        while h:
            head.next = ListNode(heapq.heappop(h))
            head = head.next

        return prehead.next
