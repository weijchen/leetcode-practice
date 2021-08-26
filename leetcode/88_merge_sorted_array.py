"""
88. Merge Sorted Array
- Easy
- Array, Two Pointers, Sorting
- Link: https://leetcode.com/problems/merge-sorted-array/
"""


# Solution 1: Merge and Sort
# Time: O((n+m)log(n+m)) | Space: O(1)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(n):
            nums1[i + m] = nums2[i]

        # Sort nums1 list in-place.
        nums1.sort()


# Solution 2: Extra space with Three Pointers
# Time: O(m + n) | Space: O(m)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1Copy = nums1[:m]

        p1, p2 = 0, 0

        for p in range(m+n):
            if p2 >= n or (p1 < m and nums1Copy[p1] <= nums2[p2]):
                nums1[p] = nums1Copy[p1]
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1


# Solution 3: No extra space with Three Pointers
# Time: O(m + n) | Space: O(1)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        p1, p2 = m - 1, n - 1

        for p in range(m + n - 1, -1, -1):
            if p2 < 0:
                break

            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
