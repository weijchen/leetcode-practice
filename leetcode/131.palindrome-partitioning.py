#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans_list = []
        ans = []
        self.findPartition(s, [], ans)
        # self.checkPalindrome(ans_list)
        return ans_list
    
    def findPartition(self, remain, comb, ans, curPath=""):
        if len(remain) > 0:
            addChar = remain[0]
            remain = s[1:]
            self.findPartition(remain, comb, ans, curPath + "{}".format(addChar))
            self.findPartition(remain, comb, ans, curPath)
        else:
            ans.append(comb)





    def checkPalindrome(self, s_list: List[str]) -> bool:
        for s in s_list:
            if s != reversed(s):
                return False
        return True
        
# @lc code=end

