"""
17. Letter Combinations of a Phone Number
- Medium
- String, Backtracking, Depth-first Search, Recursion
- Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""


"""
Solution 1: BFS
Time: O(3^N * 4^M) -> where N is the number of digits in the input that maps to 3 letters, and M is the number of digits in the input that maps to 4 letters
Space: O(3^N * 4^M)
"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitMap = {'2': ['a', 'b', 'c'],
                    '3': ['d', 'e', 'f'],
                    '4': ['g', 'h', 'i'],
                    '5': ['j', 'k', 'l'],
                    '6': ['m', 'n', 'o'],
                    '7': ['p', 'q', 'r', 's'],
                    '8': ['t', 'u', 'v'],
                    '9': ['w', 'x', 'y', 'z']}

        avaiCharList = []
        for d in digits:
            avaiCharList.append(digitMap[d])

        if len(avaiCharList) == 0:
            return []

        curNode = avaiCharList.pop(0)
        curLevel = [char for char in curNode]
        tmpCurLevel = []

        while avaiCharList:
            nextLevel = avaiCharList.pop(0)
            for avai in curLevel:
                for e in nextLevel:
                    tmpCurLevel.append("{}{}".format(avai, e))
            curLevel, tmpCurLevel = tmpCurLevel, []

        return curLevel


"""
Solution 2: DFS / backtracking
Time: O(3^N * 4^M) -> where N is the number of digits in the input that maps to 3 letters, and M is the number of digits in the input that maps to 4 letters
Space: O(3^N * 4^M)
"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitMap = {'2': ['a', 'b', 'c'],
                    '3': ['d', 'e', 'f'],
                    '4': ['g', 'h', 'i'],
                    '5': ['j', 'k', 'l'],
                    '6': ['m', 'n', 'o'],
                    '7': ['p', 'q', 'r', 's'],
                    '8': ['t', 'u', 'v'],
                    '9': ['w', 'x', 'y', 'z']}

        def backtracking(combination, digits):
            if len(digits) == 0:
                ret.append(combination)
            else:
                curChar = digitMap[digits[0]]
                for char in curChar:
                    backtracking(combination + char, digits[1:])

        ret = []
        if digits:
            backtracking("", digits)

        return ret
