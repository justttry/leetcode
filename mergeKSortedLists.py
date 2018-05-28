#encoding:UTF-8

import os
import numpy as np

#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    @staticmethod
    def mergeKLists(lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def get_values(lists):
            if len(lists) == 0:
                return []
            ret = [i.val for i in lists if i is not None]
            return ret + get_values([i.next for i in lists if i is not None])
        def get_next(node):
            return node.next
        values = get_values(lists)
        values = [i for i in values if i is not None]
        if len(values) == 0:
            return None
        values = sorted(values)[::-1]
        ret = ListNode(values[0])
        for i in values[1:]:
            new_ret = ListNode(i)
            new_ret.next = ret
            ret = new_ret
        return ret