#!/usr/bin/env python3

# Day 18: Course Schedule II
#
# There are a total of n courses you have to take, labeled from 0 to n-1.
# Some courses may have prerequisites, for example to take course 0 you have to
# first take course 1, which is expressed as a pair: [0,1]
# Given the total number of courses and a list of prerequisite pairs, return
# the ordering of courses you should take to finish all courses.
# There may be multiple correct orders, you just need to return one of them. If
# it is impossible to finish all courses, return an empty array.

import collections

class Solution:
    def findOrder(self, numCourses: int, prerequisites: [[int]]) -> [int]:
        # Minimal case
        if numCourses == 0:
            return []

        # Build a dependency graph
        graph = collections.defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)

        # Check for cycles
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

        for node in range(numCourses):
            if inCycle(graph, visited, node):
                return []

        # Get a topological sort of what is guaranteed to be a DAG
        def topologicalSort(graph, visited, stack, node):
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    topologicalSort(graph, visited, stack, neighbor)
            stack.append(node)

        visited = [False for _ in range(numCourses)]
        stack = []
        for node in range(numCourses):
            if not visited[node]:
                topologicalSort(graph, visited, stack, node)
        return stack

# Tests
assert Solution().findOrder(2, [[1,0]]) == [0,1]
assert Solution().findOrder(2, [[0,1]]) == [1,0]
assert Solution().findOrder(2, [[0,1], [1,0]]) == []
assert Solution().findOrder(4, [[1,0],[2,0],[3,1],[3,2]]) in [[0,1,2,3], [0,2,1,3]]
