"""
496. Next Greater Element I
- Easy
- Array, Hash Table, Stack, Monotonic Stack
- Link: https://leetcode.com/problems/next-greater-element-i/
"""


# Solution 1: Hash Table + Monotonic Stack
# Time: O(M + N) | Space: O(M + N)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = dict()
        st = []
        
        for num in nums2:
            while st and num > st[-1]:
                prev = st.pop()
                d[prev] = num
            st.append(num)

        while st:
            prev = st.pop()
            d[prev] = -1
            
        return [d[n] for n in nums1]
