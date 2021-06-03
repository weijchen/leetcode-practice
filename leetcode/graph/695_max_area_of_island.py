"""
695. Max Area of Island
- Medium
- DFS, Array
- Link: https://leetcode.com/problems/max-area-of-island/
"""


# Solution 1: DFS
# Time: O(R * C) | Space: O(R * C), where R is the number of row and C is the number of column
class Solution:
    def __init__(self):
        self.ans = 0

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        def findIsland(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0 or (r, c) in seen:
                return 0

            seen.add((r,c))
            return 1 + findIsland(r-1, c) + findIsland(r+1, c) + findIsland(r, c-1) + findIsland(r, c+1)
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                self.ans = max(findIsland(r, c), self.ans)
        return self.ans
