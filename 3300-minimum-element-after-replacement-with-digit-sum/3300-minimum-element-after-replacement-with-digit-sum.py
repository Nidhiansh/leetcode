class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=float('inf')
        for num in nums:
            c=0
            while num>0:
                c+=num%10
                num//=10
            res=min(res, c)
        return res