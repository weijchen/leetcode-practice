"""
71. Simplify Path
- Medium
- String, Stack
- Link: https://leetcode.com/problems/simplify-path/
"""


# Solution 1: Stack + String
# Time: O(N) | Space: O(N)
class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = [p for p in path.split('/') if p is not '']

        st = []

        for p in path_list:
            if p == '..':
                if len(st) != 0:
                    st.pop()
            elif p == '.':
                continue
            else:
                st.append(p)

        canPath = ""
        for e in st:
            toAdd = "/" + e
            canPath += toAdd

        return "/" if len(canPath) == 0 else canPath
