class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        dir=[[(0,-1),(0,1)],[(-1,0),(1,0)],[(0,-1),(1,0)],[(0,1),(1,0)],[(0,-1),(-1,0)],[(-1,0),(0,1)]]
        q=deque()
        q.append((0,0))
        m=len(grid)
        n=len(grid[0])
        vis=[[-1]*n for _ in range(m)]
        while q:
            x,y=q.popleft()
            vis[x][y]=1
            val=grid[x][y]
            if x==m-1 and y==n-1:
                return True
            for i,j in dir[val-1]:
                nx,ny=x+i,y+j
                if 0<=nx<m and 0<=ny<n:
                    if (-i,-j) in dir[grid[nx][ny]-1] and vis[nx][ny]==-1:
                        q.append((nx,ny))
                        vis[nx][ny]=1
        return False