"""
3. Longest Substring Without Repeating Characters
- Medium
- Hash Table, Two Pointers, String, Sliding Window
- Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""


# Approach 1: Hash Table + Two Pointers
# Time: O(2n) = O(n)
# Space: O(m)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        ret = 0
        l = len(s)
        p1 = p2 = 0
        
        while p2 <= l - 1:
            p2 += 1
            curSubString = s[p1: p2]
            
            if self.checkDuplicate(curSubString):
                p1 += 1
                ret = max(len(curSubString) - 1, ret)
            else:
                ret = max(len(curSubString), ret)
                
        return ret
            
    def checkDuplicate(self, s: str) -> bool:
        ret = {}
        for _ in s:
            if _ in ret.keys():
                return True
            else:
                ret[_] = True
        return False
