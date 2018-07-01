#encoding:UTF-8

import unittest

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    @staticmethod
    def getMinimumDifference(root):
        """
        :type root: TreeNode
        :rtype: int
        """
        length = len(root)
        ret = 1e100
        for i in range(length/2):
            if root[2*i+1] is not None:
                a = abs(root[i] - root[2*i+1])
                if a < ret:
                    ret = a
            if root[2*i+1] is not None:
                a = abs(root[i] - root[2*i+2])
                if a < ret:
                    ret = a
        return ret
    

########################################################################
class SolutionTest(unittest.TestCase):
    """"""
    
    #----------------------------------------------------------------------
    def test_0(self):
        root = [236,104,701,None,227,None,911]
        print Solution.getMinimumDifference(root)
        
#----------------------------------------------------------------------
def suite():
    """"""
    suite = unittest.TestSuite()
    suite.addTest(SolutionTest('test_0'))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suite')
    
    