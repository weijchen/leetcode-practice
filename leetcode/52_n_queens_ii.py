"""
52. N-Queens II
- Hard
- Backtracking
- Link: https://leetcode.com/problems/n-queens-ii/
"""


# Solution 1: DFS + backtracking
# Time: O(N!) | Space: O(N)
class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        diagonals = set()
        anti_diagonals = set()

        def is_valid(r, c):
            diagonals_idx = r - c
            anti_diagonals_idx = r + c
            return c not in cols and diagonals_idx not in diagonals and anti_diagonals_idx not in anti_diagonals

        def backtrack(r, c):
            if r == n:
                return 1
            ans = 0
            for col in range(n):
                diagonals_idx = r - col
                anti_diagonals_idx = r + col
                if not is_valid(r, col):
                    continue

                cols.add(col)
                diagonals.add(diagonals_idx)
                anti_diagonals.add(anti_diagonals_idx)

                ans += backtrack(r+1, col)

                anti_diagonals.remove(anti_diagonals_idx)
                diagonals.remove(diagonals_idx)
                cols.remove(col)
            return ans

        return backtrack(0, 0)
