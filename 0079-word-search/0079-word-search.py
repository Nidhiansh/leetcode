class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        n1=len(word)
        n=len(board)
        m=len(board[0])
        def rec(i,x,y):
            if 0>x or x>=n or 0>y or y>=m or board[x][y]!=word[i]:
                return False
            if i==n1-1:
                return True
            temp=board[x][y]
            board[x][y]="#"
            res=rec(i+1,x+1,y) or rec(i+1,x,y+1) or rec(i+1,x-1,y) or rec(i+1,x,y-1)
            board[x][y]=temp
            return res
        for r in range(n):
            for c in range(m):
                if rec(0,r,c):
                    return True
        return False
                