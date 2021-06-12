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

        nodeDep = 0
        graph = defaultdict(GNode)
        for relation in prerequisites:
            nextCourse, prevCourse = relation[0], relation[1]
            graph[prevCourse].outNodes.append(nextCourse)
            graph[nextCourse].inDegrees += 1
            nodeDep += 1

        # start point
        nodepCourse = deque()
        for course in range(numCourses):
            if graph[course].inDegrees == 0:
                nodepCourse.append(course)

        delDeps = 0
        while nodepCourse:
            course = nodepCourse.pop()
            ans.append(course)

            for nei in graph[course].outNodes:
                graph[nei].inDegrees -= 1
                delDeps += 1

                # find next start point, also check the occurrence of cycle
                if graph[nei].inDegrees == 0:
                    nodepCourse.append(nei)

        if nodeDep == delDeps:
            return ans
        else:
            return []
