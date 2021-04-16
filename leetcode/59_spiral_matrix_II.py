"""
59. Spiral Matrix II
- Medium
- Array
- Link: https://leetcode.com/problems/spiral-matrix-ii/
"""


# Time: O(n^2), since we iterate over n * n matrix | Space: O(1)
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0 for _ in range(n)] for _ in range(n)]
        cur = 1

        startRow = 0
        endRow = n
        startCol = 0
        endCol = n

        while startRow < endRow and startCol < endCol:
            for c in range(startCol, endCol):
                if ans[startRow][c] == 0:
                    ans[startRow][c] = cur
                    cur += 1
            for r in range(startRow + 1, endRow - 1):
                if ans[r][endCol - 1] == 0:
                    ans[r][endCol - 1] = cur
                    cur += 1
            for c in reversed(range(startCol, endCol)):
                if ans[endRow - 1][c] == 0:
                    ans[endRow - 1][c] = cur
                    cur += 1
            for r in reversed(range(startRow + 1, endRow - 1)):
                if ans[r][startCol] == 0:
                    ans[r][startCol] = cur
                    cur += 1

            startRow += 1
            endRow -= 1
            startCol += 1
            endCol -= 1
        return ans
