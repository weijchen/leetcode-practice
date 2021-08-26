"""
253. Meeting Rooms II
- Medium
- Sort, Heap, Greedy
- Link: https://leetcode.com/problems/meeting-rooms-ii/
- 重點是要紀錄最近要空下來的會議室
"""


# Solution 1: Greedy + Heap
# Time: O(NlogN) | Space: O(N)
# Sorting: O(NlogN)
# extract-min operation on a heap: O(logN) -> take N meetings in the worst case -> O(NlogN)
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        rooms = []
        intervals.sort(key=lambda x: x[0])
        heapq.heappush(rooms, intervals[0][1])

        for i in intervals[1:]:
            if i[0] >= rooms[0]:
                heapq.heappop(rooms)

            heapq.heappush(rooms, i[1])

        return len(rooms)
