"""
1041. Robot Bounded in Circle
- Medium
- Math, String, Simulation
- Link: https://leetcode.com/problems/robot-bounded-in-circle/
"""


# Solution 1: Math
# Time: O(N) | Space: O(1)
# 要回到原點，勢必要經過四個轉向 (連續的順時鐘或是逆時鐘)，所以可以檢查四個 cycle 之後，是否在原點
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        degree = 0
        cur = [0, 0]
        numOfCycle = 4
        count = 0

        while count < numOfCycle:
            for ins in instructions:
                if ins == 'L':
                    degree -= 90
                elif ins == 'R':
                    degree += 90
                else:
                    if degree % 360 == 0:
                        cur[1] += 1
                    elif degree % 360 == 90:
                        cur[0] += 1
                    elif degree % 360 == 180:
                        cur[1] -= 1
                    else:
                        cur[0] -= 1
            count += 1
        return cur == [0, 0]


# Solution 2: Math
# Time: O(N) | Space: O(1)
# 觀察後發現，單個 cycle 結束後除非仍面向北且有移動，不然一定會回到原點
# 畫圖 deltaX and deltaY 可以檢查
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        x = y = 0
        # north: 0, east: 1, south: 2, west: 3
        idx = 0

        for ins in instructions:
            if ins == 'L':
                idx = (idx + 3) % 4
            elif ins == 'R':
                idx = (idx + 1) % 4
            else:
                x += directions[idx][0]
                y += directions[idx][1]

        return (x == 0 and y == 0) or (idx != 0)
