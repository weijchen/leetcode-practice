"""
39. Combination Sum
- Medium
- Array, Backtracking
- Link: https://leetcode.com/problems/combination-sum/
"""


# Approach 1: Backtracking
# Time: O(N^T/M), where N is the length of array, T is the target value and M is the minimal value in the array | Space: O(T/M)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(start, comb, _sum):
            if _sum == target:
                ans.append(list(comb))
                return
            elif _sum > target:
                return

            for i in range(start, len(candidates)):
                comb.append(candidates[i])
                backtrack(i, comb, _sum + candidates[i])
                comb.pop()

        backtrack(0, [], 0)
        return ans


# Solution 2: DFS
# Time: O(N^T/M), where N is the length of array, T is the target value and M is the minimal value in the array | Space: O(T/M)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(cur, remain, comb):
            if cur == target:
                ans.append(comb)
            else:
                for idx, each in enumerate(remain):
                    if cur + each <= target:
                        dfs(cur+each, remain[idx:], comb + [each])

        for idx, cand in enumerate(candidates):
            dfs(cand, candidates[idx:], [cand])

        return ans
