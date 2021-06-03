"""
547. Number of Provinces
- Medium
- DFS, BFS, Union Find
- Link: https://leetcode.com/problems/number-of-provinces/
- 和 200 題一樣，透過調整 edge list 來找出相連的點
"""


# Solution 1: DFS (recursive)
# Time: O(N^2) | Space: O(N)
class Solution:
    def findConnect(self, isConnected, city):
        for conn in range(len(isConnected[city])):
            if isConnected[city][conn] == 1:
                isConnected[city][conn] = 0
                isConnected[conn][city] = 0
                self.findConnect(isConnected, conn)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ans = 0
        for city in range(len(isConnected)):
            if isConnected[city][city] == 1:
                ans += 1
                self.findConnect(isConnected, city)
        return ans


# Solution 2: DFS (iterative)
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [0] * len(isConnected)
        curr = 0
        province = 0

        def dfs():
            st = [curr]
            while st:
                curCity = st.pop()
                for i, connected in enumerate(isConnected[curCity]):
                    if visited[i] == 0 and connected == 1:
                        st.append(i)
                        visited[i] = 1

        while curr < len(visited):
            if visited[curr] == 0:
                province += 1
                dfs()
            curr += 1

        return province


# Solution 3: Union Find
# Time: O(N^2), to traverse the input matrix | Space: O(N), the size of parent array
# Time for union: O(N)
# Time for find: O(N)
class UnionFind:
    def __init__(self, length):
        self.parent = [x for x in range(length)]
        self.rank = [1 for i in range(length)]
        self.countDistinct = length

    def union(self, x, y):
        first = self.find(x)
        second = self.find(y)

        if first == second:
            return

        self.countDistinct -= 1

        # parent 是利用 rank 來做比較
        if self.rank[first] > self.rank[second]:
            self.parent[first] = second
        elif self.rank[first] < self.rank[second]:
            self.parent[second] = first
        else:
            self.parent[first] = second
            self.rank[first] += 1

    def find(self, x):
        # parent is itself
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        uf = UnionFind(len(isConnected))

        for city in range(1, len(isConnected)):
            for conn in range(city):
                if isConnected[city][conn]:
                    uf.union(city, conn)
        return uf.countDistinct

