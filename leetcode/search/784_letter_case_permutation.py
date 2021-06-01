"""
784. Letter Case Permutation
- Medium
- Backtracking, Bit Manipulation
- Link: https://leetcode.com/problems/letter-case-permutation/
- The key to this problem is how to detect alpha and to change letter case
"""


# Solution 1: Backtracking
# Time: O(2^L), where L is the length of letters in s | Space: O(2^L) + O(N) (sols + stack)
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []

        def backtracking(sList, idx, n):
            if idx == n:
                ans.append(''.join(sList[:]))
                return

            charOrd = ord(sList[idx])
            backtracking(sList, idx+1, n)
            if (charOrd >= ord('a') and charOrd <= ord('z')):
                sList[idx] = sList[idx].upper()
                backtracking(sList, idx+1, n)
                sList[idx] = sList[idx].lower()
            if (charOrd >= ord('A') and charOrd <= ord('Z')):
                sList[idx] = sList[idx].lower()
                backtracking(sList, idx+1, n)
                sList[idx] = sList[idx].upper()

        # 使用列表結構，來協助 String 類型的大小寫轉換
        sList = [_ for _ in s]
        backtracking(sList, 0, len(s))
        return ans


# Solution 2: Backtracking with bit operator
# Time: O(2^L), where L is the length of letters in s | Space: O(2^L) + O(N) (sols + stack)
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []

        def backtracking(sList, idx, n):
            if idx == n:
                ans.append(''.join(sList[:]))
                return

            charOrd = ord(sList[idx])
            backtracking(sList, idx+1, n)
            if sList[idx].isalpha():
                # 針對第五個 bit (32) 做 toggle
                sList[idx] = chr(ord(sList[idx]) ^ (1 << 5))
                backtracking(sList, idx+1, n)
                sList[idx] = chr(ord(sList[idx]) ^ (1 << 5))

        sList = [_ for _ in s]
        backtracking(sList, 0, len(s))
        return ans
