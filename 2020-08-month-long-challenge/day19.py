#!/usr/bin/env python3

# Day 19: Goat Latin
#
# A sentence S is given, composed of words separated by spaces. Each word
# consists of lowercase and uppercase letters only.
# We would like to convert the sentence to "Goat Latin" (a made-up language
# similar to Pig Latin.)
#
# The rules of Goat Latin are as follows:
# - If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of
#   the word. 
#   For example, the word "apple" becomes "applema".
# - If a word begins with a consonant (i.e. not a vowel), remove the first
#   letter and append it to the end, then add "ma".
#   For example, the word "goat" becomes "oatgma".
# - Add one letter 'a' to the end of each word per its word index in the
#   sentence, starting with 1.
#   For example, the first word gets "a" added to the end, the second word gets
#   "aa" added to the end and so on.
#
# Return the final sentence representing the conversion from S to Goat Latin.
#
# Note:
# - S contains only uppercase, lowercase and spaces. Exactly one space between
#   each word.
# - 1 <= S.length <= 150

class Solution():
    def toGoatLatin(self, S: str) -> str:
        # Fun fun functional
        def goat(word):
            return word + "ma" if word.lower().startswith(("a","e","i","o","u")) \
                else word[1:] + word[0] + "ma"

        def baah(words):
            return [word + "a" * (position + 1) \
                for position, word in enumerate(words)]

        return " ".join(baah([goat(word) for word in S.split(" ")]))

# Tests
assert Solution().toGoatLatin("I speak Goat Latin") == "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
assert Solution().toGoatLatin("The quick brown fox jumped over the lazy dog") == "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
