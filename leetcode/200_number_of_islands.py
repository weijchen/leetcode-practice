"""
200. Number of Islands
- Medium
- DFS, BFS, Union Find
- Link: https://leetcode.com/problems/number-of-islands/
"""


# Solution 1: DFS
# Time: O(R * C) | Space: O(R * C), if the grid is filled with 1
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        if not grid:
            return ans
        row, col = len(grid), len(grid[0])

        def dfs(r, c):
            grid[r][c] = '2'

            for di, dj in (1, 0), (0, 1), (-1, 0), (0, -1):
                newR, newC = r + di, c + dj

                if 0 <= newR < row and 0 <= newC < col and grid[newR][newC] == '1':
                    dfs(newR, newC)

        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    dfs(r, c)
                    ans += 1

        return ans


# Solution 2: Union Find, aka Disjoint Set
# Time: O(R * C) | Space: O(R * C), if the grid is filled with 1
class UF:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.n = n
        self.size = n

    def union(self, i, j):
        pi, pj = self.find(i), self.find(j)
        if pi != pj:
            self.size -= 1
            self.parants[pj] = pi

    def find(self, i):
        # 如果 parent 不是自己，代表有 predecessor，開始做 traverse
        if i != self.parents[i]:
            self.parents[i] = self.find(self.parents[i])
        return self.parants[i]


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        d = dict()
        idx = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    d[i, j] = idx
                    idx += 1
        uf = UF(idx)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    if i > 0 and grid[i-1][j] == '1':
                        uf.union(d[i-1, j], d[i, j])
                    if j > 0 and grid[i][j-1] == '1':
                        uf.union(d[i, j-1], d[i, j])
        return uf.size
