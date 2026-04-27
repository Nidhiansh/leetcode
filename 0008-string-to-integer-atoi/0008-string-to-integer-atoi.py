class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.lstrip()
        if not s:
            return 0
        res,i,sign=0,0,1
        if s[i]=='-':
            sign=-1
            i+=1
        elif s[i]=='+':
            i+=1
        while i<len(s) and s[i].isdigit():
            res=res*10+int(s[i])
            i+=1
        res*=sign
        return max(-2**31, min(res, 2**31-1))