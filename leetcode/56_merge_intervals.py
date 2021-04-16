"""
48. Rotate Image
- Medium
- Array
- Link: https://leetcode.com/problems/rotate-image/
"""


# Sort
# Time: O(NlogN), for sorting | Space: O(logN), for sorting
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort()

        _prev = intervals[0]
        if len(intervals) == 1:
            return [_prev]

        for e in intervals[1:]:
            _next = e

            if (_next[0] < _prev[0] and _next[1] < _prev[0]) or (_next[0] > _prev[1] and _next[1] > _prev[1]):
                ans.append(_prev)
                _prev = _next
            else:
                _prev = [min(_prev[0], _next[0]), max(_prev[1], _next[1])]

        if _prev != _next:
            ans.append(_prev)
        else:
            ans.append(_next)
        return ans


# Prettier code
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # otherwise, there is overlap, so we merge the current and previous
                # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
