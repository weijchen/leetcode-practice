"""
78. Subsets
- Medium
- Array, Backtracking, Bit Manipulation
- Link: https://leetcode.com/problems/subsets/
"""


# Approach 1: Backtracking
# Time: O(N * 2^N) | Space: O(1), since we only use the ans array for returning answer
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        self.helper(nums, ans)
        return ans

    def helper(self, arr, ans, comb=[]):
        ans.append(comb)
        for idx in range(len(arr)):
            remain = arr[idx+1:]
            newComb = comb + [arr[idx]]
            self.helper(remain, ans, newComb)


# Approach 2: Bit Manipulation
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = []

        for i in range(2**n, 2**(n + 1)):
            # generate bitmask, from 0..00 to 1..11
            bitmask = bin(i)[3:]

            # append subset corresponding to that bitmask
            output.append([nums[j] for j in range(n) if bitmask[j] == '1'])

        return output


# Practice 1
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtracking(start, depth, comb):
            ans.append(comb[:])

            for idx in range(start, len(nums)):
                comb.append(nums[idx])
                backtracking(idx + 1, depth + 1, comb)
                comb.pop()

        backtracking(0, 0, [])

        return ans
