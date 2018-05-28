#encoding:UTF-8

import os
import unittest
import numpy as np
from maxPoints import Point
from maxPoints import Solution
    
class TestSolution(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_solution(self):
        ps = [[1,1],[2,2],[3,3]]
        ps = [Point(*i) for i in ps]
        c = Solution.maxPoints(ps)
        self.assertEqual(c, 3)
    
    def test_solution_1(self):
        ps = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
        ps = [Point(*i) for i in ps]
        c = Solution.maxPoints(ps)
        self.assertEqual(c, 4)
    
def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestSolution('test_solution'))
    suite.addTest(TestSolution('test_solution_1'))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suite')