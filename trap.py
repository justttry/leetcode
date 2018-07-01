#encoding:UTF-8

import unittest

class Solution(object):
    @staticmethod
    def trap(height):
        """
        :type height: List[int]
        :rtype: int
        """
        high = 0
        a = []
        b = []
        c = []
        length = len(height)
        for i in height:
            if i >= high:
                high = i
            a.append(high)
        high = 0
        for i in height[::-1]:
            if i >= high:
                high = i
            b.append(high)
        c = [a[i] if a[i] < b[length-1-i] else b[length-1-i] for i in range(length)]
        return sum([c[i] - height[i] for i in range(length)])
    
########################################################################
class SolutionTest(unittest.TestCase):
    """"""
    
    #----------------------------------------------------------------------
    def test_0(self):
        a = [0,1,0,2,1,0,1,3,2,1,2,1]
        print Solution.trap(a)

#----------------------------------------------------------------------
def suite():
    """"""
    suite = unittest.TestSuite()
    suite.addTest(SolutionTest('test_0'))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suite')