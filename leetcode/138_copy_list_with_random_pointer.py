"""
138. Copy List with Random Pointer
- Medium
- Hash Table, Linked List
- Link: https://leetcode.com/problems/copy-list-with-random-pointer/
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


# Solution 1: DFS (recursive)
# 把 Linked List 視作 Graph 來處理，想成是有多個 edge (next, random) 的 Node
# Time: O(V + E) | Space: O(V)
class Solution:
    def __init__(self):
        self.visited = {}

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head

        if head in self.visited:
            return self.visited[head]

        cloneNode = Node(head.val, None, None)

        self.visited[head] = cloneNode

        cloneNode.next = self.copyRandomList(head.next)
        cloneNode.random = self.copyRandomList(head.random)

        return cloneNode


# Solution 1: DFS (iterative)
# Time: O(V + E) | Space: O(V)
# 與 recursive 不同的是多了 createNewNode 的機制，其他重點相同，創建新節點並紀錄在 hash table
# hash table 紀錄的是 "舊節點 -> 新節點" 的資訊
class Solution:
    def __init__(self):
        self.visited = {}

    def createNewNode(self, node: 'Node'):
        if node:
            if node in self.visited:
                return self.visited[node]
            else:
                new_node = Node(node.val, None, None)
                self.visited[node] = new_node
                return new_node
        else:
            return None

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head

        old_node = head
        new_node = Node(old_node.val, None, None)
        self.visited[old_node] = new_node

        while old_node:
            new_node.next = self.createNewNode(old_node.next)
            new_node.random = self.createNewNode(old_node.random)

            old_node = old_node.next
            new_node = new_node.next

        return self.visited[head]
