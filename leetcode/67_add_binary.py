"""
67. Add Binary
- Easy
- Math, String
- Link: https://leetcode.com/problems/add-binary/
"""


# Time: O(max(N, M)) | Space: O(1) - in-place replacement
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = a[::-1], b[::-1]
        if len(a) >= len(b):
            l, s = a, b
        else:
            l, s = b, a

        carry = 0
        maxL = max(len(l), len(s))
        for i in range(maxL):
            l_int = int(l[i]) if i < len(l) else 0
            s_int = int(s[i]) if i < len(s) else 0
            _sum, carry = (l_int + s_int +
                           carry) % 2, (l_int + s_int + carry) // 2
            l = "".join((l[:i], str(_sum), l[i+1:]))

        if carry:
            l = l + "1"

        return l[::-1]
