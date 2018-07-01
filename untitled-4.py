#encoding:UTF-8

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        tmp = s
        for _ in range(len(s)):
            tmp = tmp[1:] + tmp[0]
            if tmp == s:
                return True
        return False