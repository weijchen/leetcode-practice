"""
24. Swap Nodes in Pairs
- Medium
- Linked List Recursion
- Link: https://leetcode.com/problems/swap-nodes-in-pairs/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Swap values
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is not None and head.next is not None:
            n1, n2 = head, head.next

            while n1 and n2:
                tmp = n1.val
                n1.val = n2.val
                n2.val = tmp
                n1 = n2.next
                if n1 is not None:
                    n2 = n2.next.next

            return head

        else:
            return head


# Without swapping values
# 利用單一個 node 來做定向，後續再透過調整原先鏈結做結構上的調整
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        prehead = ListNode(-1)
        prev = prehead

        while head and head.next:
            first_node, second_node = head, head.next

            prev.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            prev = first_node
            head = first_node.next

        return prehead.next
