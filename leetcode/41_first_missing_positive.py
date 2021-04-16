"""
41. First Missing Positive
- Hard
- Array
- Link: https://leetcode.com/problems/first-missing-positive/
"""


# Approach 1: Index List Table || Index Hash Table
# Time: O(n) | Space: O(n)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        table = [1 for k in range(len(nums))]

        for num in nums:
            if num <= len(nums) and num > 0:
                if table[num-1] == 1:
                    table[num-1] = 0

        cur = 0
        for i, b in enumerate(table):
            if b == 1:
                return i+1
            else:
                cur = i+1
        return 1 if cur == 0 else cur+1
