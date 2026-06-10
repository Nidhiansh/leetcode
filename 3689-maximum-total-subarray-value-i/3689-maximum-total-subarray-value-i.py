class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        mn=min(nums)
        mx=max(nums)
        return k*(mx-mn)
