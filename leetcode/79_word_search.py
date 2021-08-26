"""
79. Word Search
- Medium
- Array, Backtracking, Matrix
- Link: https://leetcode.com/problems/word-search/
"""


# Solution 1: Backtracking
# Time: O(N*3^L), at each position, we can only choose three direction to move | Space: O(L), where L is the length of the word to be matched
class Solution:
    def __init__(self):
        self.found = False

    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = [[0]*cols for _ in range(rows)]
        avai = [(r, c) for r in range(rows)
                for c in range(cols) if board[r][c] == word[0]]

        if not avai:
            return False

        def pre_check():
            """Checks whether board has all the characters required in word
            """
            chars_required = Counter(word)

            # Mark down the characters required, if they appear in the board
            for row in board:
                for char in row:
                    if char in chars_required and chars_required[char] > 0:
                        chars_required[char] -= 1

            # Ensure the board has all of the characters required for the word
            for count in chars_required.values():
                if count > 0:
                    return False
            return True

        def is_valid(r, c):
            return r >= 0 and r < rows and c >= 0 and c < cols and visited[r][c] == 0

        def findWord(word, r, c):
            if len(word) == 0:
                self.found = True
            else:
                for newR, newC in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                    if not is_valid(newR, newC):
                        continue
                    if board[newR][newC] == word[0]:
                        visited[newR][newC] = 1
                        findWord(word[1:], newR, newC)
                        visited[newR][newC] = 0

        # essential for the performance improvement
        if not pre_check():
            return False

        for r, c in avai:
            if self.found:
                return True
            visited[r][c] = 1
            findWord(word[1:], r, c)
            visited[r][c] = 0

        return self.found
