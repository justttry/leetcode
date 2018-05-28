#encoding:UTF-8

import os
import numpy as np

# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    @staticmethod
    def maxPoints(points):
        """
        :type points: List[Point]
        :rtype: int
        """
        return 3