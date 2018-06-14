#encoding:UTF-8

import os
import unittest
import numpy as np
from strongPasswordChecker import Solution
    
class TestSolution(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_solution(self):
        n = '123'
        c = Solution.strongPasswordChecker(n)
        self.assertEqual(c,'121')
    
def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestSolution('test_solution'))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suite')