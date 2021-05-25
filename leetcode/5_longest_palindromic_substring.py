"""
5. Longest Palindromic Substring
- Medium
- String, Dynamic Programming
- Link: https://leetcode.com/problems/longest-palindromic-substring/
"""


# Solution 1: Expand Around Center
# Time: O(N^2) | Space: O(1)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            curStr = self.helper(s, i, i)
            ans = ans if len(ans) > len(curStr) else curStr

            curStr = self.helper(s, i, i+1)
            ans = ans if len(ans) > len(curStr) else curStr

        return ans

    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]


class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)
        # Form a bottom-up dp 2d array
        # dp[i][j] will be 'true' if the string from index i to j is a palindrome. 
        dp = [[False] * n  for _ in range(n)]
        
        ans = ''
        # every string with one character is a palindrome
        for i in range(n):
            dp[i][i] = True
            ans = s[i]
            
        maxLen = 1
        for start in range(n-1, -1, -1):
            for end in range(start+1, n):             
				# palindrome condition
                if s[start] == s[end]:
                    # if it's a two char. string or if the remaining string is a palindrome too
                    if end - start == 1 or dp[start+1][end-1]:
                        dp[start][end] = True
                        if maxLen < end - start + 1:
                            maxLen = end - start + 1
                            ans = s[start: end+ 1]
        
        return ans
