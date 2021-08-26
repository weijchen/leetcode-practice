"""
791. Custom Sort String
- Medium
- Hash Table, String, Sorting
- Link: https://leetcode.com/problems/custom-sort-string/
"""


# Solution 1: Hash Table
# Time: O(M + N) where M is the length of order and N is the length of str
# Space: O(M)
class Solution:
    def customSortString(self, order: str, str: str) -> str:

        ordDict = {order[i]: [i, 0] for i in range(len(order))}
        ans = ""
        for char in str:
            if char not in ordDict:
                ans += char
            else:
                ordDict[char][1] += 1

        prev = ""
        for k, v in ordDict.items():
            for _ in range(v[1]):
                prev += k

        return prev + ans
