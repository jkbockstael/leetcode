#!/usr/bin/env python3

# Day 3: Valid Palindrome
#
# Given a string, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
            if not s[right].isalnum():
                right -= 1
            if s[left].isalnum() and s[right].isalnum():
                if s[left].lower() != s[right].lower():
                    return False
                else:
                    left += 1
                    right -= 1
        return True

# Tests
assert Solution().isPalindrome("A man, a plan, a canal: Panama") == True
assert Solution().isPalindrome("race a car") == False
