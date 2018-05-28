#encoding:UTF-8

import os
import unittest
import numpy as np
from swapNodesInPairs import ListNode
from swapNodesInPairs import Solution
    
class TestSolution(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_solution(self):
        a = ListNode(2)
        a.next = ListNode(4)
        a.next.next = ListNode(3)
        a.next.next.next = ListNode(5)
        c = Solution.swapPairs(a)
        self.assertEqual(c.val, 4)
        self.assertEqual(c.next.val, 2)
        self.assertEqual(c.next.next.val, 5)
        self.assertEqual(c.next.next.next.val, 3)
    
def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestSolution('test_solution'))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suite')