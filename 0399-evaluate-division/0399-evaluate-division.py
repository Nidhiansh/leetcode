class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        d={}
        idx=0
        for i in range(len(equations)):
            a,b=equations[i]
            if a not in d:
                d[a]=idx
                idx+=1
            if b not in d:
                d[b]=idx
                idx+=1
        adj=[{} for _ in range(len(d))]
        for i in range(len(equations)):
            a,b=equations[i]
            val=values[i]
            adj[d[a]][d[b]]=val
            adj[d[b]][d[a]]=1/val
        print(adj)
        vis=set()
        def dfs(u,v,vis,div):
            if u==v:
                return div
            vis.add(u)
            for nei,w in adj[u].items():
                if nei not in vis:
                    res=dfs(nei,v,vis,div*w)
                    if res!=-1.0:
                        return res
            return -1.0
        res=[]
        for a,b in queries:
            if a not in d or b not in d:
                res.append(-1.0)
            elif a==b:
                res.append(1.0)
            else:
                res.append(dfs(d[a],d[b],set(),1.0))
        return res