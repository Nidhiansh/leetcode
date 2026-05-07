class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need={}
        for i in t:
            need[i]=need.get(i,0)+1
        l,r,valid=0,0,0
        start,length=0,float('inf')
        win={}
        while r<len(s):
            a=s[r]
            r+=1
            if a in need:
                win[a]=win.get(a,0)+1
                if win[a]==need[a]:
                    valid+=1
            while valid==len(need):
                if r-l<length:
                    start=l
                    length=r-l
                d=s[l]
                l+=1
                if d in need:
                    if win[d]==need[d]:
                        valid-=1
                    win[d]-=1
        return "" if length==float('inf') else s[start:start+length]