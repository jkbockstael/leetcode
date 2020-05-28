#!/usr/bin/env python3

# Day 27: Possible Bipartition
#
# Given a set of N people (numbered 1, 2, ..., N), we would like to split
# everyone into two groups of any size.
# Each person may dislike some other people, and they should not go into the
# same group. 
# Formally, if dislikes[i] = [a, b], it means it is not allowed to put the
# people numbered a and b into the same group.
# Return true if and only if it is possible to split everyone into two groups
# in this way.
#
# Notes:
# - 1 <= N <= 2000
# - 0 <= dislikes.length <= 10000
# - 1 <= dislikes[i][j] <= N
# - dislikes[i][0] < dislikes[i][1]
# - There does not exist i != j for which dislikes[i] == dislikes[j].

class Solution:
    def possibleBipartition(self, N: int, dislikes: [[int]]) -> bool:
        # Parse the input as an undirected graph
        dislike_graph = {}
        for a, b in dislikes:
            if a not in dislike_graph:
                dislike_graph[a] = []
            if b not in dislike_graph:
                dislike_graph[b] = []
            dislike_graph[a].append(b)
            dislike_graph[b].append(a)

        # Recursive assignment into groups:
        # Assign a person to a group, then assign all their dislikes to the
        # other group. If at some point we encounter a person that's already in
        # a group and we should assign them to the other, this means the graph
        # isn't bipartite.
        groups = {}
        def traverse(node, group):
            if node in groups:
                return groups[node] == group
            groups[node] = group
            group = 0 if group == 1 else 1
            neighbors = dislike_graph[node] if node in dislike_graph else []
            return all(traverse(neighbor, group) for neighbor in neighbors)

        # This must hold true for everybody
        return all(traverse(node, 0) for node in range(1, N + 1) \
            if node not in groups)

# Tests
assert Solution().possibleBipartition(4, [[1,2],[1,3],[2,4]]) == True
assert Solution().possibleBipartition(3, [[1,2],[1,3],[2,3]]) == False
assert Solution().possibleBipartition(5, [[1,2],[2,3],[3,4],[4,5],[1,5]]) == False
assert Solution().possibleBipartition(4, []) == True
