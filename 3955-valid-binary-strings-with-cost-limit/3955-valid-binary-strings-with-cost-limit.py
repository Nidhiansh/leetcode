class Solution(object):
    def generateValidStrings(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[str]
        """
        ans=[]
        def backtrack(i,path,last,cost):
            if cost>k:return
            if i==n:
                ans.append(path)
                return
            backtrack(i+1,path+'0','0',cost)
            if last!='1':backtrack(i+1,path+'1','1',cost+i)
        backtrack(0,'','0',0)
        return ans