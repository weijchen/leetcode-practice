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
