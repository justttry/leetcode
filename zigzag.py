#encoding:UTF-8

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        lists = [[] for i in range(numRows)]
        for i, j in enumerate(s):
            t = i % (2 * numRows - 2)
            if t < numRows:
                lists[t].append(j)
            else:
                lists[2*numRows-2-t].append(j)
        return ''.join([''.join(i) for i in lists])
    

if __name__ == '__main__':
    a = Solution()
    print a.convert('PAYPALISHIRING', 3)