#
# @lc app=leetcode id=187 lang=python3
#
# [187] Repeated DNA Sequences
#

# @lc code=start
# Solution 1: Linear-time Slice using substring + hashset
# Time: O((N-L)L) | Space: O((N-L)L)
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10: return None
        seqDict = dict()
        ans = set()

        for i in range(len(s)-9):
            curSeq = s[i: i+10]
            if curSeq in seqDict.keys():
                ans.add(curSeq)
            seqDict[curSeq] = True
        return ans
        

# @lc code=end

