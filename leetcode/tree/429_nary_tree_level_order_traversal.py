"""
429. N-ary Tree Level Order Traversal
- Medium
- BFS, DFS, Tree
- Link: https://leetcode.com/problems/n-ary-tree-level-order-traversal/
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


# Solution 1: BFS
# Time: O(N) | Space: O(N)
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ans = []
        if not root:
            return ans

        curLevel = [root]
        while curLevel:
            nextLevel = []
            curLevelNode = []
            for node in curLevel:
                curLevelNode.append(node.val)
                for child in node.children:
                    nextLevel.append(child)

            ans.append(curLevelNode)
            curLevel = nextLevel

        return ans


# Solution 2: BFS using python built-in queue
# Time: O(N) | Space: O(N)
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ans = []
        if not root:
            return ans

        queue = collections.deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                queue.extend(node.children)
            ans.append(level)
        return ans


# Solution 3: DFS
# Time: O(N) | Space: O(N)
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:

        def traverse_node(node, level):
            if len(result) == level:
                result.append([])
            result[level].append(node.val)
            for child in node.children:
                traverse_node(child, level + 1)

        result = []

        if root is not None:
            traverse_node(root, 0)
        return result
