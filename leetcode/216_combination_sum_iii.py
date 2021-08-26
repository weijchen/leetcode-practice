"""
216. Combination Sum III
- Medium
- Array, Backtracking
- Link: https://leetcode.com/problems/combination-sum-iii/
"""


# Solution 1: Backtracking
# Time: C(m, k) = C(9, K) = 9! / k! / (9-k)! | Space: O(K)
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def backtracking(s, remaining, comb):
            if remaining == 0 and len(comb) == k:
                ans.append(comb[:])
                return
            for num in range(s, 10):
                if len(comb) >= k:
                    continue
                if remaining >= num:
                    comb.append(num)
                    backtracking(num+1, remaining - num, comb)
                    comb.pop()

        backtracking(1, n, [])

        return ans
