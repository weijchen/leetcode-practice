"""
46. Permutations
- Medium
- Backtracking
- Link: https://leetcode.com/problems/permutations/
"""


# Time: O(N) | Space: O(N!) -> one has to keep N! solutions
class Solution:
    def __init__(self):
        self.ans = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.helper(nums)
        return self.ans

    def helper(self, arr, path=[]):
        for idx in range(len(arr)):
            curNum = arr[idx]
            remain = arr[:idx] + arr[idx + 1:]
            tmpPath = [_ for _ in path]
            tmpPath.append(curNum)

            if len(remain) > 0:
                self.helper(remain, tmpPath)
            else:
                self.ans.append(tmpPath)
