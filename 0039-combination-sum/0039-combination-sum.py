class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n=len(candidates)
        res=[]
        def rec(start,target,temp):
            if target<0:
                return
            elif target==0:
                res.append(temp[:])
            else:
                for i in range(start,n):
                    temp.append(candidates[i])
                    rec(i,target-candidates[i],temp)
                    temp.pop()
        candidates.sort()
        rec(0,target,[])
        return res