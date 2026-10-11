class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=0
        n=len(nums)
        for i in range(1,n+1):
            if n%i==0:
                res=res+nums[i-1]*nums[i-1]
        return res