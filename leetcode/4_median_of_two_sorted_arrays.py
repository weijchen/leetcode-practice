"""
4. Median of Two Sorted Arrays
- Hard
- Array, Binary Search, Divide and Conquer
- Link: https://leetcode.com/problems/median-of-two-sorted-arrays/
"""


# Solution 1: Binary Search
# Time: O(log(min(M, N))) | Space:O(1)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1, l2 = len(nums1), len(nums2)
        if l1 > l2:
            return self.findMedianSortedArrays(nums2, nums1)

        med = (l1 + l2 + 1) // 2

        l, r = 0, len(nums1) - 1
        while l <= r:
            m1 = (r - l) // 2 + l
            m2 = med - m1
            if nums1[m1] < nums2[m2-1]:
                l = m1 + 1
            else:
                r = m1 - 1

        m1 = l
        m2 = med - l
        c1 = max(float('-inf') if m1 <=
                 0 else nums1[m1-1], float('-inf') if m2 <= 0 else nums2[m2-1])

        if (l1 + l2) % 2 == 1:
            return c1

        c2 = min(float('inf') if m1 >= l1 else nums1[m1], float(
            'inf') if m2 >= l2 else nums2[m2])
        return (c1 + c2) / 2
