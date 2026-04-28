class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        nums=set(nums)
        res=[]
        for i in range(1,n+1):
            if i not in nums:
                res.append(i)
        return res