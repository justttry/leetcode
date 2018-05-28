#encoding:UTF-8

import os
import unittest
import numpy as np
from mergeKSortedLists import ListNode
from mergeKSortedLists import Solution
    
class TestSolution(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_solution(self):
        a = ListNode(1)
        a.next = ListNode(4)
        a.next.next = ListNode(5)
        b = ListNode(1)
        b.next = ListNode(3)
        b.next.next = ListNode(4)
        c = ListNode(2)
        c.next = ListNode(6)
        d = Solution.mergeKLists([a, b, c])
        self.assertEqual(d.val, 1)
        self.assertEqual(d.next.val, 1)
        self.assertEqual(d.next.next.val, 2)
        d = d.next.next.next
        self.assertEqual(d.val, 3)
        self.assertEqual(d.next.val, 4)
        self.assertEqual(d.next.next.val, 4)
        d = d.next.next.next
        self.assertEqual(d.val, 5)
        self.assertEqual(d.next.val, 6)
    
    def test_solution_1(self):
        a = ListNode(1)
        a.next = ListNode(4)
        a.next.next = ListNode(5)
        b = ListNode(1)
        b.next = ListNode(3)
        b.next.next = ListNode(4)
        c = ListNode(None)
        d = Solution.mergeKLists([a, b, c])
        self.assertEqual(d.val, 1)
        self.assertEqual(d.next.val, 1)
        self.assertEqual(d.next.next.val, 3)
        d = d.next.next.next
        self.assertEqual(d.val, 4)
        self.assertEqual(d.next.val, 4)
        self.assertEqual(d.next.next.val, 5)
    
    def test_solution_2(self):
        a = ListNode(None)
        b = ListNode(None)
        c = ListNode(None)
        d = Solution.mergeKLists([a, b, c])
        self.assertIsNone(d)
        
    
def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestSolution('test_solution'))
    suite.addTest(TestSolution('test_solution_1'))
    suite.addTest(TestSolution('test_solution_2'))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suite')