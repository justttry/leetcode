#encoding:UTF-8

import os
import numpy as np

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    @staticmethod
    def swapPairs(head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def getSubNodes(l):
            if l is None:
                return None
            elif l.next is None:
                return l
            else:
                a = l
                b = l.next
                ret = ListNode(b.val)
                ret.next = ListNode(a.val)
                ret.next.next = getSubNodes(b.next)
            return ret
        return getSubNodes(head)
                