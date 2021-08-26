"""
146. LRU Cache
- Medium
- Design
- Link: https://leetcode.com/problems/lru-cache/
"""


# Solution 1: Hash Table (Ordered Dict in python built-in library)
# Time: O(1) | Space: O(capacity)
# Key methods to remember for OrderedDict
# - .move_to_end()
# - .popitem(last)
class LRUCache:

    def __init__(self, capacity: int):
        self.d = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        self.d.move_to_end(key)
        return self.d[key]

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d.move_to_end(key)
        self.d[key] = value

        if len(self.d) > self.capacity:
            self.d.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


class DLinkedNode():
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None



# Solution 2: Hashmap + DLinkedList
# Time; O(1) | Space: O(capacity)
# DLinkedList 用來操作 1) 刪除尾node, 2) 增加node至head後方
# KeyMap 用來記錄使用過的 Node (key-value) -> node 可送入 DLinkedList 來執行相關操作 / 可檢查不存在的 Node 來做增加
class LRUCache:
    def _add_node(self, node):
        # always add the new node right after head
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev

    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        res = self.tail.prev
        self._remove_node(res)
        return res

    def __init__(self, capacity: int):
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = DLinkedNode(), DLinkedNode()

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if not node:
            return -1

        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)

        if not node:
            newNode = DLinkedNode()
            newNode.key = key
            newNode.value = value

            self.cache[key] = newNode
            self._add_node(newNode)

            self.size += 1

            if self.size > self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            node.value = value
            self._move_to_head(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
