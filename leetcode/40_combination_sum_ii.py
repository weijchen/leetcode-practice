"""
40. Combination Sum II
- Medium
- Array, Backtracking
- Link: https://leetcode.com/problems/combination-sum-ii/
"""


# Approach 1: Backtracking + deal with repeating element
# Time: O(2^N), in the worst case, the algo will exhaust all possible combinations from the input array
# Space: O(N)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        self.helper(candidates, target, 0, ans, [])
        return ans

    def helper(self, arr, target, start, ans, comb):
        if target == 0:
            ans.append(comb)
        elif target > 0:
            for idx in range(start, len(arr)):
                if idx > start and arr[idx] == arr[idx-1]:
                    continue

                if arr[idx] > target:
                    break

                newComb = comb + [arr[idx]]
                newTarget = target - arr[idx]
                newStart = idx + 1
                self.helper(arr, newTarget, newStart, ans, newComb)


# Practice 1
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        ans = []

        def backtracking(nums, start, remaining, comb):
            if remaining == 0:
                ans.append(comb[:])
                return

            for idx in range(start, len(nums)):
                if idx > start and nums[idx] == nums[idx-1]:
                    continue

                if nums[idx] > target:
                    break

                if remaining >= nums[idx]:
                    comb.append(nums[idx])
                    backtracking(nums, idx+1, remaining - nums[idx], comb)
                    comb.pop()

        if candidates:
            backtracking(candidates, 0, target, [])
        return ans
