"""
560. Subarray Sum Equals K
- Medium
- Array, Hash Table
- Link: https://leetcode.com/problems/subarray-sum-equals-k/
"""


# Solution 1: Hash Table
# Time: O(N) | Space: O(N)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {0: 1}
        curSum = 0
        count = 0

        for num in nums:
            curSum += num
            toFind = curSum - k
            count += d.get(toFind, 0)
            d[curSum] = d.get(curSum, 0) + 1

        return count
