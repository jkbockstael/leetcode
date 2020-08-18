#!/usr/bin/env python3

# Day 17: Distribute Candies to People
#
# We distribute some number of candies, to a row of n = num_people people in
# the following way:
# We then give 1 candy to the first person, 2 candies to the second person, and
# so on until we give n candies to the last person.
# Then, we go back to the start of the row, giving n + 1 candies to the first
# person, n + 2 candies to the second person, and so on until we give 2 * n
# candies to the last person.
# This process repeats (with us giving one more candy each time, and moving to
# the start of the row after we reach the end) until we run out of candies.
# The last person will receive all of our remaining candies (not necessarily
# one more than the previous gift).
#
# Return an array (of length num_people and sum candies) that represents the
# final distribution of candies.
#
# Constraints:
# - 1 <= candies <= 10^9
# - 1 <= num_people <= 1000

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> [int]:
        distribution = [0 for _ in range(num_people)]

        # How many full rounds can we do?
        # The first round will be 1, 2, 3, ..., n
        # The second one will be n + 1, n + 2, n + 3, ... 2n
        # The third one will be 2n + 1, 2n + 2, 2n + 3, ... 3n
        # This means a total of n * (n + 1) / 2 + (round - 1) * n^2 for each
        # round
        rounds = 0
        while True:
            round_candies = num_people * (num_people + 1) // 2 \
                + rounds * num_people ** 2
            if round_candies > candies:
                break
            else:
                candies -= round_candies
                rounds += 1

        # Now that we know how many full rounds can be done, we can give all
        # these rounds worth of candies
        if rounds > 0:
            distribution = [sum(round * num_people + position 
                for round in range(rounds))
                for position in range(1, num_people + 1)]

        # Then distribute the leftovers
        position = 0
        while candies > 0:
            handout = rounds * num_people + position + 1
            distribution[position] += min(candies, handout)
            candies -= handout
            position += 1

        return distribution

# Tests
assert Solution().distributeCandies(10, 3) == [5,2,3]
assert Solution().distributeCandies(7, 4) == [1,2,3,1]
assert Solution().distributeCandies(10, 3) == [5,2,3]
assert Solution().distributeCandies(60, 4) == [15,18,15,12]
