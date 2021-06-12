"""
561. Array Partition I
- Easy
- Array
- Link: https://leetcode.com/problems/array-partition-i/
"""


# Solution 1: Array
# Time: O(NlogN) | Space: O(1)
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0

        for i in range(0, len(nums), 2):
          ans += nums[i]
        return ans
