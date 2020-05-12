#!/usr/bin/env python3

# Day 11: Flood Fill
#
# An image is represented by a 2-D array of integers, each integer representing
# the pixel value of the image (from 0 to 65535).
# Given a coordinate (sr, sc) representing the starting pixel (row and column)
# of the flood fill, and a pixel value newColor, "flood fill" the image. 
# To perform a "flood fill", consider the starting pixel, plus any pixels
# connected 4-directionally to the starting pixel of the same color as the
# starting pixel, plus any pixels connected 4-directionally to those pixels
# (also with the same color as the starting pixel), and so on. Replace the
# color of all of the aforementioned pixels with the newColor. 
# At the end, return the modified image.
#
# Notes:
# - The length of image and image[0] will be in the range [1, 50].
# - The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc <
#   image[0].length.
# - The value of each color in image[i][j] and newColor will be an integer in
#   [0, 65535].

class Solution:
    def fill(self, image: [[int]], sr: int, sc: int, oldColor: int, newColor: int) -> [[int]]:
        if image[sr][sc] != oldColor:
            return image
        else:
            image[sr][sc] = newColor
            if sr > 0 and image[sr - 1][sc] != newColor:
                image = self.fill(image, sr - 1, sc, oldColor, newColor)
            if sr < len(image) - 1 and image[sr + 1][sc] != newColor:
                image = self.fill(image, sr + 1, sc, oldColor, newColor)
            if sc > 0 and image[sr][sc - 1] != newColor:
                image = self.fill(image, sr, sc - 1, oldColor, newColor)
            if sc < len(image[0]) -1 and image[sr][sc + 1] != newColor:
                image =  self.fill(image, sr, sc + 1, oldColor, newColor)
            return image

    def floodFill(self, image: [[int]], sr: int, sc: int, newColor: int) -> [[int]]:
        return self.fill(image, sr, sc, image[sr][sc], newColor)

# Test
assert Solution().floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2) == [[2,2,2],[2,2,0],[2,0,1]]
