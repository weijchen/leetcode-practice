"""
36. Valid Sudoku
- Medium
- Hash Table
- Link: https://leetcode.com/problems/valid-sudoku/
"""


# Solution 1: Hash Table
# Time: O(N^2) | Space: O(N^2)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.is_valid_row(board) and self.is_valid_col(board) and self.is_valid_area(board)

    def is_valid_area(self, board):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                area = [board[x][y]
                        for x in range(i, i+3) for y in range(j, j+3)]
                if not self.is_valid_unit(area):
                    return False
        return True

    def is_valid_row(self, board):
        for row in board:
            if not self.is_valid_unit(row):
                return False
        return True

    def is_valid_col(self, board):
        for col in zip(*board):
            if not self.is_valid_unit(col):
                return False
        return True

    def is_valid_unit(self, area):
        unit = [_ for _ in area if _ is not '.']
        return len(unit) == len(set(unit))
