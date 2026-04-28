class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def rec(n,s):
            if n==1:
                return s
            c=1
            i=0
            temp=""
            while i<len(s):
                if i+1<len(s) and s[i]==s[i+1]:
                    c+=1
                else:
                    temp+=str(c)+s[i]
                    c=1
                i+=1
            return rec(n-1,temp)
        return rec(n,"1")
