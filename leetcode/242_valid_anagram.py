"""
242. Valid Anagram
- Easy
- Hash Table
- Link: https://leetcode.com/problems/valid-anagram/
"""


# Solution 1: Hash Table
# Time: O(n) | Space: O(1) -> the table's size stays constant no matter how large n is (hash table keys can be max 26 for 26 lowercase characters)
# 因為字母數量固定為 26，所以 space complexity stays constant
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = collections.Counter(s)
        t_count = collections.Counter(t)

        if len(s_count.keys()) != len(t_count.keys()):
            return False

        return s_count == t_count
