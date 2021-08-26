"""
987. Time Based Key-Value Store
- Medium
- Hash Table, Binary Search
- Link: https://leetcode.com/problems/time-based-key-value-store/
"""


# Solution 1: Hash Table + Binary Search
# Time: O(logN) | Space: O(N)
class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key, value, timestamp):
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        keyMap = self.map[key]
        l, r = 0, len(keyMap) - 1
        found = -1
        while l <= r:
            mid = (l - r) // 2 + r
            ts, val = keyMap[mid]
            if ts == timestamp:
                return val
            elif ts > timestamp:
                r = mid - 1
            else:
                found = mid
                l = mid + 1

        if found == -1:
            return ""
        else:
            return keyMap[found][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
