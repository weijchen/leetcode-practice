"""
15. 3Sum
- Medium
- Array, Two Pointers
- Link: https://leetcode.com/problems/3sum/
"""


# Solution 1: Hash Table + Two Pointers
# Time: O(N^2) -> twoSum is O(N), which we call n times; sort the array is O(N*logN) | Space: O(N)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        if len(nums) < 3:
            return ans
        nums.sort()

        for i, num in enumerate(nums):
            if num > 0:
                break
            if i == 0 or nums[i-1] != nums[i]:
                self.twoSum(nums, i, ans)
        return ans

    def twoSum(self, nums, first, ans):
        l, r = first + 1, len(nums) - 1
        while l < r:
            _sum = nums[first] + nums[l] + nums[r]
            if _sum == 0:
                ans.append([nums[first], nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
            elif _sum > 0:
                r -= 1
            else:
                l += 1
