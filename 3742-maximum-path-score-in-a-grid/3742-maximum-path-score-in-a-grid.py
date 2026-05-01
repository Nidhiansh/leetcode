class Solution(object):
    def maxPathScore(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        m=len(grid)
        n=len(grid[0])
        dp={}
        def solve(r,c,temp):
            cost=1 if grid[r][c]>0 else 0
            score=grid[r][c]
            if temp<cost:
                return -float('inf')
            if r==m-1 and c==n-1:
                return grid[r][c]
            if (r,c,temp) in dp:
                return dp[(r,c,temp)]
            res=-float('inf')
            if r+1<m:
                res=max(res,solve(r+1,c,temp-cost))
            if c+1<n:
                res=max(res,solve(r,c+1,temp-cost))
            dp[(r,c,temp)]=res+score if res!=-float('inf') else -float('inf')
            return dp[(r,c,temp)]
        ans=solve(0,0,k)
        return int(ans) if ans!=-float('inf') else -1
        