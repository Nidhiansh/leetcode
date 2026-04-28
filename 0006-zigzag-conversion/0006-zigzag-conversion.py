class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1 or numRows>=len(s):
            return s
        res=[""]*numRows
        j=0
        step=1
        for i in s:
            res[j]+=i
            if j==0:
                step=1
            elif j==numRows-1:
                step=-1
            j+=step
        return "".join(res)