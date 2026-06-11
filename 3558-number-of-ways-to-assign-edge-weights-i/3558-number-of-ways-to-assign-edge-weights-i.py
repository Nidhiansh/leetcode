class Solution(object):
    def assignEdgeWeights(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        g={}
        for u,v in edges:
            if u not in g: g[u]=[]
            if v not in g: g[v]=[]
            g[u].append(v)
            g[v].append(u)
        q=deque([(1,0)])
        vis={1}
        max_k=0
        while q:
            u,d=q.popleft()
            max_k=max(max_k,d)
            if u in g:
                for v in g[u]:
                    if v not in vis:
                        vis.add(v)
                        q.append((v,d+1))
        return pow(2,max_k-1,10**9+7)