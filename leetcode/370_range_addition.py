"""
370. Range Addition
- Medium
- Array, Prefix Sum
- Link: https://leetcode.com/problems/range-addition/
"""


# Solution 1: Rolling Sum
# Time: O(N) | Space: O(N)
# 當 start:end 要增加某數值 N === start 存 +N, end 存 -N
# 再來做 rolling sum
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        ans = [0] * length

        for start, end, add in updates:
            ans[start] += add
            if end + 1 < length:
                ans[end+1] -= add

        _sum = 0

        for idx, num in enumerate(ans):
            _sum += num
            ans[idx] = _sum

        return ans
