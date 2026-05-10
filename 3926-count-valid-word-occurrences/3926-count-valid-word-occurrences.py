class Solution(object):
    def countWordOccurrences(self, chunks, queries):
        """
        :type chunks: List[str]
        :type queries: List[str]
        :rtype: List[int]
        """
        s="".join(chunks)
        n,d,curr,i=len(s),{},[],0
        while i<n:
            if s[i].islower():
                curr.append(s[i])
            elif s[i]=='-' and i>0 and i<n-1 and s[i-1].islower() and s[i+1].islower():
                curr.append(s[i])
            else:
                if curr:
                    w="".join(curr)
                    d[w]=d.get(w,0)+1
                    curr=[]
            i+=1
        if curr:
            w="".join(curr)
            d[w]=d.get(w,0)+1
        return [d.get(i,0) for i in queries]