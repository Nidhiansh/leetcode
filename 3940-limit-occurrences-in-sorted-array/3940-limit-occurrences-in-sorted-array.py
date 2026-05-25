class Solution(object):
    def limitOccurrences(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res=[]
        for x in nums:
            if len(res)<k or res[-k]!=x:
                res.append(x)
        return res

        