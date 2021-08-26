"""
277. Find the Celebrity
- Medium
- Two Pointers, Greedy, Graph, Interactive
- Link: https://leetcode.com/problems/find-the-celebrity/
"""


# Solution 1: Brute Force
# Time: O(N^2) | Space: O(1)
class Solution:
    def findCelebrity(self, n: int) -> int:
        self.n = n
        for i in range(n):
            if self.is_celebrity(i):
                return i
        return -1

    def is_celebrity(self, i):
        for j in range(self.n):
            if i == j:
                continue  # Don't ask if they know themselves.
            if knows(i, j) or not knows(j, i):
                return False
        return True
