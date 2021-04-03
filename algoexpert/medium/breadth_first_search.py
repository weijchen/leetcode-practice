"""
Breadth-first Search
- Medium
"""


# Time: O(n) | Space: O(n)
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        # Write your code here.
        q = []
        if not self:
            return array
        else:
            q.append(self)

        ret = []
        curLevel, nextLevel = q, []
        while curLevel:
            for _ in curLevel:
                ret.append(_.name)
                nextLevel.extend(_.children)
            curLevel = nextLevel
            nextLevel = []

        return ret
