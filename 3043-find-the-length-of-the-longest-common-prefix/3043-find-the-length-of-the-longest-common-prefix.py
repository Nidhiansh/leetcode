class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        pre=set()
        for num in arr2:
            s=str(num)
            for i in range(1,len(s)+1):
                pre.add(s[:i])
        ans = 0
        for num in arr1:
            s=str(num)
            for i in range(len(s),0,-1):
                if s[:i] in pre:
                    ans=max(ans,i)
                    break
        return ans