"""
18. 4Sum
- Medium
- Array, Hash Table, Two Pointers
- Link: https://leetcode.com/problems/4sum/
"""


# Solution 1: Hash Table
# Time: O(N^{k-1}), where k is the length of a valid pair | Space: O(N)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def kSum(nums, target, k):
            if len(nums) == 0 or nums[0] * k > target or target > nums[-1] * k:
                return []
            if k == 2:
                return twoSum(nums, target)
            res = []
            for i in range(len(nums)):
                if i == 0 or nums[i-1] != nums[i]:
                    remains = nums[i+1:]
                    tmpKSum = kSum(remains, target - nums[i], k-1)
                    for _, set in enumerate(tmpKSum):
                        res.append([nums[i]] + set)
            return res

        def twoSum(nums, target):
            res = []
            s = set()
            for i in range(len(nums)):
                if len(res) == 0 or res[-1][1] != nums[i]:
                    if target - nums[i] in s:
                        res.append([target - nums[i], nums[i]])
                s.add(nums[i])
            return res

        nums.sort()
        return kSum(nums, target, 4)


# Solution 2: Two Pointers
# Time: O(N^{k-1}), where k is the length of a valid pair | Space: O(N)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def kSum(nums, target, k):
            res = []
            if len(nums) == 0 or nums[0] * k > target or target > nums[-1] * k:
                return res
            if k == 2:
                return twoSum(nums, target)
            for i in range(len(nums)):
                if i == 0 or nums[i-1] != nums[i]:
                    remains = nums[i+1:]
                    tmpKSum = kSum(remains, target - nums[i], k - 1)
                    for _, set in enumerate(tmpKSum):
                        res.append([nums[i]] + set)
            return res

        def twoSum(nums, target):
            res = []
            l, r = 0, len(nums)-1
            while l < r:
                _sum = nums[l] + nums[r]
                if _sum > target or (r < len(nums) - 1 and nums[r] == nums[r+1]):
                    r -= 1
                elif _sum < target or (l > 0 and nums[l] == nums[l-1]):
                    l += 1
                else:
                    res.append([nums[l], nums[r]])
                    l += 1
                    r -= 1
            return res

        nums.sort()
        return kSum(nums, target, 4)
