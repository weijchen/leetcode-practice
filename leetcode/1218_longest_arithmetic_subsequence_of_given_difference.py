"""
1218. Longest Arithmetic Subsequence of Given Difference
- Medium
- DP
- Link: https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/
- 解題: 需紀錄值 -> Hash Table
        Input Size 為 10^5，N^2 會超過 10^6，故存在 O(N) 的解法 -> DP
        依序搜尋是否前面出現過 num - difference 的值，有的話增加 num 的計數器
"""


# Solution 1: Hash Table + DP
# Time: O(N) | Space: O(N)
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        for num in arr:
            if num - difference in dp.keys():
                dp[num] = dp[num - difference] + 1
            else:
                dp[num] = 1

        return max(dp.values())


# with better python api calls
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
      dp = {}
      for a in arr:
        dp[a] = dp.get(a - difference, 0) + 1
      return max(dp.values())
