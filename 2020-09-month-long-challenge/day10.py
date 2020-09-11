#!/usr/bin/env python3

# Day 10: Bulls and Cows
#
# You are playing the following Bulls and Cows game with your friend: You write
# down a number and ask your friend to guess what the number is. Each time your
# friend makes a guess, you provide a hint that indicates how many digits in
# said guess match your secret number exactly in both digit and position
# (called "bulls") and how many digits match the secret number but locate in
# the wrong position (called "cows"). Your friend will use successive guesses
# and hints to eventually derive the secret number.
#
# Write a function to return a hint according to the secret number and friend's
# guess, use A to indicate the bulls and B to indicate the cows. 
#
# Please note that both secret number and friend's guess may contain duplicate
# digits.
# You may assume that the secret number and your friend's guess only contain
# digits, and their lengths are always equal.

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = sum(1 for i in range(len(secret)) if secret[i] == guess[i])
        cows = sum(min(secret.count(n), guess.count(n)) for n in set(guess))
        return f'{bulls}A{cows - bulls}B'


# Tests
assert Solution().getHint("1807", "7810") == "1A3B"
assert Solution().getHint("1123", "0111") == "1A1B"
