class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        j=0
        res=0
        for i in range(len(s)):
            if j<len(g) and g[j]<=s[i]:
                j+=1
                res+=1
        return res