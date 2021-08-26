"""
973. K Closest Points to Origin
- Medium
- Array, Math, Divide and Conquer, Geometry, Sorting, Heap (Priority Queue), Quickselect
- Link: https://leetcode.com/problems/k-closest-points-to-origin/
"""


# Solution 1: Heap
# Time: O(N logN) | Space: O(N)
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = [((x**2 + y**2)**(1/2), [x, y])for x, y in points]
        heapq.heapify(dist)
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(dist)[1])
        return ans


# Solution 2: Sorting
# Time: O(N logN) | Space: O(N)
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = [((x**2 + y**2)**(1/2), [x, y])for x, y in points]
        dist.sort()
        return [i[1] for i in dist[:k]]
