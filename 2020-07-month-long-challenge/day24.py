#!/usr/bin/env python3

# Day 24: All Paths From Source to Target
#
# Given a directed, acyclic graph of N nodes.  Find all possible paths from
# node 0 to node N-1, and return them in any order.
# The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.
# graph[i] is a list of all nodes j for which the edge (i, j) exists.
#
# Note:
# - The number of nodes in the graph will be in the range [2, 15].
# - You can print different paths in any order, but you should keep the order
#   of nodes inside one path.

class Solution:
    def allPathsSourceTarget(self, graph: [[int]]) -> [[int]]:
        paths = []
        def findAllPaths(source, target, visited, path):
            visited[source] = True
            path.append(source)
            if source == target:
                paths.append(path[::])
            else:
                for neighbor in graph[source]:
                    if not visited[neighbor]:
                        findAllPaths(neighbor, target, visited, path)
            path.pop()
            visited[source] = False
        visited = [False for _ in graph]
        findAllPaths(0, len(graph) - 1, visited, [])
        return paths

# Test
assert Solution().allPathsSourceTarget([[1,2], [3], [3], []]) in [[[0,1,3],[0,2,3]], [[0,2,3],[0,1,3]]]
