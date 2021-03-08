"""
234. Palindrome Linked List
- Easy
- Linked List, Two Pointers
- Link: https://leetcode.com/problems/palindrome-linked-list/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Save to list and compare (in other language, use two pointers)
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        _list = []
        while head:
            _list.append(head.val)
            head = head.next
        return _list == _list[::-1]
