"""
658. Find K Closest Elements
- Medium
- Array, Two Pointers, Binary Search, Sorting, Heap (Priority Queue)
- Link: https://leetcode.com/problems/find-k-closest-elements/
"""


# Solution 1: Two Pointers
# Time: O(N) | Space: O(1)
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if x < arr[0]:
            return arr[:k]
        elif x > arr[-1]:
            return arr[-k:]
        else:
            l, r = 0, len(arr) - 1
            n = len(arr) - k

            while n != 0:
                if abs(arr[l] - x) <= abs(arr[r] - x):
                    r -= 1
                else:
                    l += 1
                n -= 1
            return arr[l:r+1]
