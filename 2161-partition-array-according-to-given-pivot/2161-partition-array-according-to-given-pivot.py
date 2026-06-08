class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        s=0
        e=0
        g=0
        for i in nums:
            if i<pivot:
                s+=1
            if i==pivot:
                e+=1
            if i>pivot:
                g+=1
        l=[0]*len(nums)
        i=0
        j=s
        k=s+e
        for num in nums:
            if num<pivot:
                l[i]=num
                i+=1
            if num==pivot:
                l[j]=num
                j+=1
            if num>pivot:
                l[k]=num
                k+=1
        return l