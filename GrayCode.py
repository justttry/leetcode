#encoding:UTF-8

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def gray(n):
            if n == 1:
                return [0, 1]
            else:
                ret = gray(n - 1)
                return ret + [2**(n-1) + i for i in ret[::-1]]
        return gray(n)
            