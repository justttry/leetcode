#encoding:UTF-8

import os
import unittest
import numpy as np
from addTwoNumbers import ListNode
from addTwoNumbers import Solution
    
class TestSolution(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_solution(self):
        a = ListNode(2)
        a.next = ListNode(4)
        a.next.next = ListNode(3)
        b = ListNode(5)
        b.next = ListNode(6)
        b.next.next = ListNode(4)
        c = Solution.addTwoNumbers(a, b)
        self.assertEqual(c.val, 7)
        self.assertEqual(c.next.val, 0)
        self.assertEqual(c.next.next.val, 8)
    
def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestSolution('test_solution'))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suite')