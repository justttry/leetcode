#encoding:UTF-8

import unittest

class Solution(object):
    
    @staticmethod
    def repeatedSubstringPattern(s):
        """
        :type s: str
        :rtype: bool
        """
        length = len(s)
        if length <= 1:
            return False
        x = 1
        while x ** 2 <= length:
            if length % x == 0:
                y = length / x
                if len(set([s[x*i:x*i+x] for i in range(y)])) == 1:
                    return True
                elif x!=1 and len(set(s[y*i:y*i+y] for i in range(x))) == 1:
                    return True
            x += 1
        return False
    
    
########################################################################
class SolutionTest(unittest.TestCase):
    """"""
    
    #----------------------------------------------------------------------
    def test_0(self):
        s = 'abab'
        print Solution.repeatedSubstringPattern(s)
    
    #----------------------------------------------------------------------
    def test_1(self):
        s = 'bb'
        print Solution.repeatedSubstringPattern(s)
    
    #----------------------------------------------------------------------
    def test_2(self):
        s = 'aba'
        print Solution.repeatedSubstringPattern(s)
    
    #----------------------------------------------------------------------
    def test_3(self):
        s = 'a'
        print Solution.repeatedSubstringPattern(s)
        
#----------------------------------------------------------------------
def suite():
    """"""
    suite = unittest.TestSuite()
    suite.addTest(SolutionTest('test_0'))
    suite.addTest(SolutionTest('test_1'))
    suite.addTest(SolutionTest('test_2'))
    suite.addTest(SolutionTest('test_3'))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suite')