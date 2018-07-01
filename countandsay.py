#encoding:UTF-8

import unittest

class Solution(object):
    @staticmethod
    def countAndSay(n):
        """
        :type n: int
        :rtype: str
        """
        def rets(s):
            cnt = 0
            a = None
            ret = ''
            for i in s:
                if a != i:
                    if a:
                        ret += str(cnt)
                        ret += a
                    a = i
                    cnt = 1
                else:
                    cnt += 1
            ret += str(cnt)
            ret += a
            return ret
        if n <= 1:
            return '1'
        y = '1'
        for j in range(n):
            y = rets(y)
        return y
    
    
########################################################################
class CountAndSayTest(unittest.TestCase):
    """"""
    
    #----------------------------------------------------------------------
    def test_0(self):
        print Solution.countAndSay(1)
    
    #----------------------------------------------------------------------
    def test_1(self):
        print Solution.countAndSay(2)
    
    #----------------------------------------------------------------------
    def test_2(self):
        print Solution.countAndSay(3)
    
    #----------------------------------------------------------------------
    def test_3(self):
        print Solution.countAndSay(4)
    
    #----------------------------------------------------------------------
    def test_4(self):
        print Solution.countAndSay(5)
    
    #----------------------------------------------------------------------
    def test_5(self):
        print Solution.countAndSay(6)
        
        
#----------------------------------------------------------------------
def suite():
    """"""
    suite = unittest.TestSuite()
    suite.addTest(CountAndSayTest('test_0'))
    suite.addTest(CountAndSayTest('test_1'))
    suite.addTest(CountAndSayTest('test_2'))
    suite.addTest(CountAndSayTest('test_3'))
    suite.addTest(CountAndSayTest('test_4'))
    suite.addTest(CountAndSayTest('test_5'))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suite')