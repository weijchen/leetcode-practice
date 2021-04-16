"""
48. Rotate Image
- Medium
- Array
- Link: https://leetcode.com/problems/rotate-image/
"""


# Approach 1: Find matrix pattern (aka. Layer by layer)
# Time: O(m*n), where m*n is the total number of element in the matrix | Soace: O(m*n)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        startCol = 0
        endCol = len(matrix[0])
        startRow = 0
        endRow = len(matrix)

        while startCol < endCol and startRow < endRow:
            for c in range(startCol, endCol):
                ans.append(matrix[startRow][c])

            for r in range(startRow+1, endRow):
                ans.append(matrix[r][endCol-1])

            for c in reversed(range(startCol, endCol-1)):
                if startRow != endRow-1:
                    ans.append(matrix[endRow-1][c])

            for r in reversed(range(startRow+1, endRow-1)):
                if startCol != endCol-1:
                    ans.append(matrix[r][startCol])

            startCol += 1
            endCol -= 1
            startRow += 1
            endRow -= 1

        return ans
