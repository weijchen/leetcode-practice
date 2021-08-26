"""
47. Permutation III
- Medium
- Backtracking
- Link: https://leetcode.com/problems/permutations-ii/
"""


# Solution 1: Backtracking (with used array)
# Time: O(N!) | Space: O(N!)
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        used = [0] * len(nums)
        nums.sort()

        def backtracking(used, perm):
            if len(perm) == len(nums):
                ans.append(perm[:])
                return

            for idx in range(0, len(nums)):
                if used[idx] == 1:
                    continue
                if idx > 0 and nums[idx] == nums[idx-1] and used[idx-1]:
                    continue

                used[idx] = 1
                perm.append(nums[idx])
                backtracking(used, perm)
                perm.pop()
                used[idx] = 0

        backtracking(used, [])

        return ans


# Solution 1: Backtracking (without used array)
class Solution:
    def permuteUnique(self, nums):
        res = []
        nums.sort()
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
