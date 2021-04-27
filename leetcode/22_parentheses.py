"""
22. Generate Parentheses
- Medium
- String, Backtracking
- Link: https://leetcode.com/problems/generate-parentheses/
"""


# Approach 1: Backtracking
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        merged = ""
        self.helper(n, n, ans, merged)
        return ans

    def helper(self, lN, rN, ans, merged, comb=""):
        if lN == 0 and rN == 0:
            if len(merged) == 0:
                ans.append(comb)
        else:
            if lN > 0:
                newMerged = merged + "("
                newComb = comb + "("
                self.helper(lN-1, rN, ans, newMerged, newComb)

            if rN > 0 and lN < rN:
                if len(merged) != 0 and merged[-1] == "(":
                    newComb = comb + ")"
                    newMerged = merged[:-1]
                    self.helper(lN, rN-1, ans, newMerged, newComb)
