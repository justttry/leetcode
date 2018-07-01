#encoding:UTF-8

import unittest

class Solution(object):
    @staticmethod
    def hammingDistance(x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        ret = 0
        while x != 0 or y != 0:
            if x%2 != y%2:
                ret += 1
            x = x>>1
            y = y>>1
        return ret
    
########################################################################
class SolutionTest(unittest.TestCase):
    """"""
    
    #----------------------------------------------------------------------
    def test_0(self):
        x = 1
        y = 4
        print Solution.hammingDistance(x, y)
    
    #----------------------------------------------------------------------
    def test_1(self):
        x = 1
        y = 3
        print Solution.hammingDistance(x, y)
        
#----------------------------------------------------------------------
def suite():
    """"""
    suite = unittest.TestSuite()
    suite.addTest(SolutionTest('test_0'))
    suite.addTest(SolutionTest('test_1'))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suite')
        
    
    