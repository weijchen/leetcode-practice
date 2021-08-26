"""
38. Count and Say
- Medium
- String
- Link: https://leetcode.com/problems/count-and-say/
"""


# Solution 1: String
# Time: O(NM), where M is the max length of string | Space: O(NM)
class Solution:
    def countAndSay(self, n: int) -> str:
        d = {1: "1"}
        
        if n == 1:
            return d[n]
        
        for i in range(2, n+1):
            count = 1
            cur_num = ""
            cur_saying = ""
            
            mapNum = d[i-1]
            l = len(mapNum)
            
            for j in range(l):
                if j == 0 or mapNum[j] != mapNum[j-1]:
                    if j != 0:
                        cur_saying += str(count)
                        cur_saying += str(cur_num)
                    cur_num = mapNum[j]
                    count = 1
                    
                else:
                    count += 1
            cur_saying += str(count)
            cur_saying += str(cur_num)
            
            d[i] = cur_saying
                
        return d[n]
                    
            