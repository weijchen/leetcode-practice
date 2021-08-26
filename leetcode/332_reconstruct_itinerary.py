"""
332. Reconstruct Itinerary
- Medium
- DFS, Graph, Eulerian Circuit
- Link: https://leetcode.com/problems/reconstruct-itinerary/
"""


# Solution 1: Backtracking + Greedy
# Time: O(E^d), where E is the number of total flights and d is the maximum number of flights from an airport | Space: O(V + E)
# 每一種可行的 path 都試過
class Solution:
    def __init__(self):
        self.ans = []
        self.visitBitmap = {}

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        g = collections.defaultdict(list)
        ans_length = len(tickets) + 1

        for (_from, _to) in tickets:
            g[_from].append(_to)

        for origin, itinerary in g.items():
            itinerary.sort()
            self.visitBitmap[origin] = [False] * len(itinerary)

        def backtrack(start, path):
            if len(path) == ans_length:
                self.ans = path
                return True

            for idx, nei in enumerate(g[start]):
                if not self.visitBitmap[start][idx]:
                    self.visitBitmap[start][idx] = True
                    ret = backtrack(nei, path + [nei])
                    self.visitBitmap[start][idx] = False
                    if ret:
                        return True
            return False

        backtrack("JFK", ["JFK"])
        return self.ans


# Solution 2: Eulerian Cycle
# Time: O(E*logE) | Space: O(V + E)
# 每次只試排序最小的邊
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        from collections import defaultdict
        self.flightMap = defaultdict(list)

        for ticket in tickets:
            origin, dest = ticket[0], ticket[1]
            self.flightMap[origin].append(dest)

        # sort the itinerary based on the lexical order
        for origin, itinerary in self.flightMap.items():
        # Note that we could have multiple identical flights, i.e. same origin and destination.
            itinerary.sort(reverse=True)

        self.result = []
        self.DFS('JFK')

        # reconstruct the route backwards
        return self.result[::-1]

    def DFS(self, origin):
        destList = self.flightMap[origin]
        while destList:
            #while we visit the edge, we trim it off from graph.
            nextDest = destList.pop()
            self.DFS(nextDest)
        self.result.append(origin)
