#encoding:UTF-8

import os
import numpy as np
import unittest

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    @staticmethod
    def addTwoNumbers(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def get_number(l):
            if l.next is None:
                return l.val
            else:
                return l.val + 10 * get_number(l.next)
        def get_node(v):
            if v < 10:
                return ListNode(v)
            else:
                a = ListNode(v%10)
                a.next = get_node(v//10)
                return a
        l1_v = get_number(l1)
        l2_v = get_number(l2)
        sum_ = l1_v + l2_v
        return get_node(sum_)
        