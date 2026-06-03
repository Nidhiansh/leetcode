class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        n1=len(nums1)
        n2=len(nums2)
        if n1>n2:
            nums1,nums2=nums2,nums1
            n1,n2=n2,n1
        high=n1
        low=0
        mid=(n1+n2+1)//2
        while low<=high:
            m1=(low+high)//2
            m2=mid-m1
            l1,l2=float('-inf'),float('-inf')
            r1,r2=float('inf'),float('inf')
            if m1>0:
                l1=nums1[m1-1]
            if m1<n1:
                r1=nums1[m1]
            if m2>0:
                l2=nums2[m2-1]
            if m2<n2:
                r2=nums2[m2]
            if l1<=r2 and l2<=r1:
                if (n1+n2)%2==1:
                    return max(l1,l2)
                else:
                    return (max(l1,l2)+min(r1,r2))/2.0
            else:
                if l1>r2:
                    high=m1-1
                else:
                    low=m1+1

