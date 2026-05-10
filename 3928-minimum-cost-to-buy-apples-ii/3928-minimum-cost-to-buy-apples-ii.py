class Solution(object):
    def minCost(self, n, prices, roads):
        """
        :type n: int
        :type prices: List[int]
        :type roads: List[List[int]]
        :rtype: List[int]
        """
        adj1,adj2=[[] for _ in range(n)],[[] for _ in range(n)]
        for u,v,c,t in roads:
            adj1[u].append((v,c))
            adj1[v].append((u,c))
            adj2[u].append((v,c*t))
            adj2[v].append((u,c*t))
        def dj(node,adj):
            dist=[float('inf')]*n
            dist[node]=0
            pq=[(0,node)]
            while pq:
                d,u=heapq.heappop(pq)
                if d>dist[u]:
                    continue
                for v,w in adj[u]:
                    if dist[u]+w<dist[v]:
                        dist[v]=dist[u]+w
                        heapq.heappush(pq,(dist[v],v))
            return dist
        d1=[dj(i,adj1) for i in range(n)]
        d2=[dj(i,adj2) for i in range(n)]
        ans=[]
        for i in range(n):
            m=prices[i]
            for j in range(n):
                m=min(m,d1[i][j]+prices[j]+d2[j][i])
            ans.append(m)
        return ans