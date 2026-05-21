class Solution(object):
    def getSubarrayBeauty(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        sl=SortedList()
        ans=[]
        for i in range(len(nums)):
            sl.add(nums[i])
            if i>=k:
                sl.remove(nums[i-k])
            if i>=k-1:
                val=sl[x-1]
                ans.append(val if val<0 else 0)
        return ans