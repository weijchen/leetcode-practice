"""
90. Subsets II
- Medium
- Array, Backtracking
- Link: https://leetcode.com/problems/subsets-ii/
- The key to this problem is how to remove/avoid duplicates efficiently.
"""


# Solution 1: backtracking
# Time: O(2^N) | Space: O(N)
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        def backtracking(s, comb):
            ans.append(comb[:])
            for idx in range(s, len(nums)):
                # 用來避免出現相同組合的解答
                # For the same depth, among the same numbers, only the first number can be used.
                if idx > s and nums[idx] == nums[idx-1]:
                    continue
                comb.append(str(nums[idx]))
                backtracking(idx+1, comb)
                comb.pop()

        backtracking(0, [])
        return ans
