"""
200. Number of Islands
- Medium
- DFS, BFS, Union Find
- Link: https://leetcode.com/problems/number-of-islands/
"""


# Solution 1: DFS (recursively)
# Time: O(R * C), where R is # of row and C is # of col | Space: O(R * C), if the grid is filled with 1
class Solution:
    def findIsland(self, grid, row, col):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == '0': return
        grid[row][col] = '0'
        self.findIsland(grid, row-1, col)
        self.findIsland(grid, row+1, col)
        self.findIsland(grid, row, col-1)
        self.findIsland(grid, row, col+1)
    
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    ans += 1
                    self.findIsland(grid, r, c)  
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
