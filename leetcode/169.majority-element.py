#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
# Solution 1: Sorting
# Time: O(NlogN) | Space: O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)// 2]

# @lc code=end


# Solution 2: Boyer-Moore Voting Algorithm
# Time: O(N) | Space: O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            else:
                count += (-1 if num is not candidate else 1)
        return candidate
