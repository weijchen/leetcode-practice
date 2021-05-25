#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.ageList = []   # heap
        self.data = {}
        self.lruKey = None

    def get(self, key: int) -> int:
        if key not in self.data.keys():
            return -1
        return self.data[key]

    def put(self, key: int, value: int) -> None:
        numOfData = len(self.data.keys())
        print(numOfData)
        print(key)
        if numOfData >= self.size:
            keyToRemove = self.ageList.pop(-1)
            del self.data[keyToRemove]
            self.data[key] = value
            self.ageList.append(key)
        else:
            self.data[key] = value
            self.ageList.append(key)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

