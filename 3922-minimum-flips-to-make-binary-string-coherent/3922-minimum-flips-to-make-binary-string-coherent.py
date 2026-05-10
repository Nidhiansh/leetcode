class Solution(object):
    def minFlips(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        if n<3:
            return 0
        n1=s.count('1')
        n0=len(s)-n1
        res1=n0
        res2=max(n1-1,0)
        res3=n1-int(s[0])-int(s[-1])
        return min(res1,res2,res3)