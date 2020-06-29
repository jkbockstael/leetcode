#!/usr/bin/env python3

# Day 28: Reconstruct Itinerary
#
# Given a list of airline tickets represented by pairs of departure and arrival
# airports [from, to], reconstruct the itinerary in order. All of the tickets
# belong to a man who departs from JFK. Thus, the itinerary must begin with
# JFK.
#
# Note:
# - If there are multiple valid itineraries, you should return the itinerary
#   that has the smallest lexical order when read as a single string. For
#   example, the itinerary ["JFK", "LGA"] has a smaller lexical order than
#   ["JFK", "LGB"].
# - All airports are represented by three capital letters (IATA code).
# - You may assume all tickets form at least one valid itinerary.
# - One must use all the tickets once and only once.

from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: [[str]]) -> [str]:
        # Build the graph
        graph = defaultdict(list)
        origin = lambda ticket: ticket[0]
        destination = lambda ticket: ticket[1]
        for ticket in tickets:
            graph[origin(ticket)].append(destination(ticket))
        for node in graph:
            # Sort the neighbors in reverse lexicographical order, as we will
            # be popping them from the end
            graph[node] = sorted(graph[node], reverse=True)
        # Now trace the path starting at JFK
        path = []
        stack = ["JFK"]
        peek = lambda stack: stack[-1]
        while len(stack) > 0:
            node = peek(stack)
            if len(graph[node]) > 0:
                stack.append(graph[node].pop())
            else:
                path.append(stack.pop())
        return path[::-1]

# Tests
assert Solution().findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]) == ["JFK", "MUC", "LHR", "SFO", "SJC"]
assert Solution().findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]) == ["JFK","ATL","JFK","SFO","ATL","SFO"]
assert Solution().findItinerary([["JFK","ATL"],["ORD","PHL"],["JFK","ORD"],["PHX","LAX"],["LAX","JFK"],["PHL","ATL"],["ATL","PHX"]]) == ["JFK","ATL","PHX","LAX","JFK","ORD","PHL","ATL"]
assert Solution().findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]) == ["JFK","NRT","JFK","KUL"]
assert Solution().findItinerary([["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]]) == ["JFK","AXA","AUA","ADL","ANU","AUA","ANU","EZE","ADL","EZE","ANU","JFK","AXA","EZE","TIA","AUA","AXA","TIA","ADL","EZE","HBA"]
