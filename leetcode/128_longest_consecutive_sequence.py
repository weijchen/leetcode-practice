"""
128. Longest Consecutive Sequence
- Medium
- Array, Hash Table, Union Find
- Link: https://leetcode.com/problems/longest-consecutive-sequence/
"""

# Solution 1: Array Sorting
# Time: O(NlogN) | Space: O(1)


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      if len(nums) == 0:
            return 0

        nums.sort()
        
        ret = 0
        cur = 1
        
        for idx in range(1, len(nums)):
            if nums[idx] - nums[idx-1] == 1:
                cur += 1
            elif nums[idx] - nums[idx-1] == 0:
                continue
            else:
                ret = max(ret, cur)
                cur = 1
        
        return max(ret, cur)
        
        

# Solution 2: HashSet
# Time: O(N) | Space: O(N)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        num_set = set(nums)
        
        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                
                longest_streak = max(longest_streak, current_streak)
        
        return longest_streak
