"""
733. Flood Fill
- Easy
- DFS
- Link: https://leetcode.com/problems/flood-fill/
"""


# Solution 1: DFS (recursive)
# Time: O(R*C) | Space: O(R*C), where R is the number of row and C is the number of column
# 可通過和原點顏色的比較來降低空間複雜度 -> O(1)
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        seen = set()

        def dfs(r, c, val):
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c] != val or (r, c) in seen:
                return
            seen.add((r, c))
            image[r][c] = newColor
            dfs(r+1, c, val)
            dfs(r-1, c, val)
            dfs(r, c+1, val)
            dfs(r, c-1, val)

        dfs(sr, sc, image[sr][sc])

        return image


# Solution 2: DFS (iterative)
# Time: O(R*C) | Space: O(R*C), where R is the number of row and C is the number of column
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        st = [[sr, sc]]
        N, M = len(image), len(image[0])
        curr = image[sr][sc]
        if curr == newColor:
            return image
        while st:
            x, y = st.pop()
            image[x][y] = newColor
            if x > 0 and image[x-1][y] == curr:
                st.append([x-1, y])
            if y > 0 and image[x][y-1] == curr:
                st.append([x, y-1])
            if x < N-1 and image[x+1][y] == curr:
                st.append([x+1, y])
            if y < M-1 and image[x][y+1] == curr:
                st.append([x, y+1])
        return image
