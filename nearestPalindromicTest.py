#encoding:UTF-8

import os
import unittest
import numpy as np
from nearestPalindromic import Solution
    
class TestSolution(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_solution(self):
        n = '123'
        c = Solution.nearestPalindromic(n)
        self.assertEqual(c,'121')
    
    def test_solution_1(self):
        n = '1'
        c = Solution.nearestPalindromic(n)
        self.assertEqual(c,'0')
    
def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestSolution('test_solution'))
    suite.addTest(TestSolution('test_solution_1'))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suite')