"""
628. Maximum Product of Three Numbers
- Easy
- Array, Math
- Link: https://leetcode.com/problems/maximum-product-of-three-numbers/
"""


# Solution 1: Math
# Time: O(NlogN) | Space: O(1)
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()

        multiOne = nums[0] * nums[1] * nums[-1]
        multiTwo = nums[-1] * nums[-2] * nums[-3]
        if multiOne >= multiTwo:
            return multiOne
        else:
            return multiTwo


# Solution 2: Manually Sort
# Time: O(N) | SpaceL O(1)
def maximumProduct(self, nums: List[int]) -> int:

    maxv = [- 1000, -1000, -1000]
    minv = [1000, 1000]

    for x in nums:
        if x > maxv[0]:
            if x <= maxv[1]:
                maxv[0] = x
            elif x <= maxv[2]:
                maxv[0] = maxv[1]
                maxv[1] = x
            else:
                maxv[0] = maxv[1]
                maxv[1] = maxv[2]
                maxv[2] = x

        if x < minv[1]:
            if x >= minv[0]:
                minv[1] = x
            else:
                minv[1] = minv[0]
                minv[0] = x

    if maxv[-1] > 0 and minv[0] * minv[1] > maxv[0] * maxv[1]:
        return minv[0] * minv[1] * maxv[2]
    else:
        return maxv[0] * maxv[1] * maxv[2]
