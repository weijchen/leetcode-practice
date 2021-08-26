"""
1578. Minimum Deletion Cost to Avoid Repeating Letters
- Medium
- Array, String, DP, Greedy
- Link: https://leetcode.com/problems/minimum-deletion-cost-to-avoid-repeating-letters/
- 思路：搜尋連續相同的數，取出最大值剩餘計入回傳值
"""


# Solution 1: Greedy
# Time: O(N) | Space: O(N)
class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        cand = [cost[0]]
        cur = s[0]
        _sum = 0

        for idx, (char, char_cost) in enumerate(zip(s, cost)):
            if idx == 0:
                continue

            if char == cur:
                cand.append(char_cost)
            else:
                if len(cand) >= 2:
                    _sum += (sum(cand) - max(cand))
                cand = [char_cost]
                cur = char

        return _sum + 0 if len(cand) < 2 else _sum + sum(cand) - max(cand)
