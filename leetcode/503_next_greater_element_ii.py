"""
496. Next Greater Element II
- Medium
- Array, Hash Table, Stack, Monotonic Stack
- Link: https://leetcode.com/problems/next-greater-element-ii/
"""


# Solution 1: Hash Table + Monotonic Stack
# Time: O(N) | Space: O(N)
# 要跑兩次 for-loop
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums)
        st = []

        for i in range(2):
            for idx, num in enumerate(nums):
                while st and num > nums[st[-1]]:
                    prev = st.pop()
                    ans[prev] = num

                st.append(idx)

        return ans
