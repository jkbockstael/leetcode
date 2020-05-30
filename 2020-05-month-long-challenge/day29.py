#!/usr/bin/env python3

# Day 29: Course Schedule
#
# There are a total of numCourses courses you have to take, labeled from 0 to
# numCourses-1.
# Some courses may have prerequisites, for example to take course 0 you have to
# first take course 1, which is expressed as a pair: [0,1]
# Given the total number of courses and a list of prerequisite pairs, is it
# possible for you to finish all courses?
#
# Constraints:
# - The input prerequisites is a graph represented by a list of edges, not
#   adjacency matrices.
# - You may assume that there are no duplicate edges in the input
#   prerequisites.
# - 1 <= numCourses <= 10^5

class Solution:
    def canFinish(self, numCourses: int, prerequisites: [[int]]) -> bool:
        # Minimal case
        if numCourses == 0 or len(prerequisites) == 0:
            return True
        # Build a dependency graph
        graph = {}
        for a, b in prerequisites:
            if a not in graph:
                graph[a] = []
            graph[a].append(b)
        # Cycle check function
        visited = {}
        def inCycle(graph, visited, node):
            if node not in graph:
                return False
            if node in visited:
                return visited[node]
            visited[node] = True
            for neighbor in graph[node]:
                if inCycle(graph, visited, neighbor):
                    return True
            visited[node] = False
            return False
        # Check for cycles
        for node in range(0, numCourses):
            if inCycle(graph, visited, node):
                return False
        return True

# Tests
assert Solution().canFinish(2, [[1,0]]) == True
assert Solution().canFinish(2, [[1,0],[0,1]]) == False
assert Solution().canFinish(3, [[1,0], [2,1]]) == True
