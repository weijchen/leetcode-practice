"""
252. Meeting Rooms
- Easy
- Sort
- Link: https://leetcode.com/problems/meeting-rooms/
"""


# Solution 1: Sorting
# Time: O(NlogN) | Space: O(1)
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(len(intervals)-1):
            prevEnd, currStart = intervals[i][1], intervals[i+1][0]
            if prevEnd > currStart:
                return False
        return True
