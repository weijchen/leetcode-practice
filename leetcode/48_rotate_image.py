"""
48. Rotate Image
- Medium
- Array
- Link: https://leetcode.com/problems/rotate-image/
"""


# Approach 1: reverse, then use the pattern
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        curInd = 1
        colToRep = 0
        matrix.reverse()

        for i, row in enumerate(matrix):
            curInd = i + 1
            for j in range(i+1, len(matrix)):
                self.swap(matrix, i, curInd, j, colToRep)
                curInd += 1
            colToRep += 1
            if colToRep == len(matrix):
                break

    def swap(self, mat, x1, y1, x2, y2):
        mat[x1][y1], mat[x2][y2] = mat[x2][y2], mat[x1][y1]


# Approach 2: Reverse on Diagonal and then Reverse Left to Right
# Time: O(M), where M is the number of element in the matrix | Space: O(1)
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)
        self.reflect(matrix)

    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    def reflect(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][-j -
                                        1] = matrix[i][-j - 1], matrix[i][j]
