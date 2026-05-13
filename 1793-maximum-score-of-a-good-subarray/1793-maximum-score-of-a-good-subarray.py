class Solution(object):
    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i=j=k
        m=score=nums[k]
        n=len(nums)
        while i>=0 and j<=n-1:
            lval=nums[i-1] if i>0 else -1
            rval=nums[j+1] if j<n-1 else -1
            if lval>rval:
                i-=1
                m=min(m,lval)
                score=max(score,m*(j-i+1))
            else:
                j+=1
                m=min(m,rval)
            score=max(score,m*(j-i+1))
        return score