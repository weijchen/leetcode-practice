#
# @lc app=leetcode id=147 lang=python3
#
# [147] Insertion Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        curr = head

        while curr:
            prev = dummy

            while prev.next and prev.next.val < curr.val:
                prev = prev.next
            
            next = curr.next
            curr.next = prev.next
            prev.next = curr

            curr = next
        
        return dummy.next


        
# @lc code=end

