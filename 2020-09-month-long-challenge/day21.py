#!/usr/bin/env python3

# Day 21: Car Pooling
#
# You are driving a vehicle that has capacity empty seats initially available
# for passengers.  The vehicle only drives east (ie. it cannot turn around and
# drive west.)
# Given a list of trips, trip[i] = [num_passengers, start_location,
# end_location] contains information about the i-th trip: the number of
# passengers that must be picked up, and the locations to pick them up and drop
# them off.  The locations are given as the number of kilometers due east from
# your vehicle's initial location.
#
# Return true if and only if it is possible to pick up and drop off all
# passengers for all the given trips. 

class Solution:
    def carPooling(self, trips: [[int]], capacity: int) -> bool:
        stops = []
        for people, start, end in trips:
            stops.append((start, people))
            stops.append((end, -people))
        
        stops.sort()
        
        for _, people in stops:
            capacity -= people
            if capacity < 0:
                return False
        return True

# Tests
assert Solution().carPooling([[2,1,5],[3,3,7]], 4) == False
assert Solution().carPooling([[2,1,5],[3,3,7]], 5) == True
assert Solution().carPooling([[2,1,5],[3,5,7]], 3) == True
assert Solution().carPooling([[3,2,7],[3,7,9],[8,3,9]], 11) == True
