class Solution(object):
    def minOperations(self, grid, x):
        """
        :type grid: List[List[int]]
        :type x: int
        :rtype: int
        """
        l=[]
        for i in grid:
            for j in i:
                l.append(j)
        l.sort()
        k=len(l)
        k=l[k//2]
        res=0
        for i in l:
            temp=abs(i-k)
            if temp%x!=0:
                return -1
            res+=temp//x
        return res