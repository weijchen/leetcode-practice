"""
621. Task Scheduler
- Medium
- Array, Two Pointers, Binary Search, Sorting, Heap (Priority Queue)
- Link: https://leetcode.com/problems/find-k-closest-elements/
"""

# Solution 1: Math
# Time: O(N), where N is the number of tasks to execute | Space: O(1)
# ABX   ABX   ABX   A
#  (n+1) * (max_f-1) + p (最多次數的 task 有幾個，最後會排在一起) -> 有殘留空位 (X) 的情況
#  len(tasks) -> 沒有殘留空位的情況
#  兩者取最大值
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequency = [0] * 26
        for task in tasks:
            frequency[ord(task) - ord('A')] += 1

        frequency.sort()

        max_f = frequency[-1]
        n_max = frequency.count(max_f)

        return max((n+1)*(max_f-1) + n_max, len(tasks))


# Solution 2: Priority Queue (max-heap)
# Time: O(NlogM), where N is the number of tasks, and M is the number of unique tasks | Space: O(N)
from heapq import *
class Solution(object):
    def leastInterval(self, tasks, n):
        counter = collections.Counter(tasks)
        heap = [(-v, k) for k, v in counter.items()]
        heapify(heap)
        time = 0
        while heap:
            i = 0
            temp = []
            while i <= n:
                if heap:
                    v, k = heappop(heap)
                    if -v > 1:
                        temp.append((v+1, k))
                time += 1
                # 若 heap, temp 皆以用完，會強制完結此輪 (發生在最後一組 task 的時候)
                if not heap and not temp:
                    break
                i += 1
            for l in temp:
                heappush(heap, l)

        return time
