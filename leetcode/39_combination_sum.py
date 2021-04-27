"""
39. Combination Sum
- Medium
- Array, Backtracking
- Link: https://leetcode.com/problems/combination-sum/
"""


# Approach 1: Backtracking
# Time: O(N^T/M), where N is the length of array, T is the target value and M is the minimal value in the array | Spacee: O(T/M)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()
        self.helper(candidates, ans, target)
        return [list(_) for _ in list(ans)]

    def helper(self, arr, ans, target, comb=[]):
        if sum(comb) == target:
            ans.add(tuple(sorted(comb)))
        elif sum(comb) < target:
            for idx, ele in enumerate(arr):
                newComb = comb + [ele]
                self.helper(arr, ans, target, newComb)


# Approach 2: Backtracking + Pruning(*** important for improving backtracking algo.)
# Time: O(N^T/M), where N is the length of array, T is the target value and M is the minimal value in the array | Spacee: O(T/M)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()
        ans = []
        self.helper(candidates, ans, 0, target)
        return ans

    # 只利用該元素 index (含)以後 的 array，避免出現重複的組合
    def helper(self, arr, ans, index, target, comb=[]):
        if target == 0:
            ans.append(comb)
        elif target > 0:
            for idx in range(index, len(arr)):
                newComb = comb + [arr[idx]]
                newTarget = target - arr[idx]
                self.helper(arr, ans, idx, newTarget, newComb)
