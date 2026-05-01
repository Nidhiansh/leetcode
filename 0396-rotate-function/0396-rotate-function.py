class Solution(object):
    def maxRotateFunction(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        ans=0
        func=0
        s=sum(nums)
        for i in range(n):
            func+=i*nums[i]
        ans=func
        for i in range(n):
            func=func+s-n*nums[n-1-i]
            ans=max(ans,func)
        return ans




