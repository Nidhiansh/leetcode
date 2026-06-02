class Solution(object):
    def digitFrequencyScore(self, n):
        """
        :type n: int
        :rtype: int
        """
        d={}
        while n!=0:
            a=n%10
            d[a]=d.get(a,0)+1
            n=n//10
        res=0
        for i in d:
            res+=i*d[i]
        return res