"""
77. Combinations
- Medium
- Backtracking
- Link: https://leetcode.com/problems/combinations/
"""


# Approach 1: Backtracking
# Time: O(k * nCk) | Space: O(k * nCk)
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = [_ for _ in range(1, n + 1)]
        ans = []
        self.helper(arr, ans, k)
        return ans

    def helper(self, lis, ans, k, comb=[]):
        # exist condition
        if len(comb) == k:
            ans.append(comb)
        else:
            # iterate current dimension
            for idx, ele in enumerate(lis):
                nextComb = comb + [ele]
                remain = lis[idx+1:]
                self.helper(remain, ans, k, nextComb)


# Approach 1-better: Backtracking
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(first=1, curr=[]):
            # if the combination is done
            if len(curr) == k:
                output.append(curr[:])
            for i in range(first, n + 1):
                # add i into the current combination
                curr.append(i)
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()

        output = []
        backtrack()
        return output


# Practice 1
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def backtracking(start, comb):
            if len(comb) == k:
                ans.append(comb[:])
                return

            for i in range(start, n+1):
                comb.append(i)
                backtracking(i+1, comb)
                comb.pop()

        backtracking(1, [])
        return ans
