class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        for i in nums:
            temp=i
            t1=0
            l=[]
            while temp!=0:
                t1=temp%10
                temp=temp//10
                l.append(t1)
            res.extend(l[::-1])
        return res