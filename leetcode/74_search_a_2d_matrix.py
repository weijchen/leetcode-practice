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
        numRow, numCol = len(matrix), len(matrix[0])
        lRow, rRow = 0, numRow
        lCol, rCol = 0, numCol
        r = self.searchRow(matrix, lRow, rRow, target)
        if r == -1:
            return False
        else:
            return self.searchCol(matrix[r], lCol, rCol, target)

    def searchRow(self, matrix, lRow, rRow, target):
        if lRow < rRow:
            pivot_row = (rRow + lRow) // 2
            _min = matrix[pivot_row][0]
            _max = matrix[pivot_row][-1]
            if target < _min:
                return self.searchRow(matrix, lRow, pivot_row, target)
            elif target > _max:
                return self.searchRow(matrix, pivot_row + 1, rRow, target)
            else:
                return pivot_row
        else:
            return -1

    def searchCol(self, arr, lCol, rCol, target):
        if lCol < rCol:
            pivot = (rCol + lCol) // 2

            if target < arr[pivot]:
                return self.searchCol(arr, lCol, pivot, target)
            elif target > arr[pivot]:
                return self.searchCol(arr, pivot + 1, rCol, target)
            else:
                return True
        else:
            return False
