"""
119. Pascal's Triangle II
- Easy
- Array
- Link: https://leetcode.com/problems/pascals-triangle-ii/
"""


# Approach 1: Array
# Time: O(N^2) | Space: O()
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        curRow = 0
        row = [1]

        while curRow < rowIndex:
            tmpRow = row + [0]
            row = [sum(i) for i in zip(tmpRow, tmpRow[::-1])]
            curRow += 1
        return row
