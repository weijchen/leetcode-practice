"""
46. Permutations
- Medium
- Backtracking
- Link: https://leetcode.com/problems/permutations/
"""


# Approach 1: Backtracking
# Time: O(N!) | Space: O(N!) -> one has to keep N! solutions
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.helper(nums, ans)
        return ans

    def helper(self, arr, ans, path=[]):
        # exist condition
        if len(arr) == 0:
            ans.append(path)

        # iterate current dimension
        for idx in range(len(arr)):
            remain = arr[:idx] + arr[idx + 1:]
            nextPath = path + [arr[idx]]
            self.helper(remain, ans, nextPath)


# Practice 1
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        used = [0] * len(nums)

        def backtracking(used, perm):
            if len(perm) == len(nums):
                ans.append(perm[:])

            for idx in range(len(nums)):
                if used[idx] == 1:
                    continue
                used[idx] = 1
                perm.append(nums[idx])
                backtracking(used, perm)
                perm.pop()
                used[idx] = 0

        backtracking(used, [])
        return ans
