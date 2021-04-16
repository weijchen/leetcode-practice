"""
49. Group Anagrams
- Medium
- Hash Table, String
- Link: https://leetcode.com/problems/group-anagrams/
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ht = {}
        for word in strs:
            k = ''.join(sorted(word))
            if k not in ht.keys():
                ht[k] = [word]
            else:
                ht[k].append(word)

        ret = []
        for k in ht.keys():
            ret.append(ht[k])
        return ret
