"""
1249. Minimum Remove to Make Valid Parentheses
- Medium
- String, Stack
- Link: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
"""


# Solution 1: Stack
# Time: O(N) | Space: O(N)
# 利用 Stack 的性質，來將不合理的 () 去除，同時用到 union set 的概念
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        index_to_remove = set()
        stack = []
        for idx, char in enumerate(s):
            if char not in '()':
                continue
            if char == '(':
                stack.append(idx)
            elif not stack:
                index_to_remove.add(idx)
            else:
                stack.pop()

        index_to_remove = index_to_remove.union(set(stack))
        ans = []
        for i in range(len(s)):
            if i not in index_to_remove:
                ans.append(s[i])

        return "".join(ans)
