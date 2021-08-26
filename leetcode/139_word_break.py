"""
139. Word Break
- Medium
- Hash Table, String, DP, Trie, Memoization
- Link: https://leetcode.com/problems/word-break/
"""


# Solution 1: Brute Force
# Time: O(2^N) | Space: O(N)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def recursion(s, word_dict, start):
            if start == len(s):
                return True

            for end in range(start+1, len(s) + 1):
                if s[start:end] in word_dict and recursion(s, word_dict, end):
                    return True
            return False

        return recursion(s, set(wordDict), 0)


# Solution 2: Memoization
# Time: O(N^2) | Space: O(N)
# T(n) = T(n-1) + n. n is for the O(1) memo accesses for n scaled end ptrs in the for loop.
# Similarly, T(n-1) = T(n-2) + (n-1).
# Hence, after substituting T(n-1) with T(n-2) + (n-1), T(n) = T(n-2) + (n-1) + n. Keep substituting.
# T(1) = 1.
# Hence, T(n) = 1 + 2 + ... (n-1) + n = n(n+1)/2. Thus, O(n^2).
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        memo = {}

        def recursion(s, wordSet, memo):
            # 1. base cases
            if not s:
                return True
            elif s in memo:
                return memo[s]

            # 2. body
            for word in wordSet:
                prefix = s[:len(word)]

                if prefix == word and recursion(s[len(word):], wordSet, memo):
                    memo[prefix] = True
                    return True

            # we can not find any matches inside our wordSet
            memo[s] = False
            return False

        return recursion(s, wordSet, memo)


# Solution 3: DP
# Time: O(N^2) | Space: O(N)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break
        return dp[len(s)]
