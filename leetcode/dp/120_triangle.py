"""
120. Triangle
- Medium
- Array, DP
- Link: https://leetcode.com/problems/triangle/
"""


# Solution 1: DP
# Time: O(N^2) | Space: O(N)
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = []
        for row_id, row in enumerate(triangle):
            if row_id == 0:
                cur = [row[0]]
            else:
                cur = [0] * len(row)
                for idx, num in enumerate(row):
                    num1 = dp[row_id-1][idx-1] if idx-1 >= 0 else float('inf')
                    num2 = dp[row_id-1][idx] if idx + \
                        1 < len(row) else float('inf')
                    cur[idx] = min(num1, num2) + num

            dp.append(cur)

        return min(dp[-1])
