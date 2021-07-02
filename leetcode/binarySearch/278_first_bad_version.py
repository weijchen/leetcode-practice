"""
278. First Bad Version
- Easy
- Binary Search, Interactive
- Link: https://leetcode.com/problems/first-bad-version/
"""


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):


# Solution 1: Binary Search
# Time: O(logN) | Space: O(1)
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n

        while l < r:
            m = (r - l) // 2 + l
            if isBadVersion(m):
                r = m
            else:
                l = m + 1

        return l
