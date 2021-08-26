"""
134. Gas Station
- Medium
- Array, Greedy
- Link: https://leetcode.com/problems/gas-station/
"""


# Solution 1: Brute Force
# Time: O(N^2) | Space: O(N)
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        chg = [g - c for g, c in zip(gas, cost)]
        ret = -1

        for idx in range(len(gas)):
            remain = 0
            for inc in range(len(gas)):
                remain += chg[(idx + inc) % len(chg)]
                if remain < 0:
                    break

            if remain < 0:
                continue

            ret = idx
            if ret != -1:
                break

        return ret


# Solution 1: One-pass Greedy
# Time: O(N) | Space: O(1)
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start_point = 0
        total_tank = 0
        curr_tank = 0
        for idx in range(len(gas)):
            total_tank += (gas[idx] - cost[idx])
            curr_tank += (gas[idx] - cost[idx])
            if curr_tank < 0:
                start_point = idx+1
                curr_tank = 0

        return start_point if total_tank >= 0 else -1
