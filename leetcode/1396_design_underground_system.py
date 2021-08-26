"""
1396. Design Underground System
- Medium
- Hash Table, String, Design
- Link: https://leetcode.com/problems/design-underground-system/
"""


# Solution 1: Hash Table
# Time: O(1) | Space: O(N^2)
class UndergroundSystem:
    def __init__(self):
        self.timeTable = collections.defaultdict(dict)
        self.avgTime = collections.defaultdict(dict)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.timeTable[id] = (t, stationName)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        inTime, fromName = self.timeTable[id]
        duration = t - inTime
        key = "{}-{}".format(fromName, stationName)
        if key in self.avgTime:
            self.avgTime[key].append(duration)
        else:
            self.avgTime[key] = [duration]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = "{}-{}".format(startStation, endStation)
        return sum(self.avgTime[key]) / len(self.avgTime[key])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
