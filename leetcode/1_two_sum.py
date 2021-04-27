"""
1. Two Sum
- Easy
- Array, Hash Table
- Link: https://leetcode.com/problems/two-sum/
"""

# Approach 1: One-Pass Hash Table
# Time: O(n) | Space: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in dic:
                dic[num] = i
            else:
                return [dic[n], i]
