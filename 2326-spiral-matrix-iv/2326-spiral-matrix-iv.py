# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def spiralMatrix(self, m, n, head):
        """
        :type m: int
        :type n: int
        :type head: Optional[ListNode]
        :rtype: List[List[int]]
        """
        res,seen=[[-1]*n for _ in range(m)],[[False]*n for _ in range(m)]
        dr=[0,1,0,-1]
        dc=[1,0,-1,0]
        r=c=di=0
        while head:
            res[r][c]=head.val
            seen[r][c]=True
            head=head.next
            nr,nc=r+dr[di],c+dc[di]
            if 0<=nr<m and 0<=nc<n and not seen[nr][nc]:
                r,c=nr,nc
            else:
                di=(di+1)%4
                r,c=r+dr[di],c+dc[di]
        return res