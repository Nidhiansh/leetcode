class Solution(object):
    def minimumSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        for i in nums:
            if i==0:
                c+=1
        res=0
        n=len(nums)
        for i in nums[n-c:]:
            if i==0:
                res+=1
        return c-res