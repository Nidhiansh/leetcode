class Solution(object):
    def maximumJumps(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp={}
        def rec(idx):
            if idx in dp:
                return dp[idx]
            if idx==0:
                return 0
            m=-float('inf')
            for i in range(idx):
                if abs(nums[idx]-nums[i])<=target:
                    res=rec(i)
                    if res!=-1:
                        m=max(m,1+res)
            dp[idx]=m if m!=-float('inf') else -1
            return dp[idx]
        return rec(len(nums)-1)