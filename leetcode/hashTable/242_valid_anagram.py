"""
242. Valid Anagram
- Easy
- Hash Table
- Link: https://leetcode.com/problems/valid-anagram/
"""


# Solution 1: Hash Table
# Time: O(n) | Space: O(1) -> the table's size stays constant no matter how large n is (hash table keys can be max 26 for 26 lowercase characters)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = Counter(s)
        d2 = Counter(t)

        if len(d1.keys()) != len(d2.keys()):
            return False

        for k, v in d2.items():
            if k not in d1.keys():
                return False
            else:
                if v != d1[k]:
                    return False
        return True
