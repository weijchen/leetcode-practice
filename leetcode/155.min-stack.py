#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
# Solution 1: tuple for storing information
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.st = []

    def push(self, val: int) -> None:
        if len(self.st) == 0:
            self.st.append((val, val))
        else:
            current_min = self.st[-1][1]
            self.st.append((val, min(current_min, val)))

    def pop(self) -> None:
        self.st.pop(-1)

    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        return self.st[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end
