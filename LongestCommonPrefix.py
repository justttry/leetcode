#Encoding:UTF-8

import unittest


########################################################################
class Solution(object):
    """"""
    
    #----------------------------------------------------------------------\
    @staticmethod
    def longestCommonPrefix(strs):
        ret = ''
        if not strs:
            return ret
        for i, j in enumerate(strs[0]):
            for k in strs[1:]:
                if not k[i:]:
                    return ret
                elif j != k[i]:
                    return ret
            ret += j
        return ret
        
    
    