"""
1465. Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
- Medium
- Array, Greedy, Sorting
- Link: https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/
"""


# Solution 1: Greedy
# Time: O(NlogN) + O(MlogM), for sorting N horizontal cuts and M vertical cuts; O(N), for remain operations | Space: O(1)
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts = [0] + sorted(horizontalCuts) + [h]
        verticalCuts = [0] + sorted(verticalCuts) + [w]
        maxWidth = 0
        for i in range(0, len(horizontalCuts)-1):
            maxWidth = max(maxWidth, horizontalCuts[i+1] - horizontalCuts[i])

        maxHeight = 0
        for i in range(0, len(verticalCuts)-1):
            maxHeight = max(maxHeight, verticalCuts[i+1] - verticalCuts[i])
        ret = (maxWidth * maxHeight) % (pow(10, 9) + 7)
        return ret
