#encoding:UTF-8

import unittest
import math

class Solution(object):
    @staticmethod
    def licenseKeyFormatting(S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        s = ''.join([i.upper() for i in S if i !='-'])[::-1]
        cnt = int(math.ceil(len(s)/float(K)))
        ret = '-'.join([s[i*K:i*K+K] for i in range(cnt)])
        return ret[::-1]
    
########################################################################
class SolutionTest(unittest.TestCase):
    """"""
    
    #----------------------------------------------------------------------
    def test_0(self):
        s = "2-4A0r7-4k"
        k = 3
        print Solution.licenseKeyFormatting(s, k)

#----------------------------------------------------------------------
def suite():
    """"""
    suite = unittest.TestSuite()
    suite.addTest(SolutionTest('test_0'))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suite')
    