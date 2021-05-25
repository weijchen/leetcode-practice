"""
3. Longest Substring Without Repeating Characters
- Medium
- Hash Table, Two Pointers, String, Sliding Window
- Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""


# Approach 1: Hash Table + Two Pointers
# Time: O(2n) = O(n) | Space: O(m)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        if len(s) == 0:
            return ans
        s_length = len(s)
        p1 = p2 = 0

        while p2 <= s_length:
            toCheck = s[p1: p2]
            if self.checkRepeat(toCheck):
                toCheck_length = len(toCheck)
                ans = max(ans, toCheck_length)
                p2 += 1
            else:
                p1 += 1
        return ans

    def checkRepeat(self, string) -> bool:
        dic = dict()
        for c in string:
            if c in dic.keys():
                return False
            else:
                dic[c] = True
        return True
