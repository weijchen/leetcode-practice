"""
22. Generate Parentheses
- Medium
- String, Backtracking
- Link: https://leetcode.com/problems/generate-parentheses/
"""


# Solution 1: Backtracking (Iterative)
# Time: O(4^N / N * N^1/2) | Space: O(4^N / N * N^1/2) -> 可以想成是要產生兩顆樹 (是否有 '(' 和是否有 ')') = 2^(2*N)
# Generate all sequences
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        st = [("(", "(")]

        while st:
            origin, merge = st.pop()
            if len(origin) == 2 * n:
                if len(merge) == 0:
                    ans.append(origin)
            else:
                if len(merge) == 0:
                    newOrigin, newMerge = origin + "(", merge + "("
                    st.append((newOrigin, newMerge))
                else:
                    newOrigin, newMerge = origin + "(", merge + "("
                    st.append((newOrigin, newMerge))
                    newOrigin, newMerge = origin + ")", merge[:-1]
                    st.append((newOrigin, newMerge))

        return ans


# Solution 2: Backtracking (Recursive)
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
