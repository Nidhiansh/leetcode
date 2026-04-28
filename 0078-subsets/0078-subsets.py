class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n=len(nums)
        res=[]
        def rec(i,temp):
            if i==n:
                res.append(temp[:])
                return
            temp.append(nums[i])
            rec(i+1,temp)
            temp.pop()
            rec(i+1,temp)
        rec(0,[])
        return res