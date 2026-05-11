class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        R,C=len(matrix),len(matrix[0])
        res,seen=[],[[False]*C for _ in range(R)]
        dr=[0,1,0,-1]
        dc=[1,0,-1,0]
        r=c=di=0
        for _ in range(R*C):
            res.append(matrix[r][c])
            seen[r][c]=True
            nr,nc=r+dr[di],c+dc[di]
            if 0<=nr<R and 0<=nc<C and not seen[nr][nc]:
                r,c=nr,nc
            else:
                di=(di+1)%4
                r,c=r+dr[di],c+dc[di]
        return res