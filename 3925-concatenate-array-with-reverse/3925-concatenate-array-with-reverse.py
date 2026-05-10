class Solution(object):
    def concatWithReverse(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        for i in nums:
            ans.append(i)
        n=len(nums)
        for i in range(n-1,-1,-1):
            ans.append(nums[i])
        return ans