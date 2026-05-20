class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        n=len(grid)
        m=len(grid[0])
        vis=[[False]*m for _ in range(n)]
        dir=[(0,1),(1,0),(-1,0),(0,-1)]
        def bfs(x,y):
            q=deque()
            q.append((x,y))
            vis[x][y]=True
            while q:
                x,y=q.popleft()
                for i,j in dir:
                    nx,ny=x+i,y+j
                    if 0<=nx<n and 0<=ny<m and (not vis[nx][ny]) and grid[nx][ny]=="1":
                        vis[nx][ny]=True
                        q.append((nx,ny))
        res=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]=="1" and not vis[i][j]:
                    bfs(i,j)
                    res+=1
        return res