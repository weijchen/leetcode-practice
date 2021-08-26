"""
347. Top K Frequent Elements
- Medium
- Hash Table, Heap
- Link: https://leetcode.com/problems/top-k-frequent-elements/
"""


# Solution 1: Hash Table + Heap
# Time: O(NlogN) | Space: O(N + k), N elements and a heap with k elements
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        if len(nums) == 0:
            return ans

        d = Counter(nums)
        count = k
        h = [(-v, k) for k, v in d.items()]
        heapq.heapify(h)
        while count > 0:
            ans.append(heapq.heappop(h)[1])
            count -= 1
        return ans
