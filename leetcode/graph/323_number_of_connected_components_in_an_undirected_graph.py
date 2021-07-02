"""
323. Number of Connected Components in an Undirected Graph
- Medium
- DFS, BFS, Union Find, Graph
- Link: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
"""


# Solution 1: Union Find
# Time: O(E*alpha(N)), where alpha() is the inverse Ackermann function | Space: O(V)
class UF:
    def __init__(self, n):
        self.parents = [_ for _ in range(n)]
        self.rank = [0 for _ in range(n)]
        self.size = n

    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb:
            return

        self.size -= 1

        if self.rank[pa] > self.rank[pb]:
            self.parents[pb] = pa
        elif self.rank[pb] > self.rank[pa]:
            self.parents[pa] = pb
        else:
            self.parents[pb] = pa
            self.rank[pa] += 1

    def find(self, item):
        if self.parents[item] != item:
            self.parents[item] = self.find(self.parents[item])
        return self.parents[item]


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UF(n)
        for (a, b) in edges:
            uf.union(a, b)

        return uf.size
