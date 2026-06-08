class Solution(object):
    def sumOfGoodIntegers(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        res=0
        for i in range(max(n-k,1),n+k+1):
            if abs(n-i)<=k and (n&i)==0:
                res+=i
        return res