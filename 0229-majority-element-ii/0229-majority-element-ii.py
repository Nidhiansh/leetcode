class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=[]
        d={}
        for i in nums:
            d[i]=0
        for i in nums:
            d[i]+=1
        for i in d:
            if d[i]>(len(nums)/3):
                l.append(i)
        return l