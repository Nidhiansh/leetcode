class Solution(object):
    def findValidElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        if n==1:
            return nums
        pre=[0]*n
        suf=[0]*n
        pre[0]=nums[0]
        for i in range(1,n):
            pre[i]=max(pre[i-1],nums[i])
        suf[n-1]=nums[n-1]
        for i in range(n-2,-1,-1):
            suf[i]=max(suf[i+1],nums[i])
        res=[]
        res.append(nums[0])
        for i in range(1,n-1):
            if nums[i]>pre[i-1] or nums[i]>suf[i+1]:
                res.append(nums[i])
        res.append(nums[n-1])
        return res