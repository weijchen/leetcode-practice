"""
51. N-Queens
- Hard
- Array, Backtracking
- Link: https://leetcode.com/problems/n-queens/
"""


# Solution 1: DFS + backtracking
# Time: O(N!) | Space: O(N^2)
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        empty_board = [["."] * n for _ in range(n)]
        cols = set()
        diagonals = set()
        anti_diagonals = set()

        def is_valid(r, c):
            diagonals_idx = r - c
            anti_diagonals_idx = r + c
            return c not in cols and diagonals_idx not in diagonals and anti_diagonals_idx not in anti_diagonals

        def create_board(state):
            board = []
            for row in state:
                board.append("".join(row))
            return board

        def backtrack(r, state):
            if r == n:
                ans.append(create_board(state))
                return True

            for col in range(n):
                diagonals_idx = r - col
                anti_diagonals_idx = r + col
                if not is_valid(r, col):
                    continue

                cols.add(col)
                diagonals.add(diagonals_idx)
                anti_diagonals.add(anti_diagonals_idx)
                state[r][col] = 'Q'

                backtrack(r+1, state)

                state[r][col] = '.'
                anti_diagonals.remove(anti_diagonals_idx)
                diagonals.remove(diagonals_idx)
                cols.remove(col)

        backtrack(0, empty_board)
        return ans
