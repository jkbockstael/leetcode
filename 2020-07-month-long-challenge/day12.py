#!/usr/bin/env python3

# Day 11: Reverse Bits
#
# Reverse bits of a given 32 bits unsigned integer.

class Solution:
    def reverseBits(self, n: int) -> int:
        # This can be written as a one-liner, but here's a breakdown:
        output = bin(n) # parse the input
        output = output[2:] # get rid of "0b"
        output = output.zfill(32) # pad with zeroes for a total length of 32
        output = reversed(output) # reverse the whole thing
        output = ''.join(output) # collect the reverse iterator into a string
        output = int(output, 2) # parse that to an integer
        return output

# Tests
assert Solution().reverseBits(43261596) == 964176192
assert Solution().reverseBits(4294967293) == 3221225471
