"""
74. Search a 2D Matrix
- Medium
- Array, Binary Search
- Link: https://leetcode.com/problems/search-a-2d-matrix/
"""


# Approach 1: Binary Search
# Time: O(logM + logN) = O(log(MN)), where M is the number of row and N is the number of col | Space: O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        minRow, maxRow = 0, len(matrix) - 1
        minCol, maxCol = 0, len(matrix[0]) - 1

        row = self.findRow(matrix, minRow, maxRow, target)

        while minCol <= maxCol:
            mid = (maxCol - minCol) // 2 + minCol
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                maxCol = mid - 1
            else:
                minCol = mid + 1
        return False

    def findRow(self, matrix, l, r, target):
        while l <= r:
            mid = (r - l) // 2 + l
            if matrix[mid][0] == target:
                return mid
            elif matrix[mid][0] > target:
                r = mid - 1
            else:
                l = mid + 1
        return r
