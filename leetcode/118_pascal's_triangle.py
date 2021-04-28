"""
118. Pascal's Triangle
- Easy
- Array
- Link: https://leetcode.com/problems/pascals-triangle/
"""


# Approach 1: Math + Array (reverse)
# Time: O(N^2), for-loop and sum | Space: O(N^2)
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        cur = [1]
        for num in range(numRows):
            ans.append(cur)
            tmpCur = cur + [0]
            tmpCur_rev = tmpCur[::-1]
            cur = [sum(i) for i in zip(tmpCur, tmpCur_rev)]
        return ans


# Approach 2: DP
# Time: O(N^2) | Space: O(N^2)
# 1
# 1 1
# 1 2 1   <- row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]
# 1 3 3 1
# 1 4 6 4 1
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for row_num in range(numRows):
            row = [None for _ in range(row_num+1)]
            row[0], row[-1] = 1, 1

            for j in range(1, len(row)-1):
                row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]
            triangle.append(row)
        return triangle
