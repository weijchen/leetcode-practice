"""
210. Course Schedule II
- Medium
- DFS, BFS, Graph, Topological Sort
- Link: https://leetcode.com/problems/course-schedule-ii/
"""


# Solution 1: Topological Sort
# Time: O(E + V), where V is the number of vertex and E is the number of edge | Space: O(E + V)
class GNode:
    def __init__(self):
        self.inDegrees = 0
        self.outNodes = []


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans = []

        from collections import defaultdict, deque

        nodeDependency = 0  # for checking no edge-dependncy was left
        graph = defaultdict(GNode)
        for nextCourse, prevCourse in prerequisites:
            graph[prevCourse].outNodes.append(nextCourse)
            graph[nextCourse].inDegrees += 1
            nodeDependency += 1

        nodeTraveled = deque()
        for course in range(numCourses):
            if graph[course].inDegrees == 0:
                nodeTraveled.append(course)

        deleteDependency = 0
        while nodeTraveled:
            course = nodeTraveled.pop()
            ans.append(course)
            for nei in graph[course].outNodes:
                graph[nei].inDegrees -= 1
                deleteDependency += 1

                if graph[nei].inDegrees == 0:
                    nodeTraveled.append(nei)

        return ans if deleteDependency == nodeDependency else []
