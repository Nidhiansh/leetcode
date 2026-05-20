class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        n=len(A)
        l=[False]*(n+1)
        C=[]
        count=0
        for i in range(n):
            if l[A[i]]:
                count+=1
            else:
                l[A[i]]=True
            
            if l[B[i]]:
                count+=1
            else:
                l[B[i]]=True
            C.append(count)
        return C