class Solution(object):
    def permute(self, nums):
        n=len(nums)
        used=[False]*n
        def rec(temp):
            if len(temp)==n:
                res.append(temp[:])
                return
            for i in range(n):
                if not used[i]:
                    used[i]=True
                    temp.append(nums[i])
                    rec(temp)
                    temp.pop()
                    used[i]=False
        res=[]
        rec([])
        return res