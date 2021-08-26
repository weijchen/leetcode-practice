"""
215. Kth Largest Element in an Array
- Medium
- Array, Divide and Conquer, Sorting, Heap (Priority Queue), Quickselect
- Link: https://leetcode.com/problems/kth-largest-element-in-an-array/
"""


# Solution 1: Heap
# Time: O(N log N) | Space: O(N)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        revNum = [(-num, num) for num in nums]
        heapq.heapify(revNum)

        count = 0
        ans = 0
        while count < k:
            ans = heapq.heappop(revNum)
            count += 1
        return ans[1]


# Solution 2: Heap (optimized)
# Time: O(N log N) | Space: O(1)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        count = 0
        newK = len(nums) - k
        ans = 0
        while count <= newK:
            ans = heapq.heappop(nums)
            count += 1
        return ans
