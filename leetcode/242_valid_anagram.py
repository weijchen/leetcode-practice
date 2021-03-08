"""
242. Valid Anagram
- Easy
- Hash Table, Sort
- Link: https://leetcode.com/problems/valid-anagram/
"""


# Time: O(n)
# Space: O(1) -> the table's size stays constant no matter how large n is (hash table keys can be max 26 for 26 lowercase characters)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ht = {}

        for char in s:
            if char in ht.keys():
                ht[char] += 1
            else:
                ht[char] = 1

        for char in t:
            if char not in ht.keys():
                return False
            else:
                ht[char] -= 1

        for k in ht.keys():
            if ht[k] != 0:
                return False

        return True
