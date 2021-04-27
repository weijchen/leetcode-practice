"""
73. Set Matrix Zeroes
- Medium
- Array
- Link: https://leetcode.com/problems/set-matrix-zeroes/
"""



class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        numRow = len(matrix)
        numCol = len(matrix[0])

        for r in range(numRow):
            for c in range(numCol):
                if matrix[r][c] == 0:
                    self.replace(matrix, r, c, numRow, numCol)

        for m in range(numRow):
            for n in range(numCol):
                if matrix[m][n] == None:
                    matrix[m][n] = 0

        return matrix

    def replace(self, matrix, row, col, numRow, numCol):
        for r in range(numRow):
            if matrix[r][col] != 0:
                matrix[r][col] = None

        for c in range(numCol):
            if matrix[row][c] != 0:
                matrix[row][c] = None
