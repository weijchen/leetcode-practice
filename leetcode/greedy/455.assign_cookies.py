"""
455. Assign Cookies
- Easy
- Greedy
- Link: https://leetcode.com/problems/assign-cookies/
"""


# Solution 1: Two Pointers
# Time: O(NlogN) | Space: O(1)
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        ans = 0
        if len(s) == 0:
            return ans

        child, cookie = 0, 0

        while child < len(g) and cookie < len(s):
            if g[child] > s[cookie]:
                cookie += 1
            else:
                child += 1
                cookie += 1
        return child
