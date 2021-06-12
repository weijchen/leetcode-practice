"""
1. Two Sum
- Easy
- Array, Hash Table
- Link: https://leetcode.com/problems/two-sum/
"""


# Solution 1: One-Pass Hash Table
# Time: O(n) | Space: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numPair = dict()

        for idx, num in enumerate(nums):
            if num in numPair.keys():
                return [idx, numPair[num]]
            else:
                numPair[target - num] = idx
