#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
# Solution 1: Reverse all, then reverse each word
# Time: O(N) | Space: O(N)
class Solution:
    def reverseWords(self, s: str) -> str:
        s = self.trim(s)
        s_rev = s[::-1] + " "
        p1 = p2 = 0

        while p2 < len(s_rev):
            if s_rev[p2] == ' ':
                s_rev = self.reverse(p1, p2, s_rev)
                p1 = p2+1
            p2 += 1
        return s_rev[1:]

    def reverse(self, l: int, r: int, s: str) -> str:
        s_list = [_ for _ in s]
        while l < r:
            s_list[l], s_list[r] = s_list[r], s_list[l]
            l += 1
            r -= 1
        return "".join(s_list)

    def trim(self, s: str) -> str:
        l, r = 0, len(s) - 1
        while s[l] == " ":
            l += 1
        while s[r] == " ":
            r -= 1
        output = []
        while l <= r:
            if s[l] != ' ':
                output.append(s[l])
            elif output[-1] != ' ':
                output.append(s[l])
            l += 1
        return "".join(output)
# @lc code=end
