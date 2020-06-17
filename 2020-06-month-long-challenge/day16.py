#!/usr/bin/env python3

# Day 16: Validate IP Address
#
# Write a function to check whether an input string is a valid IPv4 address or
# IPv6 address or neither.
#
# IPv4 addresses are canonically represented in dot-decimal notation, which
# consists of four decimal numbers, each ranging from 0 to 255, separated by
# dots ("."), e.g.,172.16.254.1; 
# Besides, leading zeros in the IPv4 is invalid. For example, the address
# 172.16.254.01 is invalid. 
#
# IPv6 addresses are represented as eight groups of four hexadecimal digits,
# each group representing 16 bits. The groups are separated by colons (":").
# For example, the address 2001:0db8:85a3:0000:0000:8a2e:0370:7334 is a valid
# one. Also, we could omit some leading zeros among four hexadecimal digits and
# some low-case characters in the address to upper-case ones, so
# 2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid IPv6 address(Omit leading
# zeros and using upper cases). 
# However, we don't replace a consecutive group of zero value with a single
# empty group using two consecutive colons (::) to pursue simplicity. For
# example, 2001:0db8:85a3::8A2E:0370:7334 is an invalid IPv6 address. 
# Besides, extra leading zeros in the IPv6 is also invalid. For example, the
# address 02001:0db8:85a3:0000:0000:8a2e:0370:7334 is invalid. 
#
# Note: You may assume there is no extra space or special characters in the
# input string. 

import re

class Solution:
    def validIPAddress(self, IP: str) -> str:
        def validV4(IP: str) -> bool:
            fields = IP.split(".")
            return len(fields) == 4 and all(map(lambda field: \
                    not (field.startswith("0") and field != "0")
                    and field.isnumeric()
                    and 0 <= int(field) < 256
                    , fields))

        def validV6(IP: str) -> bool:
            fields = IP.split(":")
            return len(fields) == 8 and all(map(lambda field: \
                    0 < len(field) < 5
                    and re.fullmatch('[0-9a-f]+', field, re.IGNORECASE) \
                        is not None
                    , fields))

        if "." in IP and validV4(IP):
            return "IPv4"
        if ":" in IP and validV6(IP):
            return "IPv6"
        return "Neither"

# Tests
assert Solution().validIPAddress("172.16.254.1") == "IPv4"
assert Solution().validIPAddress("256.256.256.256") == "Neither"
assert Solution().validIPAddress("172.16.254.01") == "Neither"
assert Solution().validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334") == "IPv6"
assert Solution().validIPAddress("02001:0db8:85a3:0000:0000:8a2e:0370:7334") == "Neither"
assert Solution().validIPAddress("2001:0db8:85a3::8A2E:0370:7334") == "Neither"
assert Solution().validIPAddress("192.0.0.1") == "IPv4"
