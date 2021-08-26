"""
207. Course Schedule
- Medium
- DFS, BFS, Graph, Topological Sort
- Link: https://leetcode.com/problems/course-schedule/
"""


# Solution 1: Topological Sort
# Time: O(E + V), where V is the number of vertex and E is the number of edge | Space: O(E + V)
class GNode(object):
    def __init__(self):
        self.inDegrees = 0
        self.outNodes = []


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict, deque

        graph = defaultdict(GNode)

        # 建立 graph，計算 number of dependency
        totalDeps = 0
        for relation in prerequisites:
            nextCourse, prevCourse = relation[0], relation[1]
            graph[prevCourse].outNodes.append(nextCourse)
            graph[nextCourse].inDegrees += 1
            totalDeps += 1  # total dependencies

        # 紀錄起始節點 (不存在 indegrees 的 node)
        nodepCourses = deque()
        for idx, node in graph.items():
            if node.inDegrees == 0:
                nodepCourses.append(idx)

        # 從起始節點開始，針對其 outNodes 開始消除 edge/dependency
        removedEdges = 0
        while nodepCourses:
            course = nodepCourses.pop()

            for nextCourse in graph[course].outNodes:
                graph[nextCourse].inDegrees -= 1
                removedEdges += 1

                # 當 inDegrees 不等於 0 時，代表該處有迴圈的可能
                if graph[nextCourse].inDegrees == 0:
                    nodepCourses.append(nextCourse)

        # 當消除的 edge 等同於一開始計算的 dependency 數量，代表該圖不存在 cycle
        if removedEdges == totalDeps:
            return True
        else:
            return False
