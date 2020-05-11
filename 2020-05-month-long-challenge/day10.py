#!/usr/bin/env python3

# Day 10: Find the Town Judge
#
# In a town, there are N people labelled from 1 to N.  There is a rumor that
# one of these people is secretly the town judge.
# If the town judge exists, then:
# - The town judge trusts nobody.
# - Everybody (except for the town judge) trusts the town judge.
# - There is exactly one person that satisfies properties 1 and 2.
#
# You are given trust, an array of pairs trust[i] = [a, b] representing that
# the person labelled a trusts the person labelled b.
# If the town judge exists and can be identified, return the label of the town
# judge.  Otherwise, return -1.
#
# Constraints:
# - 1 <= N <= 1000
# - trust.length <= 10000
# - trust[i] are all different
# - trust[i][0] != trust[i][1]
# - 1 <= trust[i][0], trust[i][1] <= N

class Solution:
    def findJudge(self, N: int, trust: [[int]]) -> int:
        # People are numbered starting at 1, we'll offset indices by 1
        trust_in = [0 for _ in range(N)]
        trust_out = [0 for _ in range(N)]
        for t in trust:
            trust_out[t[0] - 1] += 1
            trust_in[t[1] - 1] += 1
        for i in range(N):
            if trust_in[i] == N - 1 and trust_out[i] == 0:
                return i + 1
        return -1

# Tests
assert Solution().findJudge(2, [[1,2]]) == 2
assert Solution().findJudge(3, [[1,3],[2,3]]) == 3
assert Solution().findJudge(3, [[1,3],[2,3],[3,1]]) == -1
assert Solution().findJudge(3, [[1,2],[2,3]]) == -1
assert Solution().findJudge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]]) == 3
assert Solution().findJudge(1, []) == 1
