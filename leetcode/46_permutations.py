"""
46. Permutations
- Medium
- Backtracking
- Link: https://leetcode.com/problems/permutations/
"""


# Approach 1: Backtracking
# Time: O(N) | Space: O(N!) -> one has to keep N! solutions
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
