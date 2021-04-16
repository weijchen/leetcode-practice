"""
15. 3Sum
- Medium
- Array, Two Pointers
- Link: https://leetcode.com/problems/3sum/
"""


# Time: O(N^2) -> twoSumII is O(N), which we call n times; sort the array is O(nlogn)
# Space: from O(logn) to O(N)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        if len(nums) < 3:
            return ans

        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i-1] != nums[i]:
                self.twoSumII(nums, i, ans)
        return ans

    def twoSumII(self, nums: List[int], i: int, ans: List[int]) -> List[List[int]]:
        l, r = i + 1, len(nums)-1
        while l < r:
            curSum = nums[l] + nums[r] + nums[i]
            if curSum < 0:
                l += 1
            elif curSum > 0:
                r -= 1
            else:
                ans.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                # to avoid using two continuous and identical numbers on the left
                while l < r and nums[l] == nums[l-1]:
                    l += 1
