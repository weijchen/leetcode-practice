"""
1509. Minimum Difference Between Largest and Smallest Value in Three Moves
- Medium
- Array, Greedy, Sorting
- Link: https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/
- 思路：替換一定是從排序後的頭三及尾三元素進行置換
- a1, a2, a3, a4, ..., an-3, an-2, an-1, an
- 換最大三、換最大二及最小、換最大一及最小二、換最小三，四種情形取最小值
"""


# Solution 1: Greedy
# Time: O(NlogN) | Space: O(1)
class Solution:
    def minDifference(self, A):
        A.sort()
        return min(b - a for a, b in zip(A[:4], A[-4:]))
